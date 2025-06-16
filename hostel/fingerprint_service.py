# fingerprint_service.py
from flask import Flask, jsonify, request
from flask_cors import CORS
import base64
import os
import sys
import time
import threading
from ctypes import *
import json

# Import Digital Persona SDK components
try:
    # You'll need to install the Digital Persona SDK and import the appropriate modules
    # This is a template - adjust imports based on your SDK installation
    from dpfpdd import *
    from dpfpenroll import *
    from dpfpverify import *
    SDK_AVAILABLE = True
except ImportError:
    print("Digital Persona SDK not found. Please install the SDK.")
    SDK_AVAILABLE = False

app = Flask(__name__)
CORS(app)  # Enable CORS for Django frontend

class FingerprintScanner:
    def __init__(self):
        self.reader = None
        self.enrollment = None
        self.template = None
        self.is_capturing = False
        self.capture_result = None
        
    def initialize_scanner(self):
        """Initialize the fingerprint scanner"""
        try:
            if not SDK_AVAILABLE:
                return False, "SDK not available"
                
            # Initialize the reader
            self.reader = DPFPReader()
            if not self.reader:
                return False, "Failed to initialize reader"
                
            # Get available readers
            readers = self.reader.get_readers()
            if not readers:
                return False, "No fingerprint readers found"
                
            # Use the first available reader
            self.reader.select_reader(readers[0])
            
            return True, "Scanner initialized successfully"
            
        except Exception as e:
            return False, f"Error initializing scanner: {str(e)}"
    
    def start_capture(self, callback=None):
        """Start fingerprint capture"""
        try:
            if not self.reader:
                success, message = self.initialize_scanner()
                if not success:
                    return False, message
            
            self.is_capturing = True
            self.capture_result = None
            
            # Start capture in a separate thread
            capture_thread = threading.Thread(target=self._capture_thread, args=(callback,))
            capture_thread.daemon = True
            capture_thread.start()
            
            return True, "Capture started"
            
        except Exception as e:
            return False, f"Error starting capture: {str(e)}"
    
    def _capture_thread(self, callback=None):
        """Thread function for capturing fingerprint"""
        try:
            timeout = 30  # 30 seconds timeout
            start_time = time.time()
            
            while self.is_capturing and (time.time() - start_time) < timeout:
                try:
                    # Capture fingerprint sample
                    sample = self.reader.capture_sample()
                    
                    if sample and sample.is_valid():
                        # Process the sample
                        template = self._process_sample(sample)
                        if template:
                            self.capture_result = {
                                'success': True,
                                'template': base64.b64encode(template).decode('utf-8'),
                                'message': 'Fingerprint captured successfully'
                            }
                            break
                            
                except Exception as e:
                    print(f"Capture error: {str(e)}")
                    
                time.sleep(0.1)  # Small delay to prevent excessive CPU usage
            
            if not self.capture_result:
                self.capture_result = {
                    'success': False,
                    'template': None,
                    'message': 'Capture timeout or failed'
                }
                
            self.is_capturing = False
            
        except Exception as e:
            self.capture_result = {
                'success': False,
                'template': None,
                'message': f'Capture error: {str(e)}'
            }
            self.is_capturing = False
    
    def _process_sample(self, sample):
        """Process fingerprint sample to create template"""
        try:
            # Create feature extractor
            extractor = DPFPFeatureExtractor()
            
            # Extract features from sample
            features = extractor.extract_features(sample)
            
            if not features:
                return None
                
            # Create enrollment object if not exists
            if not self.enrollment:
                self.enrollment = DPFPEnrollment()
            
            # Add features to enrollment
            self.enrollment.add_features(features)
            
            # Check if we have enough features for template creation
            if self.enrollment.is_ready():
                template = self.enrollment.create_template()
                return template.serialize()
            
            return None
            
        except Exception as e:
            print(f"Error processing sample: {str(e)}")
            return None
    
    def stop_capture(self):
        """Stop fingerprint capture"""
        self.is_capturing = False
    
    def get_capture_result(self):
        """Get the result of the last capture operation"""
        return self.capture_result
    
    def verify_fingerprint(self, stored_template, captured_template):
        """Verify captured fingerprint against stored template"""
        try:
            # Create verifier
            verifier = DPFPVerifier()
            
            # Deserialize templates
            stored = DPFPTemplate()
            stored.deserialize(stored_template)
            
            captured = DPFPTemplate()
            captured.deserialize(captured_template)
            
            # Perform verification
            result = verifier.verify(stored, captured)
            
            return result.is_verified(), result.get_false_accept_rate()
            
        except Exception as e:
            print(f"Verification error: {str(e)}")
            return False, 0

# Global scanner instance
scanner = FingerprintScanner()

@app.route('/status', methods=['GET'])
def get_status():
    """Get scanner status"""
    try:
        success, message = scanner.initialize_scanner()
        return jsonify({
            'status': 'ready' if success else 'error',
            'message': message,
            'sdk_available': SDK_AVAILABLE
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e),
            'sdk_available': SDK_AVAILABLE
        })

@app.route('/capture', methods=['GET'])
def capture_fingerprint():
    """Capture a fingerprint"""
    try:
        # Start capture
        success, message = scanner.start_capture()
        
        if not success:
            return jsonify({
                'success': False,
                'message': message,
                'template': None
            })
        
        # Wait for capture to complete (with timeout)
        timeout = 35  # 35 seconds total timeout
        start_time = time.time()
        
        while scanner.is_capturing and (time.time() - start_time) < timeout:
            time.sleep(0.5)
        
        # Get result
        result = scanner.get_capture_result()
        
        if result:
            return jsonify(result)
        else:
            return jsonify({
                'success': False,
                'message': 'Capture timeout',
                'template': None
            })
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Capture error: {str(e)}',
            'template': None
        })

@app.route('/verify', methods=['POST'])
def verify_fingerprint():
    """Verify a fingerprint against stored template"""
    try:
        data = request.get_json()
        
        if not data or 'stored_template' not in data or 'captured_template' not in data:
            return jsonify({
                'success': False,
                'message': 'Missing template data',
                'verified': False,
                'score': 0
            })
        
        # Decode base64 templates
        stored_template = base64.b64decode(data['stored_template'])
        captured_template = base64.b64decode(data['captured_template'])
        
        # Perform verification
        verified, score = scanner.verify_fingerprint(stored_template, captured_template)
        
        return jsonify({
            'success': True,
            'verified': verified,
            'score': score,
            'message': 'Verification completed'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Verification error: {str(e)}',
            'verified': False,
            'score': 0
        })

@app.route('/stop', methods=['POST'])
def stop_capture():
    """Stop ongoing capture"""
    try:
        scanner.stop_capture()
        return jsonify({
            'success': True,
            'message': 'Capture stopped'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error stopping capture: {str(e)}'
        })

# Alternative implementation without SDK (for testing)
class MockFingerprintScanner:
    """Mock scanner for testing when SDK is not available"""
    
    def capture_fingerprint(self):
        """Simulate fingerprint capture"""
        import random
        import time
        
        # Simulate capture delay
        time.sleep(2)
        
        # Generate mock template data
        mock_template = b'mock_fingerprint_template_' + str(random.randint(1000, 9999)).encode()
        
        return {
            'success': True,
            'template': base64.b64encode(mock_template).decode('utf-8'),
            'message': 'Mock fingerprint captured successfully'
        }

# Mock endpoints for testing
@app.route('/mock/capture', methods=['GET'])
def mock_capture():
    """Mock capture endpoint for testing"""
    mock_scanner = MockFingerprintScanner()
    result = mock_scanner.capture_fingerprint()
    return jsonify(result)

@app.route('/test', methods=['GET'])
def test_endpoint():
    """Test endpoint"""
    return jsonify({
        'status': 'Flask service is running',
        'sdk_available': SDK_AVAILABLE,
        'endpoints': [
            '/status - Get scanner status',
            '/capture - Capture fingerprint',
            '/verify - Verify fingerprint',
            '/stop - Stop capture',
            '/mock/capture - Mock capture for testing'
        ]
    })

if __name__ == '__main__':
    print("Starting Fingerprint Service...")
    print(f"SDK Available: {SDK_AVAILABLE}")
    
    # Initialize scanner on startup
    if SDK_AVAILABLE:
        success, message = scanner.initialize_scanner()
        print(f"Scanner initialization: {'Success' if success else 'Failed'} - {message}")
    
    # Run the Flask app
    app.run(host='127.0.0.1', port=5000, debug=True)