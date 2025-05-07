# Django standard imports
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseRedirect
from django.db.models import Q, Sum, Count
from django.utils import timezone
from datetime import datetime, timedelta, date
from decimal import Decimal
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
import stripe
# At the top of your views.py file
from itertools import groupby
from operator import itemgetter
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import MessPaymentRequest

from itertools import groupby
from operator import itemgetter

# ReportLab imports for document generation and styling
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import TableStyle
from reportlab.lib import colors

# Django imports for pagination
from django.core.paginator import EmptyPage

# CSV functionality import
import csv


from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from .models import Room, Hostel, RoomType
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils import timezone
from django.db.models import Count, Q
from .models import ShowcaseNotice, StudentShowcaseNotice  # Corrected import
from hostel.models import Student
from .forms import ShowcaseNoticeForm  # Assuming you have a form for ShowcaseNotice
from django.http import HttpResponse

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Hostel  # Ensure you have the correct import for Hostel

# views.py
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Hostel, RoomType  # Import necessary models

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Hostel, RoomType  # Import Hostel and RoomType models

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Hostel, RoomType  # Import Hostel and RoomType models

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Hostel

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Sum
from .models import Room, RoomType, Hostel, Student
from decimal import Decimal
from .models import RoomType, Hostel, Room  # Import RoomType and other models
from django.core.exceptions import ValidationError  # Import ValidationError

from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import Student, StripePayment, Payment
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import NoticeBoard

# Models
from .models import MessMenu, MessAttendance, MessBill, MessPayment, MessPaymentRequest, MessMembership, ShowcaseNotice, Student, Admin, VisitorRequest, Profile, Visitor, Room, Hostel, Fingerprint, MessRequest

# Forms
from .forms import ShowcaseNoticeForm, MessMembershipForm

# Image processing
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

from .forms import *
from .forms import  MessMembershipForm
from django.db import IntegrityError
from .models import Complaint, Payment

# Define PAYMENT_STATUS_CHOICES if not already defined
PAYMENT_STATUS_CHOICES = [
    ('NOT_PAID', 'Not Paid'),
    ('PARTIALLY_PAID', 'Partially Paid'),
    ('FULLY_PAID', 'Fully Paid'),
]

# ===========================
# Custom User Creation Form
# ===========================

class CustomUserCreationForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    # Student fields
    registration_number = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control student-field', 'placeholder': 'Registration Number'}))
    department = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}))
    contact_info = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}))
    father_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Father\'s Name'}))
    address = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address', 'rows': 3}))
    profile_picture = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

    def clean_registration_number(self):
        registration_number = self.cleaned_data.get('registration_number')
        registration_type = self.data.get('registration_type')
        
        # Only validate registration number if registering as a student
        if registration_type == 'user' and registration_number:
            if Student.objects.filter(Registration_Number=registration_number).exists():
                raise forms.ValidationError("This Registration Number already exists!")
        return registration_number

# ===========================
# User Login Function
# User Registration Function
# User Logout Function
# ===========================

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        login_type = request.POST.get('login_type', 'user')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Check if user is attempting to access admin panel
            if login_type == 'admin':
                try:
                    admin = Admin.objects.get(Name=username)
                    login(request, user)
                    return redirect('dashboard')
                except Admin.DoesNotExist:
                    messages.error(request, "Access Denied. Please login as a student instead.")
                    return render(request, 'user_auth/login.html')
            else:
                # Check if user is a student trying to access student panel
                try:
                    student = Student.objects.get(user=user)
                    login(request, user)
                    return redirect('student_dashboard')
                except Student.DoesNotExist:
                    messages.error(request, "Access Denied. Please login as an admin instead.")
                    return render(request, 'user_auth/login.html')
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'user_auth/login.html')

def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        registration_type = request.POST.get('registration_type', 'user')
        
        # If registering as admin, only validate basic fields
        if registration_type == 'admin':
            # Filter validation to only check basic fields
            form.fields['registration_number'].required = False
            form.fields['department'].required = False
            form.fields['contact_info'].required = False
            form.fields['father_name'].required = False
            form.fields['address'].required = False
        else:
            # Make student fields required when registering as student
            form.fields['registration_number'].required = True
            
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            # Password confirmation check
            if password != confirm_password:
                messages.error(request, "Passwords do not match.")
                return render(request, 'user_auth/register.html', {'form': form})

            try:
                # Create the user object
                user = User.objects.create_user(username=username, email=email, password=password)
                user.first_name = name.split()[0]  # Extract first name
                if len(name.split()) > 1:
                    user.last_name = ' '.join(name.split()[1:])  # Extract last name(s) if available
                user.save()

                # Based on registration type, create appropriate profile
                if registration_type == 'admin':
                    Admin.objects.create(
                        Name=name,
                        Email=email,
                        Password=password,  # Note: In production, use more secure password storage
                        Admin_Role='Staff'
                    )
                    messages.success(request, "Admin registration successful. You can now log in.")
                else:
                    # Create student with the correct field names
                    names = name.split()
                    first_name = names[0]
                    last_name = ' '.join(names[1:]) if len(names) > 1 else ""
                    
                    # Get data from form
                    registration_number = form.cleaned_data['registration_number']
                    department = form.cleaned_data['department']
                    contact_info = form.cleaned_data['contact_info']
                    father_name = form.cleaned_data['father_name']
                    address = form.cleaned_data['address']
                    profile_picture = form.cleaned_data['profile_picture']

                    # Create student object
                    student = Student.objects.create(
                        user=user,
                        F_Name=first_name,
                        L_Name=last_name,
                        Registration_Number=registration_number,
                        Department=department,
                        Contact_Info=contact_info,
                        FatherName=father_name,
                        Address=address,
                        fee_status="Unpaid",  # Default fee status
                        profile_picture=profile_picture,  # Save profile picture
                    )
                    
                    student.save()  # Save the student
                    
                    messages.success(request, "Student registration successful. You can now log in.")

                return redirect('login')

            except IntegrityError:
                messages.error(request, "Username already exists. Please choose a different one.")
            except Exception as e:
                messages.error(request, f"Registration failed: {str(e)}")
        else:
            # Display form errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'user_auth/register.html', context)

def user_logout(request):
    logout(request)
    return redirect('login')


# ===========================
# Dashboard View for Admin
# Student Dashboard View Function
# ===========================
@login_required
def dashboard(request):
    # Get unread counts  
    unread_complaints = Complaint.objects.filter(is_read=False).count()
    
    # Change this line to count PENDING requests that are also unread
    pending_visitor_requests = VisitorRequest.objects.filter(status='PENDING', is_read=False).count()
    
    # Add unread mess requests
    unread_mess_requests = MessRequest.objects.filter(is_read=False).count()  # Assuming `is_read` tracks whether a request is read
    
    # Rest of your dashboard function remains the same
    total_students = Student.objects.count()
    students_with_paid_payment = Payment.objects.filter(Fee_Status='PAID').values('Student_ID').distinct().count()
    
    # Room statistics: Ensure rooms are assigned
    rooms = Room.objects.all()  # This should always assign rooms
    available_rooms = 0
    if rooms:
        available_rooms = sum(1 for room in rooms if room.is_available)  # Now you can use `is_available` directly
    
    # Complaint statistics
    total_complaints = Complaint.objects.count()
    recent_complaints = Complaint.objects.order_by('-Created_At')[:5]
    
    # Active notices query
    current_date = timezone.now()
    active_notices_query = NoticeBoard.objects.filter(
        Is_Active=True
    ).filter(
        Q(Expiry_Date__isnull=True) | Q(Expiry_Date__gte=current_date)
    )
    
    # Get the count of active notices
    active_notices_count = active_notices_query.count()
    
    # Get the actual notices for display (limited to 5)
    active_notices = active_notices_query.order_by('-Created_At')[:5]
    
    # Get today's mess menu
    today_weekday = current_date.strftime('%a').upper()[:3]  # Get the current day of the week in shortened uppercase form
    today_menu = {}
    
    # Fetch today's menu items for all meal times
    meal_times = ['BF', 'LN', 'ET', 'DN']
    for meal_time in meal_times:
        try:
            menu_item = MessMenu.objects.filter(day=today_weekday, meal_time=meal_time).first()
            today_menu[meal_time] = menu_item
        except:
            today_menu[meal_time] = None
    
    # Get the meal names for display
    meal_names = dict(MessMenu.MEAL_CHOICES)
    
    context = {
        'total_students': total_students,
        'students_with_paid_payment': students_with_paid_payment,
        'available_rooms': available_rooms,
        'total_complaints': total_complaints,
        'unread_complaints': unread_complaints,
        'complaints': recent_complaints,
        'notices': active_notices,
        'active_notices': active_notices_count,
        'pending_visitor_requests': pending_visitor_requests,
        'unread_mess_requests': unread_mess_requests,
        'today_menu': today_menu,
        'meal_names': meal_names,
    }
    
    return render(request, 'dashboard.html', context)

@login_required
def student_dashboard(request):
    # Ensure the logged-in user is a student
    if not hasattr(request.user, 'student'):
        messages.error(request, "Access denied. Student account required.")
        return redirect('login')
    
    student = request.user.student
    
    # Get recent notices for the student
    recent_notices = NoticeBoard.objects.filter(
        Is_Active=True
    ).order_by('-Created_At')[:5]
    
    # Fetch the student's associated Showcase Notices
    student_showcase_notices = StudentShowcaseNotice.objects.filter(student=student).order_by('-notice__created_date')
    
    # Count the unread showcase notices for the student
    unread_showcase_notices_count = StudentShowcaseNotice.objects.filter(student=student, read=False).count()
    
    # Get room and hostel details
    room = student.Room_ID
    hostel = student.Hostel_ID
    
    # Calculate fee status - With correct attribute names
    total_fee = getattr(student, 'total_fee', None) or \
                getattr(student, 'Total_Fee', None) or \
                getattr(student, 'fee_amount', None) or \
                0
    paid_amount = getattr(student, 'total_paid_amount', None) or \
                  getattr(student, 'paid_amount', None) or \
                  getattr(student, 'Paid_Amount', None) or \
                  0
                
    # Use the calculate_remaining_fee method if it exists, otherwise calculate manually
    if hasattr(student, 'calculate_remaining_fee') and callable(getattr(student, 'calculate_remaining_fee')):
        remaining_fee = student.calculate_remaining_fee()
    else:
        remaining_fee = float(total_fee) - float(paid_amount)
    
    # Calculate the percentage of fee paid
    fee_percentage = (float(paid_amount) / float(total_fee) * 100) if float(total_fee) > 0 else 0
    
    # Mess fee data
    # Get all attendance records for the student for the current month
    today = timezone.now().date()
    first_day = today.replace(day=1)
    last_day = today.replace(day=1, month=today.month + 1) - timezone.timedelta(days=1)
    
    attendance_records = MessAttendance.objects.filter(
        student=student,
        date__range=[first_day, last_day],
        is_present=True
    )
    
    # Calculate total mess cost for the month
    total_mess_cost = sum(record.price_charged for record in attendance_records)
    
    # Get approved payment records for the month
    approved_payments = MessPaymentRequest.objects.filter(
        student=student,
        request_date__range=[first_day, last_day],
        status='APPROVED'
    )
    
    # Calculate total paid for the month
    total_paid = sum(payment.amount for payment in approved_payments)
    
    # Calculate remaining mess dues for the month
    current_mess_dues = total_mess_cost - total_paid if total_paid < total_mess_cost else 0
    
    # Get today's mess menu
    current_date = timezone.now()
    today_weekday = current_date.strftime('%a').upper()[:3]  # Get the current day of the week in shortened uppercase form
    today_menu = {}
    
    # Fetch today's menu items for all meal times
    meal_times = ['BF', 'LN', 'ET', 'DN']
    for meal_time in meal_times:
        try:
            menu_item = MessMenu.objects.filter(day=today_weekday, meal_time=meal_time).first()
            today_menu[meal_time] = menu_item
        except:
            today_menu[meal_time] = None
    
    # Prepare context data for the dashboard
    context = {
        'student': student,
        'recent_notices': recent_notices,
        'student_showcase_notices': student_showcase_notices,
        'unread_showcase_notices_count': unread_showcase_notices_count,
        'room': room,
        'hostel': hostel,
        'fee_status': {
            'total': total_fee,
            'paid': paid_amount,
            'remaining': remaining_fee,
            'percentage': round(fee_percentage, 2)
        },
        'mess_fee_status': {
            'total_cost': total_mess_cost,
            'total_paid': total_paid,
            'remaining_due': current_mess_dues,
            'percentage_paid': (total_paid / total_mess_cost * 100) if total_mess_cost > 0 else 0
        },
        'today_menu': today_menu
    }
    
    # Render the student dashboard page
    return render(request, 'student_dashboard.html', context)

# ===========================
# Student Profile View Function
# ===========================

@login_required
def std_profile(request):
    # Get the logged-in student's profile information
    student = Student.objects.get(user=request.user)
    
    # Check if the student has a hostel assigned
    if student.Hostel_ID is None:
        messages.error(request, "This student is not assigned to any hostel.")
        return redirect('assign_hostel')  # Replace 'assign_hostel' with the actual URL name for assigning a hostel
    
    # Calculate remaining fee
    remaining_fee = student.calculate_remaining_fee()
    
    # Map fee status to display name
    fee_status_display = dict(Student.PAYMENT_STATUS_CHOICES).get(student.fee_status, student.fee_status)
    
    # Determine color for fee status
    fee_status_color = 'green' if student.fee_status == 'FULLY_PAID' else 'red' if student.fee_status == 'NOT_PAID' else 'orange'
    
    # Mess fee data - using the same approach as in student_dashboard
    # Get all attendance records for the student for the current month
    today = timezone.now().date()
    first_day = today.replace(day=1)
    last_day = today.replace(day=1, month=today.month + 1) - timezone.timedelta(days=1)
    
    attendance_records = MessAttendance.objects.filter(
        student=student,
        date__range=[first_day, last_day],
        is_present=True
    )
    
    # Calculate total mess cost for the month
    total_mess_cost = sum(record.price_charged for record in attendance_records)
    
    # Get approved payment records for the month
    approved_payments = MessPaymentRequest.objects.filter(
        student=student,
        request_date__range=[first_day, last_day],
        status='APPROVED'
    )
    
    # Calculate total paid for the month
    total_paid = sum(payment.amount for payment in approved_payments)
    
    # Calculate remaining mess dues for the month
    current_mess_dues = total_mess_cost - total_paid if total_paid < total_mess_cost else 0
    
    # Prepare mess fee status
    mess_fee_status = {
        'total_cost': total_mess_cost,
        'total_paid': total_paid,
        'remaining_due': current_mess_dues,
        'percentage_paid': (total_paid / total_mess_cost * 100) if total_mess_cost > 0 else 0
    }
    
    # Prepare context data for rendering the profile page
    context = {
        'student': student,
        'personal_info': {
            'Father\'s Name': student.FatherName,
            'Email': student.user.email,
            'Contact': student.Contact_Info,
            'Address': student.Address,
            'Department': student.Department
        },
        'hostel_info': {
            'Hostel Name': student.Hostel_ID.Hostel_Name if student.Hostel_ID else "Not Assigned",
            'Room Number': student.Room_ID.Room_No if student.Room_ID else "Not Assigned",
            'Room Type': student.Room_ID.Room_Type if student.Room_ID else "Not Assigned",
            'Floor Number': student.Room_ID.Floor_No if student.Room_ID else "Not Assigned"
        },
        'fee_status_info': [
            ('Fee Status', fee_status_display, fee_status_color),
            ('Total Fee', f'Rs {student.total_fee}', 'gray'),
            ('Paid Amount', f'Rs {student.total_paid_amount}', 'gray'),
            ('Remaining Fee', f'Rs {remaining_fee}', 'red')
        ],
        'mess_fee_status': mess_fee_status
    }
    
    
    
    # Render the student profile page
    return render(request, 'user_auth/std_profile.html', context)


# ===========================
# List All Hostels
# Add a Hostel and its Rooms
# Add a Hostel and its Rooms
# Edit Hostel Information
# Delete Hostel
# ===========================


def assign_hostel(request):
    # Logic to assign hostel or show a form for the student to select a hostel
    return render(request, 'assign_hostel.html')
def list_hostels(request):
    # Fetch all hostel objects from the database and order by Hostel_ID
    hostels = Hostel.objects.all().order_by('Hostel_ID')

    # Pagination logic: Display 10 hostels per page
    paginator = Paginator(hostels, 10)
    page_number = request.GET.get('page')  # Get the page number from the URL
    page_obj = paginator.get_page(page_number)

    # Get room types and their prices
    room_types = RoomType.objects.all()
    room_type_prices = {}
    for rt in room_types:
        room_type_prices[rt.type_name] = rt.price
    
    # Add room prices for each hostel to the context
    for hostel in page_obj:
        # Default prices if not found in database
        hostel.room_prices = {
            'One_Seater': room_type_prices.get('One Seater', 12000),
            'Two_Seater': room_type_prices.get('Two Seater', 10000),
            'Three_Seater': room_type_prices.get('Three Seater', 9000),
            'Four_Seater': room_type_prices.get('Four Seater', 8000),
            'Five_Seater': room_type_prices.get('Five Seater', 7500),
            'Six_Seater': room_type_prices.get('Six Seater', 7000),
            'Seven_Seater': room_type_prices.get('Seven Seater', 6500),
            'Eight_Seater': room_type_prices.get('Eight Seater', 6000),
            'Nine_Seater': room_type_prices.get('Nine Seater', 5500),
            'Ten_Seater': room_type_prices.get('Ten Seater', 5000)
        }

    # Prepare context data for rendering the template
    context = {
        'page_obj': page_obj,  # Paginated hostels
    }
    
    return render(request, 'hostel_management/list_hostels.html', context)
def view_hostel_rooms(request, hostel_id):
    # Fetch the hostel
    hostel = get_object_or_404(Hostel, Hostel_ID=hostel_id)
    
    # Check if we need to auto-generate rooms (no rooms exist for this hostel)
    rooms_count = Room.objects.filter(Hostel_ID=hostel).count()

    # Add this mapping to convert word numbers to integers
    word_to_number = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4, 
        'Five': 5,
        'Six': 6,
        'Seven': 7,
        'Eight': 8,
        'Nine': 9,
        'Ten': 10
    }
    
    # If no rooms exist and user requested to create them
    if rooms_count == 0 and request.GET.get('generate_rooms') == 'true':
        # Get room types from database
        room_types = RoomType.objects.all()
        room_type_dict = {rt.type_name: rt for rt in room_types}
        
        # Map hostel field names to Room_Type values
        field_to_room_type = {
            'One_Seater_Rooms': 'One Seater',
            'Two_Seater_Rooms': 'Two Seater',
            'Three_Seater_Rooms': 'Three Seater',
            'Four_Seater_Rooms': 'Four Seater',
            'Five_Seater_Rooms': 'Five Seater',
            'Six_Seater_Rooms': 'Six Seater',
            'Seven_Seater_Rooms': 'Seven Seater',
            'Eight_Seater_Rooms': 'Eight Seater',
            'Nine_Seater_Rooms': 'Nine Seater',
            'Ten_Seater_Rooms': 'Ten Seater',
        }
        
        # Create list of rooms to create in bulk
        floor_mappings = {
            'One Seater': 1, 
            'Two Seater': 1,
            'Three Seater': 2,
            'Four Seater': 2,
            'Five Seater': 3,
            'Six Seater': 3,
            'Seven Seater': 4,
            'Eight Seater': 4,
            'Nine Seater': 5,
            'Ten Seater': 5,
        }
        
        # Initialize room number counter - starting from 1
        room_counter = 1
        
        # Create room objects for each type
        rooms_to_create = []
        for field, room_type in field_to_room_type.items():
            num_rooms = getattr(hostel, field)
            
            # Skip if no rooms of this type
            if num_rooms == 0:
                continue
                
            # Get appropriate room type object
            room_type_obj = room_type_dict.get(room_type)
            floor = floor_mappings.get(room_type, None)  # Keep track of floor for location info
            
            if floor is None:
                continue  # Skip room creation if no valid floor mapping found
            
            # Get capacity number from the room type string
            capacity_word = room_type.split()[0]  # e.g., "One" from "One Seater"
            capacity = word_to_number.get(capacity_word, 1)  # Default to 1 if not found
            
            # Create each room of this type
            for i in range(num_rooms):
                # Generate sequential room number (1, 2, 3...)
                base_room_no = str(room_counter)
                
                # Find the next available room number by incrementing until a unique one is found
                while Room.objects.filter(Room_No=base_room_no).exists():
                    room_counter += 1
                    base_room_no = str(room_counter)
                
                # Create room object with numeric capacity
                new_room = Room(
                    Room_Type=room_type,
                    Capacity=capacity,
                    Location=f"Floor {floor}",
                    Room_No=base_room_no,
                    Floor_No=floor,
                    Students_Alloted=0,
                    Hostel_ID=hostel,
                    room_type_info=room_type_obj
                )
                rooms_to_create.append(new_room)
                room_counter += 1
        
        # Instead of bulk_create (which would fail if any room has a duplicate number),
        # create rooms one by one with error handling
        created_rooms = 0
        for room in rooms_to_create:
            try:
                room.save()
                created_rooms += 1
            except IntegrityError:
                # If we encounter a duplicate room number, we'll skip it
                continue
                
        if created_rooms > 0:
            messages.success(request, f"{created_rooms} rooms created successfully for {hostel.Hostel_Name}!")
        else:
            messages.warning(request, f"No rooms could be created. Room numbers may already exist.")
        
        # Redirect to remove the generate_rooms parameter from URL
        return redirect('view_hostel_rooms', hostel_id=hostel_id)
    
    # Get search query and selected room type from request
    search_query = request.GET.get('search', '')
    selected_room_type = request.GET.get('room_type', '')
    
    # Get all rooms for this hostel
    rooms = Room.objects.filter(Hostel_ID=hostel).prefetch_related('students')
    
    # Apply room type filter if selected
    if selected_room_type:
        rooms = rooms.filter(Room_Type__icontains=selected_room_type)
    
    # Apply search if provided
    if search_query:
        rooms = rooms.filter(
            Q(Room_No__icontains=search_query) |
            Q(Room_Type__icontains=search_query) |
            Q(Location__icontains=search_query)
        )
    
    # Calculate room statistics
    for room in rooms:
        # Get all students for this room
        room.allocated_students = room.students.all().values(
            'Student_ID',
            'F_Name',
            'L_Name',
            'Department',
            'fee_status'
        )
        
        # Update Students_Alloted field if needed
        students_count = room.students.count()
        if room.Students_Alloted != students_count:
            room.Students_Alloted = students_count
            room.save()
        
        # We don't need to set remaining_capacity manually since it's a property
        # that will be calculated automatically when accessed in the template

    # Calculate room type distribution
    room_counts = []
    room_types = {}
    
    for room in rooms:
        if room.Room_Type in room_types:
            room_types[room.Room_Type] += 1
        else:
            room_types[room.Room_Type] = 1
    
    # Calculate percentages for chart
    total_rooms = rooms.count()  # Use actual count instead of hostel.No_Of_Rooms
    if total_rooms > 0:
        for room_type, count in room_types.items():
            percentage = (count / total_rooms) * 100
            room_counts.append({
                'type': room_type,
                'count': count,
                'percentage': percentage
            })
    
    # Sort room counts by room type
    room_counts.sort(key=lambda x: x['type'])
    
    # Calculate overall capacity of the hostel based on actual rooms
    total_capacity = sum(room.Capacity for room in rooms)
    hostel.capacity = total_capacity
    
    # Update No_Of_Students based on actual student allocations if needed
    actual_students_count = sum(room.students.count() for room in rooms)
    
    # Calculate occupancy rate based on actual data
    if total_capacity > 0:
        hostel.occupancy_rate = min(100, (actual_students_count / total_capacity) * 100)
    else:
        hostel.occupancy_rate = 0
    
    context = {
        'hostel': hostel,
        'rooms': rooms,
        'search_query': search_query,
        'room_counts': room_counts,
        'has_no_rooms': rooms_count == 0,
        'selected_room_type': selected_room_type,
        'actual_students_count': actual_students_count,
    }
    
    return render(request, 'hostel_management/view_hostel_rooms.html', context)
def add_hostel(request):
    if request.method == "POST":
        # Retrieve data from the POST request
        hostel_name = request.POST.get("hostel_name")
        no_of_rooms = int(request.POST.get("no_of_rooms"))
        no_of_students = int(request.POST.get("no_of_students"))
        
        # Get all room type counts
        one_seater = int(request.POST.get("one_seater", 0))
        two_seater = int(request.POST.get("two_seater", 0))
        three_seater = int(request.POST.get("three_seater", 0))
        four_seater = int(request.POST.get("four_seater", 0))
        five_seater = int(request.POST.get("five_seater", 0))
        six_seater = int(request.POST.get("six_seater", 0))
        seven_seater = int(request.POST.get("seven_seater", 0))
        eight_seater = int(request.POST.get("eight_seater", 0))
        nine_seater = int(request.POST.get("nine_seater", 0))
        ten_seater = int(request.POST.get("ten_seater", 0))
        
        # Get all room type prices
        one_seater_price = int(request.POST.get("one_seater_price", 12000))
        two_seater_price = int(request.POST.get("two_seater_price", 10000))
        three_seater_price = int(request.POST.get("three_seater_price", 9000))
        four_seater_price = int(request.POST.get("four_seater_price", 8000))
        five_seater_price = int(request.POST.get("five_seater_price", 7500))
        six_seater_price = int(request.POST.get("six_seater_price", 7000))
        seven_seater_price = int(request.POST.get("seven_seater_price", 6500))
        eight_seater_price = int(request.POST.get("eight_seater_price", 6000))
        nine_seater_price = int(request.POST.get("nine_seater_price", 5500))
        ten_seater_price = int(request.POST.get("ten_seater_price", 5000))
        
        # Validate if the hostel name is unique
        if Hostel.objects.filter(Hostel_Name=hostel_name).exists():
            messages.error(request, "Hostel name already exists!")
            return redirect("add_hostel")
        
        # Validate minimum students requirement
        if no_of_students < 300:
            messages.error(request, "The hostel must have capacity for at least 300 students.")
            return redirect("add_hostel")
        
        # Create a new hostel instance
        try:
            hostel = Hostel.objects.create(
                Hostel_Name=hostel_name,
                No_Of_Rooms=no_of_rooms,
                No_Of_Students=no_of_students,
                One_Seater_Rooms=one_seater,
                Two_Seater_Rooms=two_seater, 
                Three_Seater_Rooms=three_seater,
                Four_Seater_Rooms=four_seater,
                Five_Seater_Rooms=five_seater,
                Six_Seater_Rooms=six_seater,
                Seven_Seater_Rooms=seven_seater,
                Eight_Seater_Rooms=eight_seater,
                Nine_Seater_Rooms=nine_seater,
                Ten_Seater_Rooms=ten_seater
            )
        except ValidationError as e:
            messages.error(request, str(e))
            return redirect("add_hostel")
        
        # Get all room types from the database
        room_types_from_db = RoomType.objects.all()
        room_type_mapping = {rt.type_name: rt for rt in room_types_from_db}
        
        # Create or update room types with prices
        room_types_with_prices = [
            {"name": "One Seater", "count": one_seater, "price": one_seater_price},
            {"name": "Two Seater", "count": two_seater, "price": two_seater_price},
            {"name": "Three Seater", "count": three_seater, "price": three_seater_price},
            {"name": "Four Seater", "count": four_seater, "price": four_seater_price},
            {"name": "Five Seater", "count": five_seater, "price": five_seater_price},
            {"name": "Six Seater", "count": six_seater, "price": six_seater_price},
            {"name": "Seven Seater", "count": seven_seater, "price": seven_seater_price},
            {"name": "Eight Seater", "count": eight_seater, "price": eight_seater_price},
            {"name": "Nine Seater", "count": nine_seater, "price": nine_seater_price},
            {"name": "Ten Seater", "count": ten_seater, "price": ten_seater_price}
        ]
        
        # Update room type prices in database
        for room_type_data in room_types_with_prices:
            room_type_name = room_type_data["name"]
            room_type_price = room_type_data["price"]
            
            # Get or create the room type
            room_type_obj = room_type_mapping.get(room_type_name)
            if room_type_obj:
                # Update the price
                room_type_obj.price = room_type_price
                room_type_obj.save()
        
        # Start room numbers from 101 (first floor, first room)
        room_counter = 101
        created_rooms = 0
        
        # Loop through each room type and create corresponding rooms
        for room_type_data in room_types_with_prices:
            room_type_name = room_type_data["name"]
            count = room_type_data["count"]
            price = room_type_data["price"]
            
            if count > 0:
                room_type_obj = room_type_mapping.get(room_type_name)
                
                # Skip if room type not found in database
                if not room_type_obj:
                    continue
                
                for i in range(count):
                    # Calculate floor based on rooms (every 20 rooms is a new floor)
                    floor_no = (created_rooms // 20) + 1
                    
                    # Assign room number: floor number * 100 + room sequence on floor
                    room_no = f"{floor_no}{(created_rooms % 20) + 1:02d}"
                    
                    # Ensure the room number is unique
                    while Room.objects.filter(Room_No=room_no).exists():
                        created_rooms += 1
                        floor_no = (created_rooms // 20) + 1
                        room_no = f"{floor_no}{(created_rooms % 20) + 1:02d}"
                    
                    # Create the room and associate it with the hostel
                    Room.objects.create(
                        Room_Type=room_type_name,
                        Capacity=room_type_obj.capacity,
                        Location=f"{hostel.Hostel_Name}, Floor {floor_no}",
                        Room_No=room_no,
                        Floor_No=floor_no,
                        Students_Alloted=0,
                        Hostel_ID=hostel,
                        room_type_info=room_type_obj,
                        Price=price  # Add the price to the room
                    )
                    
                    created_rooms += 1
        
        # Display success message and redirect to the list of hostels
        messages.success(request, f"Hostel '{hostel_name}' with {created_rooms} rooms created successfully!")
        return redirect("list_hostels")
    
    # If GET request, fetch all room types to populate the form
    room_types = RoomType.objects.all()
    context = {'room_types': room_types}
    
    # Render the hostel creation form
    return render(request, 'hostel_management/add_hostel.html', context)

def edit_hostel(request, hostel_id):
    # Retrieve the hostel object or return 404 if not found
    hostel = get_object_or_404(Hostel, Hostel_ID=hostel_id)
    if request.method == 'POST':
        # Update hostel fields based on the POST data
        hostel.Hostel_Name = request.POST.get('hostel_name')
        hostel.No_Of_Rooms = request.POST.get('no_of_rooms')
        hostel.No_Of_Students = request.POST.get('no_of_students')
        hostel.Single_Seater_Rooms = request.POST.get('single_seater')
        hostel.Two_Seater_Rooms = request.POST.get('two_seater')
        hostel.Three_Seater_Rooms = request.POST.get('three_seater')
        hostel.Six_Seater_Rooms = request.POST.get('six_seater')
        
        # Save the updated hostel information
        hostel.save()
        messages.success(request, "Hostel updated successfully!")
        return redirect('list_hostels')

    # Render the edit hostel form with the current hostel data
    return render(request, 'hostel_management/edit_hostel.html', {'hostel': hostel})

def delete_hostel(request, hostel_id):
    # Retrieve the hostel object or return 404 if not found
    hostel = get_object_or_404(Hostel, Hostel_ID=hostel_id)
    
    # Delete the hostel record from the database
    hostel.delete()
    messages.success(request, "Hostel deleted successfully!")
    return redirect('list_hostels')


# ===========================
# Add Room Function
# List Rooms Function
# Edit Room Function
# Delete Room Function
# ===========================

@login_required
def add_room(request):
    # Get hostel_id from query parameters if available
    hostel_id = request.GET.get('hostel', None)
    hostel = None
    
    if hostel_id:
        hostel = get_object_or_404(Hostel, Hostel_ID=hostel_id)
    
    if request.method == 'POST':
        # Retrieve values from the form
        room_no = request.POST.get('room_no')
        room_type = request.POST.get('room_type')
        floor_no = request.POST.get('floor_no')
        location = request.POST.get('location')
        hostel_id = request.POST.get('hostel_id')
        
        # Convert numeric fields to integers
        try:
            floor_no = int(floor_no)
        except ValueError:
            messages.error(request, "Invalid input. Please enter a valid integer for floor number.")
            return redirect('add_room')
        
        # Map room types to their capacities
        capacity_map = {
            "One Seater": 1, 
            "Two Seater": 2, 
            "Three Seater": 3, 
            "Four Seater": 4,
            "Five Seater": 5,
            "Six Seater": 6,
            "Seven Seater": 7,
            "Eight Seater": 8,
            "Nine Seater": 9,
            "Ten Seater": 10,
        }
        
        capacity = capacity_map.get(room_type)
        if not capacity:
            messages.error(request, "Invalid room type selected.")
            return redirect('add_room')
        
        # Check if the room number already exists in the hostel
        existing_room = Room.objects.filter(Room_No=room_no, Hostel_ID=hostel_id).first()
        if existing_room:
            messages.error(request, f"Room number {room_no} already exists in this hostel.")
            return redirect('add_room')
        
        # Create new room
        room = Room(
            Room_No=room_no,
            Room_Type=room_type,
            Capacity=capacity,
            Floor_No=floor_no,
            Location=location,
            Students_Alloted=0,  # Initially no students
            Hostel_ID_id=hostel_id
        )
        
        # Save the new room
        room.save()
        
        messages.success(request, "Room added successfully!")
        
        # Redirect to hostel rooms if hostel_id is provided, otherwise to room list
        if hostel_id:
            return redirect('view_hostel_rooms', hostel_id=hostel_id)
        else:
            return redirect('list_rooms')
    
    # For GET request, fetch all hostels for dropdown
    hostels = Hostel.objects.all()
    
    context = {
        'hostels': hostels,
        'selected_hostel': hostel
    }
    
    return render(request, 'room_management/add_room.html', context)

def list_rooms(request):
    # Get all rooms with their related students
    rooms = Room.objects.all().prefetch_related('students')
    
    # Get search query from GET parameters
    search_query = request.GET.get('search', '')
    
    if search_query:
        rooms = rooms.filter(
            Q(Room_No__icontains=search_query) |
            Q(Room_Type__icontains=search_query) |
            Q(Location__icontains=search_query)
        )
    
    # Calculate room statistics
    for room in rooms:
        room.allocated_students = room.students.all().values(
            'Student_ID',
            'F_Name',
            'L_Name',
            'Department',
            'fee_status'
        )
        
        # Make sure remaining_capacity is accessible
        # This is only needed if remaining_capacity is not already defined as a property on the Room model
        if not hasattr(room, 'remaining_capacity'):
            # Calculate remaining capacity as total capacity minus number of allocated students
            room.remaining_capacity = room.Capacity - room.allocated_students.count()
    
    context = {
        'rooms': rooms,
        'search_query': search_query,
    }
    
    return render(request, 'room_management/list_rooms.html', context)

@login_required
def edit_room(request, room_id):
    # Fetch the room object or return 404 if not found
    room = get_object_or_404(Room, Room_ID=room_id)
    
    if request.method == 'POST':
        # Retrieve updated values from the form
        room_no = request.POST.get('room_no')
        room_type = request.POST.get('room_type')
        floor_no = request.POST.get('floor_no')
        location = request.POST.get('location')
        students_alloted = request.POST.get('students_alloted', '0')
        
        # Convert numeric fields to integers
        try:
            floor_no = int(floor_no)
            students_alloted = int(students_alloted)
        except ValueError:
            messages.error(request, "Invalid input. Please enter valid integers for floor number and students allocated.")
            return redirect('edit_room', room_id=room_id)
        
        # Map room types to their capacities
        capacity_map = {
            "One Seater": 1, 
            "Two Seater": 2, 
            "Three Seater": 3, 
            "Four Seater": 4,
            "Five Seater": 5,
            "Six Seater": 6,
            "Seven Seater": 7,
            "Eight Seater": 8,
            "Nine Seater": 9,
            "Ten Seater": 10,
        }
        
        capacity = capacity_map.get(room_type)
        if not capacity:
            messages.error(request, "Invalid room type selected.")
            return redirect('edit_room', room_id=room_id)
        
        # Ensure students allocated doesn't exceed room capacity
        if students_alloted > capacity:
            messages.error(request, f"Allocated students ({students_alloted}) cannot exceed room capacity ({capacity}).")
            return redirect('edit_room', room_id=room_id)
        
        # Check if the new room number already exists (except for the current room)
        existing_room = Room.objects.exclude(Room_ID=room_id).filter(Room_No=room_no).first()
        if existing_room:
            messages.error(request, f"Room number {room_no} already exists.")
            return redirect('edit_room', room_id=room_id)
        
        # Update the room details
        room.Room_No = room_no
        room.Room_Type = room_type
        room.Capacity = capacity
        room.Floor_No = floor_no
        room.Location = location
        room.Students_Alloted = students_alloted
        
        # Save the updated room details
        room.save()
        
        messages.success(request, "Room updated successfully!")
        return redirect('list_rooms')

    # For GET request, load the current room details for editing
    context = {
        'room': room,
        'hostel': room.Hostel_ID
    }
    
    return render(request, 'room_management/edit_room.html', context)

def delete_room(request, room_id):
    room = get_object_or_404(Room, Room_ID=room_id)

    if request.method == 'POST':
        # Delete the room if confirmed
        room.delete()
        messages.success(request, "Room deleted successfully!")
        return redirect('list_rooms')

    return render(request, 'delete_room_confirmation.html', {'room': room})


# ===========================#
# Function to compress image (already provided)
# ===========================#
def compress_image(image):
    """
    This function takes an image, compresses it to a maximum size of 200x200 pixels,
    and returns the compressed image as an InMemoryUploadedFile object for further use.
    """
    from PIL import Image
    from io import BytesIO
    from django.core.files.uploadedfile import InMemoryUploadedFile

    img = Image.open(image)
    img = img.convert('RGB')  # Convert image to RGB
    img.thumbnail((200, 200))  # Resize image maintaining aspect ratio
    
    output = BytesIO()
    img.save(output, format='JPEG')  # Save as JPEG
    output.seek(0)  # Move cursor to start
    return InMemoryUploadedFile(output, 'ImageField', image.name, 'image/jpeg', output.getbuffer().nbytes, None)

# ===========================
# Add Student Function
# List Students Function
# View Student Function
# Edit Student Function
# Delete Student Function
# List All Students Function
# Export Students to CSV Function
# Export Students to PDF Function
# Bulk Fee Reminder Function
# ===========================

@login_required
def add_student(request):
    if request.method == "POST":
        email = request.POST.get("email")
        room_id = request.POST.get("room_id")
        hostel_id = request.POST.get("hostel_id")
        registration_number = request.POST.get("registration_number")

        # Check if the username or email already exists
        if User.objects.filter(username=email).exists():
            messages.error(request, "A user with this email already exists.")
            return redirect("add_student")

        # Check if the registration number already exists
        if Student.objects.filter(Registration_Number=registration_number).exists():
            messages.error(request, "A student with this registration number already exists.")
            return redirect("add_student")

        try:
            # Fetch room and hostel details
            room = Room.objects.get(pk=room_id)
            hostel = Hostel.objects.get(pk=hostel_id)
        except (Room.DoesNotExist, Hostel.DoesNotExist):
            messages.error(request, "Invalid room or hostel selection.")
            return redirect("add_student")

        # Check if room has remaining capacity
        if room.remaining_capacity <= 0:
            messages.error(request, "The selected room is full.")
            return redirect("add_student")

        # Create the user
        user = User.objects.create_user(
            username=email,
            email=email,
            password=request.POST.get("password"),
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
        )
        user.save()

        # Process profile picture upload
        profile_picture = request.FILES.get("profile_picture")
        if profile_picture:
            # Optional: Compress the image before saving
            profile_picture = compress_image(profile_picture)

        # Get room price - first check Room.Price, then room_type_info.price
        room_price = 0
        if hasattr(room, 'Price') and room.Price > 0:
            room_price = room.Price
        elif hasattr(room, 'room_type_info') and room.room_type_info and hasattr(room.room_type_info, 'price'):
            room_price = room.room_type_info.price
        
        # If still no price, use default based on room type
        if room_price == 0:
            room_type_prices = {
                "One Seater": 12000,
                "Two Seater": 10000,
                "Three Seater": 9000,
                "Four Seater": 8000,
                "Five Seater": 7500,
                "Six Seater": 7000,
                "Seven Seater": 6500,
                "Eight Seater": 6000,
                "Nine Seater": 5500,
                "Ten Seater": 5000,
                # Add default fallback
                "Default": 5000
            }
            room_price = room_type_prices.get(room.Room_Type, room_type_prices["Default"])

        # Calculate total fee (room price for each semester - 8 semesters total)
        total_fee = room_price * 8  # 4 years, 2 semesters per year

        # Create the student record with room price and total fee
        student = Student.objects.create(
            user=user,
            F_Name=request.POST.get("first_name"),
            L_Name=request.POST.get("last_name"),
            Contact_Info=request.POST.get("contact_info"),
            Address=request.POST.get("address"),
            Department=request.POST.get("department"),
            FatherName=request.POST.get("father_name"),
            fee_status="NOT_PAID",
            Room_ID=room,
            Hostel_ID=hostel,
            Registration_Number=registration_number,
            profile_picture=profile_picture,
            room_price=room_price,  # Store the room price for the student
            total_fee=total_fee     # Store the total fee for all semesters
        )

        # Increment Students_Alloted in the Room
        room.Students_Alloted += 1
        room.save()

        # Create fee records for each semester
        current_year = timezone.now().year
        semesters = []
        for i in range(4):  # 4 years
            semesters.extend([f'Fall-{current_year + i}', f'Spring-{current_year + i + 1}'])
        
        # Create fee records for each semester
        for i, semester in enumerate(semesters, 1):
            Payment.objects.create(
                Student_ID=student,
                Fee_Type=semester,
                Amount_Due=room_price,  # Set the Amount_Due field
                Amount_Paid=0,  # Initially 0
                Receipt_Number=f"{registration_number}-{i}",
                Fee_Status="UNPAID",  # Change from "NOT_PAID" to "UNPAID" to match the model choices
                Payment_Mode="",  # Leave blank instead of "PENDING"
                Installment_Number=i,
                Due_Date=None  # No due date initially
            )
        # Handle initial payment if provided
        initial_fee = request.POST.get("initial_payment", 0)
        if initial_fee and float(initial_fee) > 0:
            # Find the first semester payment record
            first_payment = Payment.objects.filter(Student_ID=student, Installment_Number=1).first()
            if first_payment:
                first_payment.Amount_Paid = float(initial_fee)
                first_payment.Fee_Status = "PAID"
                first_payment.Payment_Mode = "CASH"  # Default or could be from form
                first_payment.Payment_Date = timezone.now()
                first_payment.save()

            # Update student fee status
            if float(initial_fee) >= total_fee:
                student.fee_status = "FULLY_PAID"
            elif float(initial_fee) >= room_price:
                student.fee_status = "PARTIALLY_PAID"
            student.save()

        messages.success(request, f"Student added successfully! Room fee per semester: ₹{room_price}, Total fee: ₹{total_fee}")
        return redirect("list_students")

    # For GET request, load hostels and rooms for selection with prices
    hostels = Hostel.objects.all()
    rooms = Room.objects.all().select_related('room_type_info', 'Hostel_ID')  # Optimize with select_related

    # Create room data for the frontend with prices
    room_data = []
    for room in rooms:
        # Determine the price - use Room.Price if available, otherwise use RoomType.price
        price = 0
        if hasattr(room, 'Price') and room.Price > 0:
            price = room.Price
        elif hasattr(room, 'room_type_info') and room.room_type_info and hasattr(room.room_type_info, 'price'):
            price = room.room_type_info.price
        else:
            # Default prices based on room type
            room_type_prices = {
                "One Seater": 12000,
                "Two Seater": 10000,
                "Three Seater": 9000,
                "Four Seater": 8000,
                "Five Seater": 7500,
                "Six Seater": 7000,
                "Seven Seater": 6500,
                "Eight Seater": 6000,
                "Nine Seater": 5500,
                "Ten Seater": 5000,
                # Add default fallback
                "Default": 5000
            }
            price = room_type_prices.get(room.Room_Type, room_type_prices["Default"])

        # Get room capacity and remaining capacity
        capacity = room.Capacity if hasattr(room, 'Capacity') else 0
        students_alloted = room.Students_Alloted if hasattr(room, 'Students_Alloted') else 0
        remaining_capacity = max(0, capacity - students_alloted)

        room_info = {
            'pk': room.pk,
            'number': room.Room_No,
            'type': room.Room_Type,
            'capacity': capacity,
            'available': remaining_capacity,
            'price': price,
            'hostel_id': room.Hostel_ID.pk if room.Hostel_ID else None,
            'hostel_name': room.Hostel_ID.Hostel_Name if room.Hostel_ID else "Unknown"
        }
        room_data.append(room_info)

    import json

    return render(request, 'student_management/add_student.html', {
        'hostels': hostels,
        'rooms': rooms,
        'room_data_json': json.dumps(room_data)
    })

@login_required
def list_students(request):
    search_query = request.GET.get('search', '')
    selected_hostel = request.GET.get('hostel', '')
    selected_department = request.GET.get('department', '')
    selected_fee_status = request.GET.get('fee_status', '')
    sort_by = request.GET.get('sort', 'id')  # Default sort by ID
    sort_direction = request.GET.get('direction', 'asc')  # Default ascending

    students = Student.objects.all().select_related('Room_ID', 'Hostel_ID', 'user')

    if search_query:
        students = students.filter(
            Q(F_Name__icontains=search_query) |
            Q(L_Name__icontains=search_query) |
            Q(Registration_Number__icontains=search_query) |
            Q(user__email__icontains=search_query)
        )

    if selected_hostel:
        students = students.filter(Hostel_ID=selected_hostel)

    if selected_department:
        students = students.filter(Department=selected_department)

    if selected_fee_status:
        students = students.filter(fee_status=selected_fee_status)

    order_by_field = ''
    if sort_by == 'id':
        order_by_field = 'Student_ID'
    elif sort_by == 'name':
        order_by_field = 'F_Name'
    elif sort_by == 'email':
        order_by_field = 'user__email'
    elif sort_by == 'department':
        order_by_field = 'Department'
    elif sort_by == 'hostel':
        order_by_field = 'Hostel_ID__Hostel_Name'
    elif sort_by == 'fee_status':
        order_by_field = 'fee_status'
    elif sort_by == 'room_price':  # Add sorting by room price
        order_by_field = 'room_price'

    if sort_direction == 'desc' and order_by_field:
        order_by_field = f'-{order_by_field}'

    if order_by_field:
        students = students.order_by(order_by_field)

    for student in students:
        if not hasattr(student, 'room_price') or student.room_price == 0:
            if student.Room_ID:
                room = student.Room_ID
                student.room_price = room.Price if room.Price > 0 else (room.room_type_info.price if room.room_type_info else 0)
                Student.objects.filter(pk=student.pk).update(room_price=student.room_price)
        
        if hasattr(student, 'total_fee_amount'):
            student.total_fee = student.total_fee_amount
        else:
            student.total_fee = student.room_price
        
        if hasattr(student, 'total_paid_amount'):
            student.total_paid_amount = student.total_paid_amount
        else:
            payments = Payment.objects.filter(Student_ID=student.pk)
            student.total_paid_amount = payments.aggregate(Sum('Amount_Paid'))['Amount_Paid__sum'] or 0
        
        if hasattr(student, 'calculate_remaining_fee'):
            student.remaining_amount = student.calculate_remaining_fee()
        else:
            student.remaining_amount = max(0, student.total_fee - student.total_paid_amount)

    departments = Student.objects.values_list('Department', flat=True).distinct()
    hostels = Hostel.objects.all()

    total_students = students.count()
    fully_paid_count = sum(1 for student in students if student.fee_status == 'FULLY_PAID')
    not_paid_count = sum(1 for student in students if student.fee_status == 'NOT_PAID')
    partially_paid_count = sum(1 for student in students if student.fee_status == 'PARTIALLY_PAID')

    page = request.GET.get('page', 1)
    paginator = Paginator(students, 10)

    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    context = {
        'students': students,
        'search_query': search_query,
        'selected_hostel': selected_hostel,
        'selected_department': selected_department,
        'selected_fee_status': selected_fee_status,
        'sort_by': sort_by,
        'sort_direction': sort_direction,
        'departments': departments,
        'hostels': hostels,
        'total_students': total_students,
        'fully_paid_count': fully_paid_count,
        'not_paid_count': not_paid_count,
        'partially_paid_count': partially_paid_count
    }

    return render(request, 'student_management/list_students.html', context)

@login_required
def view_student(request, student_id):
    # Get the student object based on student_id
    student = get_object_or_404(Student, Student_ID=student_id)

    return render(request, 'student_management/view_student.html', {'student': student})

@login_required
def export_students_csv(request):
    # Get the same filter parameters as in list_students view
    search_query = request.GET.get('search', '')
    selected_hostel = request.GET.get('hostel', '')
    selected_department = request.GET.get('department', '')
    selected_fee_status = request.GET.get('fee_status', '')
    
    # Apply the same filters as in the list view
    students = Student.objects.all().select_related('Room_ID', 'Hostel_ID', 'user')
    
    if search_query:
        students = students.filter(
            Q(F_Name__icontains=search_query) |
            Q(L_Name__icontains=search_query) |
            Q(Registration_Number__icontains=search_query) |
            Q(user__email__icontains=search_query)
        )
    
    if selected_hostel:
        students = students.filter(Hostel_ID=selected_hostel)
    
    if selected_department:
        students = students.filter(Department=selected_department)
    
    if selected_fee_status:
        students = students.filter(fee_status=selected_fee_status)
    
    # Create the HttpResponse object with CSV header
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students_export.csv"'
    
    # Create CSV writer
    writer = csv.writer(response)
    
    # Write header row
    writer.writerow([
        'Student ID', 'Registration Number', 'First Name', 'Last Name', 
        'Email', 'Department', 'Room Number', 'Room Type', 'Hostel', 
        'Fee Status', 'Total Fee', 'Paid Amount', 'Due Amount'
    ])
    
    # Write data rows
    for student in students:
        # Calculate fees for this student
        total_fee = student.total_fee_amount
        paid_amount = student.total_paid_amount
        remaining = student.calculate_remaining_fee()
        
        writer.writerow([
            student.Student_ID,
            student.Registration_Number,
            student.F_Name,
            student.L_Name,
            student.user.email,
            student.Department,
            student.Room_ID.Room_No if student.Room_ID else 'Not Assigned',
            student.Room_ID.Room_Type if student.Room_ID else 'N/A',
            student.Hostel_ID.Hostel_Name if student.Hostel_ID else 'N/A',
            student.get_fee_status_display(),
            total_fee,
            paid_amount,
            remaining
        ])
    
    return response
@login_required
def export_students_pdf(request):
    # Get the same filter parameters as in list_students view
    search_query = request.GET.get('search', '')
    selected_hostel = request.GET.get('hostel', '')
    selected_department = request.GET.get('department', '')
    selected_fee_status = request.GET.get('fee_status', '')
    
    # Apply the same filters as in the list view
    students = Student.objects.all().select_related('Room_ID', 'Hostel_ID', 'user')
    
    if search_query:
        students = students.filter(
            Q(F_Name__icontains=search_query) |
            Q(L_Name__icontains=search_query) |
            Q(Registration_Number__icontains=search_query) |
            Q(user__email__icontains=search_query)
        )
    
    if selected_hostel:
        students = students.filter(Hostel_ID=selected_hostel)
    
    if selected_department:
        students = students.filter(Department=selected_department)
    
    if selected_fee_status:
        students = students.filter(fee_status=selected_fee_status)
    
    # Create a file-like buffer to receive PDF data
    buffer = BytesIO()
    
    # Create the PDF object, using the buffer as its "file"
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Add title
    title_style = getSampleStyleSheet()["Title"]
    elements.append(Paragraph("Student Report", title_style))
    elements.append(Spacer(1, 12))
    
    # Add date and time
    date_style = getSampleStyleSheet()["Normal"]
    date_text = f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    elements.append(Paragraph(date_text, date_style))
    elements.append(Spacer(1, 12))
    
    # Add filter information if any filters were applied
    if search_query or selected_hostel or selected_department or selected_fee_status:
        filter_info = []
        if search_query:
            filter_info.append(f"Search: {search_query}")
        if selected_hostel:
            hostel = Hostel.objects.get(pk=selected_hostel).Hostel_Name
            filter_info.append(f"Hostel: {hostel}")
        if selected_department:
            filter_info.append(f"Department: {selected_department}")
        if selected_fee_status:
            status_display = dict(PAYMENT_STATUS_CHOICES)[selected_fee_status]
            filter_info.append(f"Fee Status: {status_display}")
        
        filter_text = "Filters applied: " + ", ".join(filter_info)
        elements.append(Paragraph(filter_text, date_style))
        elements.append(Spacer(1, 12))
    
    # Create table data and style
    data = [
        ['ID', 'Student Name', 'Registration', 'Department', 'Room', 'Hostel', 'Fee Status', 'Total Fee', 'Paid', 'Due']
    ]
    
    # Add student data rows
    for student in students:
        total_fee = student.total_fee_amount
        paid_amount = student.total_paid_amount
        remaining = student.calculate_remaining_fee()
        
        row = [
            str(student.Student_ID),
            f"{student.F_Name} {student.L_Name}",
            student.Registration_Number,
            student.Department,
            student.Room_ID.Room_No if student.Room_ID else 'N/A',
            student.Hostel_ID.Hostel_Name if student.Hostel_ID else 'N/A',
            student.get_fee_status_display(),
            f"Rs{total_fee}",
            f"Rs{paid_amount}",
            f"Rs{remaining}"
        ]
        data.append(row)
    
    # Create the table
    table = Table(data)
    
    # Add style to the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    table.setStyle(style)
    
    # Add the table to our elements list
    elements.append(table)
    
    # Add summary information
    elements.append(Spacer(1, 24))
    summary_style = getSampleStyleSheet()["Heading2"]
    elements.append(Paragraph("Summary", summary_style))
    elements.append(Spacer(1, 12))
    
    # Count student fee status for summary
    total_students = students.count()
    fully_paid_count = sum(1 for student in students if student.fee_status == 'FULLY_PAID')
    not_paid_count = sum(1 for student in students if student.fee_status == 'NOT_PAID')
    partially_paid_count = sum(1 for student in students if student.fee_status == 'PARTIALLY_PAID')
    
    summary_data = [
        ['Status', 'Count', 'Percentage'],
        ['Fully Paid', str(fully_paid_count), f"{fully_paid_count/total_students*100:.1f}%" if total_students else "0%"],
        ['Partially Paid', str(partially_paid_count), f"{partially_paid_count/total_students*100:.1f}%" if total_students else "0%"],
        ['Not Paid', str(not_paid_count), f"{not_paid_count/total_students*100:.1f}%" if total_students else "0%"],
        ['Total Students', str(total_students), "100%"]
    ]
    
    summary_table = Table(summary_data, colWidths=[100, 50, 80])
    summary_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    summary_table.setStyle(summary_style)
    elements.append(summary_table)
    
    # Build the PDF document
    doc.build(elements)
    
    # Get the value of the BytesIO buffer and write it to the response
    pdf = buffer.getvalue()
    buffer.close()
    
    # Create and return the response
    response = HttpResponse(content_type='application/pdf')
    filename = f"students_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    response.write(pdf)
    
    return response

@login_required
def bulk_fee_reminder(request):
    if request.method == "POST":
        # Get students with pending or unpaid fees
        students_to_remind = Student.objects.filter(
            Q(fee_status='NOT_PAID') | Q(fee_status='PARTIALLY_PAID')
        ).select_related('user', 'Room_ID', 'Hostel_ID')
        
        # Check if any students were selected
        selected_students = request.POST.getlist('selected_students')
        if selected_students:
            students_to_remind = students_to_remind.filter(Student_ID__in=selected_students)
        
        # Get reminder message from form
        reminder_subject = request.POST.get('reminder_subject', 'Fee Payment Reminder')
        reminder_message = request.POST.get('reminder_message', '')
        
        # Track successful and failed emails
        success_count = 0
        failed_emails = []
        
        # Send email to each selected student
        for student in students_to_remind:
            try:
                # Calculate fee information
                total_fee = student.total_fee_amount
                paid_amount = student.total_paid_amount
                due_amount = student.calculate_remaining_fee()
                
                # Build personalized message
                personalized_message = reminder_message.replace('{name}', f"{student.F_Name} {student.L_Name}")
                personalized_message = personalized_message.replace('{total_fee}', str(total_fee))
                personalized_message = personalized_message.replace('{paid_amount}', str(paid_amount))
                personalized_message = personalized_message.replace('{due_amount}', str(due_amount))
                
                # Send email
                send_mail(
                    subject=reminder_subject,
                    message=personalized_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[student.user.email],
                    fail_silently=False,
                )
                
                # Log this reminder
                FeeReminder.objects.create(
                    student=student,
                    message=personalized_message,
                    sent_by=request.user
                )
                
                success_count += 1
                
            except Exception as e:
                failed_emails.append(f"{student.user.email} ({str(e)})")
        
        # Provide feedback to user
        if success_count > 0:
            messages.success(request, f"Successfully sent {success_count} fee reminders.")
        
        if failed_emails:
            messages.error(request, f"Failed to send reminders to {len(failed_emails)} students.")
            for failed in failed_emails[:5]:  # Show first 5 failures
                messages.error(request, f"Failed: {failed}")
            
            if len(failed_emails) > 5:
                messages.error(request, f"... and {len(failed_emails) - 5} more failures.")
        
        return redirect('list_students')
    
    else:  # GET request
        # Get students with pending or unpaid fees
        students_to_remind = Student.objects.filter(
            Q(fee_status='NOT_PAID') | Q(fee_status='PARTIALLY_PAID')
        ).select_related('user', 'Room_ID', 'Hostel_ID')
        
        # Calculate fee information for each student
        for student in students_to_remind:
            student.total_fee = student.total_fee_amount
            student.total_paid_amount = student.total_paid_amount
            student.remaining_amount = student.calculate_remaining_fee()
        
        # Prepare default reminder message template
        default_message = """Dear {name},

This is a reminder that your hostel fee payment is due. Please find the details below:

Total Fee: Rs{total_fee}
Amount Paid: Rs{paid_amount}
Balance Due: Rs{due_amount}

Please make the payment at your earliest convenience to avoid any penalties.

Thank you,
Hostel Administration"""
        
        return render(request, 'student_management/bulk_fee_reminder.html', {
            'students': students_to_remind,
            'default_message': default_message,
            'default_subject': 'Fee Payment Reminder'
        })

@login_required
def edit_student(request, student_id):
    student = get_object_or_404(Student, Student_ID=student_id)

    if request.method == 'POST':
        # Get the previous room before changes
        previous_room = student.Room_ID

        # Update student details from form data
        student.F_Name = request.POST.get('first_name')
        student.L_Name = request.POST.get('last_name')
        student.user.email = request.POST.get('email')  # Update user email
        student.Contact_Info = request.POST.get('contact_info')
        student.Address = request.POST.get('address')
        student.Department = request.POST.get('department')
        student.FatherName = request.POST.get('father_name')
        student.fee_status = request.POST.get('fee_status')

        # Handle the registration number update and check if it's unique
        new_registration_number = request.POST.get('registration_number')
        if new_registration_number != student.Registration_Number:
            if Student.objects.filter(Registration_Number=new_registration_number).exists():
                messages.error(request, "The registration number already exists. Please choose a different one.")
                return redirect('edit_student', student_id=student_id)
            student.Registration_Number = new_registration_number  # Update the registration number

        # Fetch room and hostel details from the form
        room_id = request.POST.get('room_id')
        hostel_id = request.POST.get('hostel_id')

        try:
            # Update room and hostel
            student.Room_ID = get_object_or_404(Room, Room_ID=room_id)
            student.Hostel_ID = get_object_or_404(Hostel, Hostel_ID=hostel_id)
        except (Room.DoesNotExist, Hostel.DoesNotExist):
            messages.error(request, "Invalid Room or Hostel ID selected!")
            return redirect('edit_student', student_id=student_id)

        # Handle the room allocation properly
        if previous_room and student.Room_ID != previous_room:
            # Decrease the capacity of the previous room (remove the student)
            if previous_room.Students_Alloted > 0:
                previous_room.Students_Alloted -= 1
                previous_room.save()

        # Update room allocations if the room changes
        if student.Room_ID:
            student.Room_ID.Students_Alloted += 1
            student.Room_ID.save()

        # Handle profile picture upload
        profile_picture = request.FILES.get('profile_picture')
        if profile_picture:
            student.profile_picture = profile_picture

        # Save the user and student details
        student.user.save()  # Save the user model
        student.save()  # Save the student model

        messages.success(request, 'Student updated successfully!')
        return redirect('list_students')

    # Render the edit student form with current student data
    hostels = Hostel.objects.all()
    rooms = Room.objects.all()

    return render(request, 'student_management/edit_student.html', {'student': student, 'hostels': hostels, 'rooms': rooms})

def delete_student(request, student_id):
    # Get the student object or return 404 if not found
    student = get_object_or_404(Student, pk=student_id)
    room = student.Room_ID  # Get the assigned room

    if request.method == "POST":
        # Delete the student from the database
        student.delete()
        
        # Update the room allocation count
        if room:
            # Ensure the room doesn't go below 0 students
            room.Students_Alloted = max(room.Students_Alloted - 1, 0)
            
            # Save the room after updating the student count
            room.save()
            
            # No need to manually set remaining_capacity since it's a property
            # that calculates automatically

        # Display success message and redirect to the student list
        messages.success(request, "Student deleted successfully, and room availability updated!")
        return redirect("list_students")  # Redirect to student list

    # Render confirmation template
    return render(request, "confirm_delete.html", {"student": student})

# ===========================
# Add Notice View Function (Admin only)
# List All Notices Function (Admin only)
# View Specific Notice Function (Admin only)
# Edit Notice Function (Admin only)
# Delete Notice Function (Admin only)
# ===========================

@login_required
def add_notice(request):
    # Ensure that only admins can add notices
    if not request.user.is_staff:
        return redirect('student_dashboard')  # Redirect non-admin users to their dashboard
    
    # Check if the user has a profile; if not, create one
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)
    
    # Fetch the admin associated with the logged-in user
    try:
        admin = Admin.objects.get(Email=request.user.email)
    except Admin.DoesNotExist:
        # If the admin doesn't exist, create one
        admin = Admin.objects.create(
            Name=request.user.username,
            Admin_Role='Superuser',
            Email=request.user.email,
            Contact_Information=request.user.profile.contact_info if hasattr(request.user.profile, 'contact_info') else request.user.email
        )
    
    # Handle POST request to create a new notice
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        expiry_date_str = request.POST.get('expiry_date')
        
        # Handle expiry date properly
        expiry_date = None
        if expiry_date_str and expiry_date_str.strip():
            try:
                expiry_date = timezone.make_aware(datetime.strptime(expiry_date_str, '%Y-%m-%d'))
            except ValueError:
                messages.error(request, 'Invalid date format. Please use YYYY-MM-DD format.')
                return render(request, 'add_notice.html')
        
        # Create and save the new notice
        notice = NoticeBoard.objects.create(
            Title=title,
            Content=content,
            Expiry_Date=expiry_date,
            Admin_ID=admin,  # Automatically link the notice to the admin
            Is_Active=True
        )
        
        # Display success message
        messages.success(request, 'Notice created successfully!')
        
        # Redirect to dashboard to see the notice right away
        return redirect('dashboard')  # Changed from 'list_of_notices'
    
    # Render the notice creation page
    return render(request, 'notice_complaint_management/add_notice.html')

@login_required
def list_of_notices(request):
    # Ensure only admins can access the list of notices
    if not request.user.is_staff:
        return redirect('student_notices')  # Redirect students to their notice page
        
    # Fetch all notices from the database, ordered by the most recent
    notices = NoticeBoard.objects.all().order_by('-Created_At')
    
    # Render the list of notices
    return render(request, 'notice_complaint_management/list_of_noticeboard.html', {'notices': notices})

@login_required
def view_notice(request, notice_id):
    # Ensure only admins can view the notice (students are redirected to their version)
    if not request.user.is_staff:
        return redirect('student_view_notice', notice_id=notice_id)
        
    try:
        # Fetch the notice using the ID
        notice = NoticeBoard.objects.get(Notice_ID=notice_id)
        return render(request, 'notice_complaint_management/view_notice.html', {'notice': notice})
    except NoticeBoard.DoesNotExist:
        # Handle the case where the notice doesn't exist
        messages.error(request, 'Notice not found!')
        return redirect('notice_complaint_management/list_of_notices')

@login_required
def edit_notice(request, notice_id):
    # Ensure only admins can edit the notice
    if not request.user.is_staff:
        return redirect('student_dashboard')  # Redirect non-admin users to their dashboard
    
    try:
        # Fetch the notice to be edited
        notice = NoticeBoard.objects.get(Notice_ID=notice_id)
        
        if request.method == 'POST':
            # Update notice fields from the form data
            notice.Title = request.POST.get('title')
            notice.Content = request.POST.get('content')
            notice.Expiry_Date = request.POST.get('expiry_date') or None
            notice.Is_Active = 'is_active' in request.POST
            notice.save()
            
            messages.success(request, 'Notice updated successfully!')
            return redirect('view_notice', notice_id=notice_id)
            
        # Render the edit form with current notice data
        return render(request, 'notice_complaint_management/edit_notice.html', {'notice': notice})
    except NoticeBoard.DoesNotExist:
        # Handle case where the notice does not exist
        messages.error(request, 'Notice not found!')
        return redirect('list_of_notices')

@login_required
def delete_notice(request, notice_id):
    # Ensure only admins can delete the notice
    if not request.user.is_staff:
        return redirect('student_dashboard')  # Redirect non-admin users to their dashboard

    try:
        # Fetch the notice to be deleted
        notice = NoticeBoard.objects.get(Notice_ID=notice_id)
    except NoticeBoard.DoesNotExist:
        # Handle case where the notice does not exist
        messages.error(request, 'Notice not found!')
        return redirect('list_of_notices')

    # Handle GET request to show the delete confirmation page
    if request.method == 'GET':
        return render(request, 'delete_notice_confirmation.html', {'notice': notice})

    # Handle POST request to delete the notice
    if request.method == 'POST':
        notice.delete()
        messages.success(request, 'Notice deleted successfully!')
        return redirect('list_of_notices')

# ===========================
# Student Notice Views
#Student view All Notices
# ===========================

@login_required
def student_notices(request):
    # Fetch all active notices from the database
    notices = NoticeBoard.objects.filter(Is_Active=True).order_by('-Created_At')
    
    # Render the notice board for students
    return render(request, 'notice_complaint_management/student_notices.html', {'notices': notices})

@login_required
def student_view_notice(request, notice_id):
    try:
        # Attempt to retrieve the notice by its ID and ensure it is active
        notice = get_object_or_404(NoticeBoard, Notice_ID=notice_id, Is_Active=True)
        
        # Render the notice details for the student
        return render(request, 'notice_complaint_management/view_notice_student.html', {'notice': notice})
    
    except NoticeBoard.DoesNotExist:
        # If the notice doesn't exist or isn't active, show an error and redirect
        messages.error(request, 'Notice not found or has been deactivated.')
        return redirect('student_notices')


# ===========================
# Submit Complaint View
# View Complaint Details
# List Complaints View
# ===========================

@login_required
def submit_complaint(request):
    # Ensure the user is a student
    if not hasattr(request.user, 'student'):
        messages.error(request, "You must be a student to submit a complaint.")
        return redirect('student_dashboard')  # Redirect to student dashboard
    
    student = request.user.student  # Get the student object related to the user

    if request.method == "POST":
        # Capture complaint details from the form
        complaint_description = request.POST.get('complaint_description')
        complaint_type = request.POST.get('complaint_type')

        # Fetch the first admin (in a real app, choose an appropriate admin)
        admin = Admin.objects.first()

        # Create and save the complaint
        Complaint.objects.create(
            Student_ID=student,
            Admin_ID=admin,
            Complaint_Description=complaint_description,
            Complaint_Type=complaint_type,
        )

        # Notify the student about successful complaint submission
        messages.success(request, "Your complaint has been submitted successfully.")
        return redirect('student_dashboard')  # Redirect to student dashboard

    # Render the complaint submission form
    return render(request, 'notice_complaint_management/submit_complaint.html')

@login_required
def view_complaint(request, complaint_id):
    # Fetch the specific complaint by its ID
    complaint = get_object_or_404(Complaint, Complaint_ID=complaint_id)

    # Render the complaint details page
    return render(request, 'notice_complaint_management/view_complaint.html', {'complaint': complaint})

@login_required
def list_complaints(request):
    # Fetch all complaints ordered by creation date (latest first)
    complaints = Complaint.objects.all().order_by('-Created_At')

    # Mark all complaints as read when the user views them
    Complaint.objects.filter(is_read=False).update(is_read=True)
    
    # Reset the unread complaints count in the session
    request.session['unread_complaints'] = 0

    # Render the list of complaints
    return render(request, 'notice_complaint_management/list_complaints.html', {'complaints': complaints})


# ===========================
# Visitor Management
# Request Visitor Function
# Update Visitor Request Function
#Visitor Requests
# Admin manages visitor requests
#Student Visistors Request History
# ===========================

@login_required
def request_visitor(request):
    if request.method == 'POST':
        visitor_name = request.POST['visitor_name']
        contact_info = request.POST['contact_info']
        visitor_id_proof = request.POST['cnic']  # Use Visitor_ID_Proof field
        purpose_of_visit = request.POST['purpose_of_visit']
        time_in = request.POST['time_in']
        time_out = request.POST['time_out']

        # Ensure that the visitor is linked to the logged-in student
        visitor = Visitor.objects.create(
            name=visitor_name,
            contact_info=contact_info,
            Visitor_ID_Proof=visitor_id_proof,
            purpose_of_visit=purpose_of_visit,
            student=request.user.student  # Link the visitor to the logged-in student
        )

        # Create the visitor request
        VisitorRequest.objects.create(
            student=request.user.student,
            visitor=visitor,
            time_in=time_in,
            time_out=time_out,
            status="Pending"  # Default status is Pending
        )

        messages.success(request, "Visitor request submitted successfully.")
        return redirect('std_request_history')

    return render(request, 'visitor_management/request_visitor.html')

def update_visitor_request(request, id):
    visitor_request = get_object_or_404(VisitorRequest, id=id)

    if request.method == 'POST':
        status = request.POST.get('status')

        if status not in ['PENDING', 'APPROVED', 'REJECTED']:
            messages.error(request, "Invalid status selected.")
            return redirect('visitor_requests')

        visitor_request.status = status
        visitor_request.save()

        messages.success(request, "Visitor request updated successfully.")
        return redirect('visitor_requests')

    return render(request, 'visitor_management/update_visitor_request.html', {'visitor_request': visitor_request})

# Admin manages visitor requests
@login_required
def admin_manage_visitor_requests(request):
    if not request.user.is_staff:
        messages.error(request, "You do not have permission to view this page.")
        return redirect('home')

    # Get all unread visitor requests first (before marking them as read)
    visitor_requests = VisitorRequest.objects.all()

    if request.method == 'POST':
        request_id = request.POST.get('request_id')
        status = request.POST.get('status')

        try:
            visitor_request = VisitorRequest.objects.get(id=request_id)
            visitor_request.status = status
            visitor_request.save()

            messages.success(request, "Visitor request updated successfully.")
        except VisitorRequest.DoesNotExist:
            messages.error(request, "Visitor request not found.")
    
    # Only mark them as read AFTER processing the request
    VisitorRequest.objects.filter(is_read=False).update(is_read=True)

    return render(request, 'visitor_management/admin_manage_visitor_requests.html', {'visitor_requests': visitor_requests})
  
@login_required
def visitor_requests(request):
    # Get all visitor requests for the logged-in student
    visitor_requests = VisitorRequest.objects.filter(student=request.user.student)
    return render(request, 'visitor_management/visitor_requests.html', {'visitor_requests': visitor_requests})

@login_required
def std_request_history(request):
    # Fetch all visitor requests for the logged-in student
    student = request.user.student
    requests = VisitorRequest.objects.filter(student=student)
    return render(request, 'visitor_management/all_std_request_history.html', {'requests': requests})


# ===========================
# Disciplinary Management
# Admin Shocase Notices
# Create ShoseCase Notices 
# Edith ShoCase Notices Function
# Delete ShoCase Notices Function
# Student ShoCase Notices Function
# Views Student  ShoCase Notices Function
# ===========================


# Add these functions to your hostel/views.py file
# Helper function to count unread notices - add this to your existing context processors
def unread_notices_count(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'student'):
            student_unread_showcase_notices = StudentShowcaseNotice.objects.filter(
                student=request.user.student,
                read=False
            ).count()
            return {'student_unread_showcase_notices': student_unread_showcase_notices}
        elif request.user.is_staff:
            unread_showcase_notices = ShowcaseNotice.objects.filter(
                studentshowcasenotice__read=False
            ).distinct().count()
            return {'unread_showcase_notices': unread_showcase_notices}
    return {}

# Admin Views for Showcase Notices
@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_showcase_notices(request):
    notices = ShowcaseNotice.objects.all().order_by('-created_date')
    
    context = {
        'notices': notices,
    }
    return render(request, 'student_showcaseNotice/admin_showcase_notices.html', context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def create_showcase_notice(request):
    if request.method == 'POST':
        form = ShowcaseNoticeForm(request.POST)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.created_by = request.user
            notice.save()
            
            # Add selected students to the notice
            selected_students = form.cleaned_data['students']
            for student in selected_students:
                StudentShowcaseNotice.objects.create(student=student, notice=notice)
            
            messages.success(request, 'Disciplinary notice created successfully.')
            return redirect('admin_showcase_notices')  # Use the URL name, not the path
    else:
        form = ShowcaseNoticeForm()
    
    context = {
        'form': form,
    }
    return render(request, 'student_showcaseNotice/create_showcase_notice.html', context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def view_showcase_notice(request, notice_id):
    notice = get_object_or_404(ShowcaseNotice, id=notice_id)
    student_notices = StudentShowcaseNotice.objects.filter(notice=notice)
    
    context = {
        'notice': notice,
        'student_notices': student_notices,
    }
    return render(request, 'student_showcaseNotice/view_showcase_notice.html', context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def edit_showcase_notice(request, notice_id):
    # Fetch the notice using its ID
    notice = get_object_or_404(ShowcaseNotice, id=notice_id)
    
    if request.method == 'POST':
        # Create the form instance with POST data
        form = ShowcaseNoticeForm(request.POST, instance=notice)
        if form.is_valid():
            # Save the notice
            notice = form.save()
            
            # Get the list of students currently associated with the notice
            # Get the list of students currently associated with the notice
            current_students = set(StudentShowcaseNotice.objects.filter(notice=notice).values_list('student_id', flat=True))

            # Get the list of students selected in the form
            selected_students = set(student.pk for student in form.cleaned_data['students'])

            # Add new students
            for student in form.cleaned_data['students']:
                if student.pk not in current_students:
                    StudentShowcaseNotice.objects.create(student=student, notice=notice)
            # Remove students that were unselected
            StudentShowcaseNotice.objects.filter(notice=notice).exclude(student__in=form.cleaned_data['students']).delete()
            
            messages.success(request, 'Disciplinary notice updated successfully.')
            return redirect('admin_showcase_notices')  # Redirect to the notices list
            
    else:
        form = ShowcaseNoticeForm(instance=notice)
        form.initial['students'] = notice.students.all()  # Pre-populate the students field
    
    context = {
        'form': form,
        'notice': notice,
    }
    return render(request, 'student_showcaseNotice/edit_showcase_notice.html', context)


@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_showcase_notice(request, notice_id):
    notice = get_object_or_404(ShowcaseNotice, id=notice_id)
    
    if request.method == 'POST':
        notice.delete()
        messages.success(request, 'Disciplinary notice deleted successfully.')
        return redirect('admin_showcase_notices')
    
    context = {
        'notice': notice,
    }
    return render(request, 'student_showcaseNotice/delete_showcase_notice.html', context)

# Student Views for Showcase Notices
@login_required
def student_showcase_notices(request):
    student = request.user.student
    student_notices = StudentShowcaseNotice.objects.filter(student=student).order_by('-notice__created_date')
    
    context = {
        'student_notices': student_notices,
    }
    return render(request, 'student_showcaseNotice/student_showcase_notices.html', context)

@login_required
def view_student_showcase_notice(request, notice_id):
    student = request.user.student
    student_notice = get_object_or_404(StudentShowcaseNotice, notice_id=notice_id, student=student)
    
    # Mark notice as read if not already
    if not student_notice.read:
        student_notice.mark_as_read()
    
    context = {
        'student_notice': student_notice,
    }
    return render(request, 'student_showcaseNotice/view_student_showcase_notice.html', context)

# ===========================
# Mess Management System
# View Mess Membership Status
# Mess Membership and Attendance Management
# Apply For Mess Membership
# Mess Request
# Admin Mess Management System Active Memeber , Reject Application, Pending Application
# ===========================

@login_required
def mess_status(request):
    try:
        # Get the mess membership status for the logged-in student
        mess_membership = MessMembership.objects.get(student=request.user.student)

        # Check if the mess membership is approved, rejected, or still pending
        if mess_membership.approved:
            status_message = "Your application has been approved!"
            status_class = "success"
        elif mess_membership.status == "Rejected":
            status_message = "Your application has been rejected."
            status_class = "danger"
        else:
            status_message = "Your application is still pending. Please wait for admin approval."
            status_class = "warning"

        # Pass the status message and mess membership data to the template
        return render(request, 'mess_management/mess_status.html', {
            'status_message': status_message,
            'status_class': status_class,
            'mess_membership': mess_membership
        })

    except MessMembership.DoesNotExist:
        # If the student has not applied for mess, inform them and redirect to the apply page
        messages.warning(request, "You have not applied for mess yet. Please apply first.")
        return redirect('apply_for_mess')  # Redirect to the apply for mess page

@login_required
def apply_for_mess(request):
    try:
        # Check if the student already has an approved and active membership
        existing_membership = MessMembership.objects.filter(
            student=request.user.student, 
            approved=True, 
            is_active=True
        ).first()
        
        # Check for fingerprint enrollment status
        try:
            fingerprint = Fingerprint.objects.get(student=request.user.student)
            fingerprint_enrolled = True
        except Fingerprint.DoesNotExist:
            fingerprint_enrolled = False
        
        if existing_membership:
            messages.info(request, "You already have an active mess membership.")
            return render(request, 'mess_management/mess_apply.html', {
                'mess_membership': existing_membership,
                'fingerprint_enrolled': fingerprint_enrolled
            })
    except Exception:
        pass

    # Check if the student has already applied but their application is pending
    try:
        pending_membership = MessMembership.objects.get(
            student=request.user.student, 
            approved=False, 
            is_active=False
        )
        messages.info(request, "You have already applied for mess membership. Please wait for admin approval.")
        return redirect('mess_status')
    except MessMembership.DoesNotExist:
        pass

    # If no active membership exists and no pending application, allow them to apply
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        department = request.POST.get('department')
        fingerprint_data = request.POST.get('fingerprint_data')

        # Validate dates
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

            if start_date >= end_date:
                messages.error(request, "End date must be after start date.")
                return render(request, 'mess_management/mess_apply.html')

            if start_date < date.today():
                messages.error(request, "Start date cannot be in the past.")
                return render(request, 'mess_management/mess_apply.html')
        except ValueError:
            messages.error(request, "Invalid date format.")
            return render(request, 'mess_management/mess_apply.html')
        
        # Create a new fingerprint record or update existing one
        if fingerprint_data:
            try:
                fingerprint, created = Fingerprint.objects.update_or_create(
                    student=request.user.student,
                    defaults={'fingerprint_template': fingerprint_data}
                )
                
                # Create a new membership application with status "Pending"
                membership = MessMembership(
                    student=request.user.student,
                    start_date=start_date,
                    end_date=end_date,
                    department=department,
                    is_active=False,
                    approved=False,
                    status="Pending",
                    fingerprint=fingerprint  # Associate the fingerprint with the mess membership
                )
                membership.save()
                
                messages.success(request, "Mess membership application with fingerprint submitted successfully. Please wait for approval.")
                return redirect('mess_status')
            except Exception as e:
                messages.error(request, f"Error submitting application: {str(e)}")
        else:
            messages.error(request, "Fingerprint scan is required for mess application. Please scan your fingerprint.")
            return render(request, 'mess_management/mess_apply.html')

    return render(request, 'mess_management/mess_apply.html')



@staff_member_required
def admin_mess_management(request):
    # Fetch different categories of memberships
    active_memberships = MessMembership.objects.filter(approved=True, is_active=True).order_by('-date_applied')
    inactive_memberships = MessMembership.objects.filter(approved=True, is_active=False).order_by('-date_applied')
    rejected_memberships = MessMembership.objects.filter(status="Rejected").order_by('-date_applied')
    pending_requests = MessMembership.objects.filter(approved=False, status="Pending").order_by('-date_applied')
    
    # Handle activation of inactive memberships
    if request.method == 'POST':
        request_id = request.POST.get('request_id')
        action = request.POST.get('action')
        
        try:
            mess_request = MessMembership.objects.get(id=request_id)
            
            if action == 'activate':
                mess_request.is_active = True
                mess_request.save()
                messages.success(request, f"Membership for {mess_request.student} activated successfully!")
                
            elif action == 'deactivate':
                mess_request.is_active = False
                mess_request.save()
                messages.success(request, f"Membership for {mess_request.student} deactivated successfully!")
                
        except MessMembership.DoesNotExist:
            messages.error(request, "Membership not found!")
            
        return redirect('admin_mess_management')
    
    context = {
        'active_memberships': active_memberships,
        'inactive_memberships': inactive_memberships,
        'rejected_memberships': rejected_memberships,
        'pending_requests': pending_requests,
        'active_tab': 'active'  # Default active tab
    }
    
    return render(request, 'mess_management/admin_mess_management.html', context)

@staff_member_required
def inactive_memberships(request):
    # Fetch inactive mess memberships (students who have mess membership but not active)
    inactive_memberships = MessMembership.objects.filter(
        approved=True, 
        is_active=False
    ).order_by('-date_applied')

    # Fetch students who are in a hostel but do not have a mess membership (haven't joined the mess)
    students_not_in_mess = Student.objects.filter(
        Room_ID__isnull=False  # Ensure the student is assigned to a room (i.e., in a hostel)
    ).exclude(
        messmembership__isnull=False  # Ensure they have no mess membership
    )
    
    # Combine both querysets by preparing two different lists for rendering in the context
    context = {
        'inactive_memberships': inactive_memberships,
        'students_not_in_mess': students_not_in_mess,
        'active_tab': 'inactive'  # Mark this tab as active
    }

    # Handle activation of inactive memberships
    if request.method == 'POST':
        request_id = request.POST.get('request_id')
        action = request.POST.get('action')

        try:
            mess_request = MessMembership.objects.get(id=request_id)

            if action == 'activate':
                mess_request.is_active = True
                mess_request.save()
                messages.success(request, f"Membership for {mess_request.student} activated successfully!")

        except MessMembership.DoesNotExist:
            messages.error(request, "Membership not found!")

        return redirect('inactive_memberships')

    return render(request, 'mess_management/inactive_memberships.html', context)

@staff_member_required
def rejected_applications(request):
    # Fetch rejected applications
    rejected_memberships = MessMembership.objects.filter(status="Rejected").order_by('-date_applied')
    
    context = {
        'rejected_memberships': rejected_memberships,
        'active_tab': 'rejected'  # Mark this tab as active
    }
    
    return render(request, 'mess_management/rejected_applications.html', context)


@staff_member_required
def mess_request(request):
    # Fetch pending requests
    pending_requests = MessMembership.objects.filter(approved=False, status="Pending").order_by('-date_applied')
    
    if request.method == 'POST':
        request_id = request.POST.get('request_id')
        action = request.POST.get('action')
        
        try:
            mess_request = MessMembership.objects.get(id=request_id)
            
            if action == 'approve':
                mess_request.approved = True
                mess_request.is_active = True
                mess_request.status = "Approved"
                mess_request.save()
                messages.success(request, f"Membership for {mess_request.student} approved successfully!")
            
            elif action == 'reject':
                mess_request.status = "Rejected"
                mess_request.save()
                messages.success(request, f"Membership request for {mess_request.student} rejected successfully!")
            
            elif action == 'deactivate':
                mess_request.is_active = False
                mess_request.save()
                messages.success(request, f"Membership for {mess_request.student} deactivated successfully!")
            
            elif action == 'activate':
                mess_request.is_active = True
                mess_request.save()
                messages.success(request, f"Membership for {mess_request.student} activated successfully!")
        
        except MessMembership.DoesNotExist:
            messages.error(request, "Request not found!")
        
        return redirect('mess_request')
    
    context = {
        'pending_requests': pending_requests,
        'active_tab': 'pending'  # Mark this tab as active
    }
    
    return render(request, 'mess_management/mess_request.html', context)


# ===========================
# Mess Attandance Management System
# Admin Manage Attandance 
# Mark Attandance BreakFAst, Lunch, TeaBreak, Dinner Attandance 

# ===========================


@staff_member_required
def manage_attendance(request):
    # Filter by date if provided
    date_filter = request.GET.get('date')
    if date_filter:
        # Handle filtering of records by date
        breakfast_records = MessAttendance.objects.filter(meal_time='BF', date=date_filter).order_by('-date')
        lunch_records = MessAttendance.objects.filter(meal_time='LN', date=date_filter).order_by('-date')
        tea_break_records = MessAttendance.objects.filter(meal_time='ET', date=date_filter).order_by('-date')
        dinner_records = MessAttendance.objects.filter(meal_time='DN', date=date_filter).order_by('-date')

        # Set records to None if no records exist for the given date
        if not breakfast_records.exists():
            breakfast_records = None
        if not lunch_records.exists():
            lunch_records = None
        if not tea_break_records.exists():
            tea_break_records = None
        if not dinner_records.exists():
            dinner_records = None
    else:
        # Fetch all attendance records for each meal
        breakfast_records = MessAttendance.objects.filter(meal_time='BF').order_by('-date')
        lunch_records = MessAttendance.objects.filter(meal_time='LN').order_by('-date')
        tea_break_records = MessAttendance.objects.filter(meal_time='ET').order_by('-date')
        dinner_records = MessAttendance.objects.filter(meal_time='DN').order_by('-date')

    context = {
        'breakfast_records': breakfast_records,
        'lunch_records': lunch_records,
        'tea_break_records': tea_break_records,
        'dinner_records': dinner_records
    }
    
    return render(request, 'mess_management/manage_attendance.html', context)


@login_required
def mark_attendance(request):
    student = request.user.student
    
    # Check if the student is a mess member
    mess_membership = MessMembership.objects.filter(student=student, approved=True, is_active=True).first()
    if not mess_membership:
        messages.error(request, "You are not a mess member. Please apply for a mess membership first.")
        return redirect('mess_apply')  # Redirect to the page where students can apply for mess membership

    # Proceed with marking attendance if the student is a mess member
    today = timezone.now().date()
    
    # Get all meal times
    meal_times = [
        {'code': 'BF', 'name': 'Breakfast'},
        {'code': 'LN', 'name': 'Lunch'},
        {'code': 'ET', 'name': 'Evening Tea'},
        {'code': 'DN', 'name': 'Dinner'}
    ]
    all_meal_codes = {meal['code'] for meal in meal_times}
    
    # Check which meal times have already been marked today
    marked_meals = set(MessAttendance.objects.filter(
        student=student,
        date=today
    ).values_list('meal_time', flat=True))
    
    # Process form submission
    if request.method == 'POST':
        for meal_code in all_meal_codes:
            checkbox_name = f'is_present_{meal_code}'
            
            # Only process if this meal hasn't been marked yet
            if meal_code not in marked_meals and checkbox_name in request.POST:
                # Get current meal price from menu (using filter() instead of get())
                menu_item = MessMenu.objects.filter(meal_time=meal_code, date=today).first()  # Use .first() to get the first result
                
                if not menu_item:
                    # Default price if no menu item exists
                    price = 0
                else:
                    price = menu_item.price
                
                # Create attendance record
                MessAttendance.objects.create(
                    student=student,
                    date=today,
                    meal_time=meal_code,
                    is_present=True,
                    price_charged=price
                )
                
        # Redirect to the same page to refresh the data
        return redirect('mess_attendance')
    
    # Calculate remaining meals to be marked
    remaining_meals = all_meal_codes - marked_meals
    
    # Get attendance for the last 30 days
    start_date = today - timezone.timedelta(days=30)
    
    # Get all attendance records in the date range
    attendance_records = MessAttendance.objects.filter(
        student=student,
        date__gte=start_date,
        date__lte=today
    ).order_by('-date')
    
    # Organize attendance by date for display
    attendance_by_date = {}
    
    for record in attendance_records:
        if record.date not in attendance_by_date:
            attendance_by_date[record.date] = {
                'date': record.date,
                'meals': {}
            }
        
        attendance_by_date[record.date]['meals'][record.meal_time] = {
            'is_present': record.is_present,
            'price': record.price_charged
        }
    
    # Convert to list and sort by date
    attendance_history = list(attendance_by_date.values())
    attendance_history.sort(key=lambda x: x['date'], reverse=True)
    
    context = {
        'attendance_history': attendance_history,
        'meal_times': meal_times,
        'marked_meals': marked_meals,
        'remaining_meals': remaining_meals
    }
    
    return render(request, 'mess_management/mess_attendance.html', context)

@login_required
def mess_attendance(request):
    student = request.user.student
    today = timezone.now().date()
    
    # Check if the student is a mess member with an approved and active membership
    try:
        mess_membership = MessMembership.objects.get(
            student=student, 
            approved=True, 
            is_active=True
        )
    except MessMembership.DoesNotExist:
        # Check if student has applied but not approved
        pending_application = MessMembership.objects.filter(student=student).first()
        if pending_application:
            if pending_application.status == "Rejected":
                messages.error(request, "Your mess membership application was rejected. Please contact the administration.")
            else:
                messages.warning(request, "Your mess membership application is still pending approval. You cannot mark attendance until it's approved.")
            return redirect('mess_status')
        else:
            # No application exists
            messages.warning(request, "You are not a mess member. Please apply for mess membership first.")
            return redirect('apply_for_mess')
    
    # Get all meal times
    meal_times = [
        {'code': 'BF', 'name': 'Breakfast'},
        {'code': 'LN', 'name': 'Lunch'},
        {'code': 'ET', 'name': 'Evening Tea'},
        {'code': 'DN', 'name': 'Dinner'}
    ]
    all_meal_codes = {meal['code'] for meal in meal_times}
    
    # Check which meal times have already been marked today
    marked_meals = set(MessAttendance.objects.filter(
        student=student,
        date=today
    ).values_list('meal_time', flat=True))
    
    # Process form submission
    if request.method == 'POST':
        for meal_code in all_meal_codes:
            checkbox_name = f'is_present_{meal_code}'
            
            # Only process if this meal hasn't been marked yet
            if meal_code not in marked_meals and checkbox_name in request.POST:
                # Get current meal price from menu
                menu_item = MessMenu.objects.filter(meal_time=meal_code, date=today).first()
                
                if not menu_item:
                    # Default price if no menu item exists
                    price = 0
                else:
                    price = menu_item.price
                
                # Create attendance record
                MessAttendance.objects.create(
                    student=student,
                    date=today,
                    meal_time=meal_code,
                    is_present=True,
                    price_charged=price
                )
                
        # Redirect to the same page to refresh the data
        messages.success(request, "Attendance marked successfully!")
        return redirect('mess_attendance')
    
    # Calculate remaining meals to be marked
    remaining_meals = all_meal_codes - marked_meals
    
    # Get attendance for the last 30 days
    start_date = today - timezone.timedelta(days=30)
    
    # Get all attendance records in the date range
    attendance_records = MessAttendance.objects.filter(
        student=student,
        date__gte=start_date,
        date__lte=today
    ).order_by('-date')
    
    # Organize attendance by date for display
    attendance_by_date = {}
    
    for record in attendance_records:
        if record.date not in attendance_by_date:
            attendance_by_date[record.date] = {
                'date': record.date,
                'meals': {}
            }
        
        attendance_by_date[record.date]['meals'][record.meal_time] = {
            'is_present': record.is_present,
            'price': record.price_charged
        }
    
    # Convert to list and sort by date
    attendance_history = list(attendance_by_date.values())
    attendance_history.sort(key=lambda x: x['date'], reverse=True)
    
    context = {
        'attendance_history': attendance_history,
        'meal_times': meal_times,
        'marked_meals': marked_meals,
        'remaining_meals': remaining_meals,
        'mess_membership': mess_membership
    }
    
    return render(request, 'mess_management/mess_attendance.html', context)

@staff_member_required
def breakfast_attendance(request):
    # Fetch attendance records for Breakfast only
    breakfast_records = MessAttendance.objects.filter(meal_time='BF').order_by('-date')

    context = {
        'breakfast_records': breakfast_records
    }

    return render(request, 'mess_management/breakfast_attendance.html', context)

@staff_member_required
def lunch_attendance(request):
    # Fetch attendance records for Lunch only
    lunch_records = MessAttendance.objects.filter(meal_time='LN').order_by('-date')

    context = {
        'lunch_records': lunch_records
    }

    return render(request, 'mess_management/lunch_attendance.html', context)

@staff_member_required
def tea_break_attendance(request):
    # Fetch attendance records for Tea Break only
    tea_break_records = MessAttendance.objects.filter(meal_time='ET').order_by('-date')

    context = {
        'tea_break_records': tea_break_records
    }

    return render(request, 'mess_management/tea_break_attendance.html', context)

@staff_member_required
def dinner_attendance(request):
    # Fetch attendance records for Dinner only
    dinner_records = MessAttendance.objects.filter(meal_time='DN').order_by('-date')

    context = {
        'dinner_records': dinner_records
    }

    return render(request, 'mess_management/dinner_attendance.html', context)


# ===========================
# Mess Menu Management (Admin)
# Add Mess Menu Function
# Add Multiple Mess Menu
# View Mess Menu
# ===========================

@staff_member_required
def add_mess_menu(request):
    if request.method == 'POST':
        date_str = request.POST.get('date')
        meal_time = request.POST.get('meal_time')
        dish_name = request.POST.get('dish_name')
        price_str = request.POST.get('price', '0')

        # Convert price to Decimal (using '0' as a fallback)
        try:
            price = Decimal(price_str.strip() or '0')
        except Exception:
            price = Decimal('0')

        # Parse the date string into a date object
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError as e:
            messages.error(request, f"Invalid date format: {e}")
            return redirect('add_mess_menu')

        # Create and save the menu item (model save() will auto-calculate day, week_number, month, year)
        menu_item = MessMenu(
            date=date_obj,
            meal_time=meal_time,
            dish_name=dish_name,
            price=price
        )
        menu_item.save()
        messages.success(request, "Menu item added successfully!")
        return redirect('view_mess_menu')

    context = {
        'meal_choices': MessMenu.MEAL_CHOICES,
        'day_choices': MessMenu.DAY_CHOICES,
    }
    return render(request, 'mess_management/add_mess_menu.html', context)


@staff_member_required
def add_multiple_menu_items(request):
    if request.method == 'POST':
        try:
            start_date_str = request.POST.get('start_date')
            end_date_str = request.POST.get('end_date')
            days = request.POST.getlist('days')
            meal_time = request.POST.get('meal_time')
            dish_name = request.POST.get('dish_name')
            price_str = request.POST.get('price', '0')
            
            # Convert price to Decimal
            price = Decimal(price_str.strip() or '0')

            # Parse the start and end dates
            start_date_obj = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date_obj = datetime.strptime(end_date_str, '%Y-%m-%d').date()

            # Validate date range
            if start_date_obj > end_date_obj:
                messages.error(request, "Start date must be before or equal to end date.")
                return redirect('add_multiple_menu_items')

            # Loop over the date range and add items for selected days
            current_date = start_date_obj
            while current_date <= end_date_obj:
                # Calculate day code (e.g., 'MON', 'TUE', etc.)
                day_code = current_date.strftime('%a').upper()[:3]
                if day_code in days:
                    menu_item = MessMenu(
                        date=current_date,
                        meal_time=meal_time,
                        dish_name=dish_name,
                        price=price
                    )
                    menu_item.save()
                current_date += timedelta(days=1)

            messages.success(request, "Multiple menu items added successfully!")
            return redirect('view_mess_menu')
        except ValueError as e:
            messages.error(request, f"Invalid date format: {e}")
            return redirect('add_multiple_menu_items')

    context = {
        'meal_choices': MessMenu.MEAL_CHOICES,
        'day_choices': MessMenu.DAY_CHOICES,
    }
    return render(request, 'mess_management/add_mess_menu.html', context)

@login_required
def view_mess_menu(request):
    today = timezone.now().date()
    selected_week = request.GET.get('week')
    selected_month = request.GET.get('month')
    selected_year = request.GET.get('year', str(today.year))

    # Handle selected month or week or default to this week
    if selected_month and selected_year:
        year = int(selected_year)
        month_num = datetime.strptime(selected_month, '%B').month
        start_date = date(year, month_num, 1)
        end_date = date(year + 1, 1, 1) - timedelta(days=1) if month_num == 12 else date(year, month_num + 1, 1) - timedelta(days=1)
        title = f"Mess Menu for {selected_month} {selected_year}"
    elif selected_week:
        year, week = map(int, selected_week.split('-W'))
        start_date = datetime.strptime(f'{year}-W{week}-1', '%Y-W%W-%w').date()
        end_date = start_date + timedelta(days=6)
        title = f"Mess Menu for Week {week}, {year}"
    else:
        start_date = today - timedelta(days=today.weekday())
        end_date = start_date + timedelta(days=6)
        title = "This Week's Mess Menu"

    # Fetch menu items for the selected date range
    menu_items = MessMenu.objects.filter(date__gte=start_date, date__lte=end_date)

    days_of_week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    meal_times = ['BF', 'LN', 'ET', 'DN']  # Updated to remove 'MB'

    # Populate the menu for each day and meal time
    structured_menu = {day: {meal: None for meal in meal_times} for day in days_of_week}
    for item in menu_items:
        if item.day in structured_menu and item.meal_time in structured_menu[item.day]:
            structured_menu[item.day][item.meal_time] = item

    current_year = today.year
    available_weeks = [(f"{current_year}-W{week}", f"Week {week}, {current_year}") for week in range(1, 53)]
    available_months = [(month_name, month_name) for month_name in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']]

    context = {
        'title': title,
        'structured_menu': structured_menu,
        'days_of_week': days_of_week,
        'meal_times': meal_times,
        'meal_names': dict(MessMenu.MEAL_CHOICES),
        'day_names': dict(MessMenu.DAY_CHOICES),
        'available_weeks': available_weeks,
        'available_months': available_months,
        'current_week': f"{today.year}-W{today.isocalendar()[1]}",
        'current_month': today.strftime('%B'),
        'current_year': today.year,
        'years': range(current_year-1, current_year+2),
    }
    
    return render(request, 'mess_management/view_mess_menu.html', context)


# ===========================
# Mess Payment System
# Mess Bill
# Add Mess Payment 
# Mess account Book
# Stripe Payment Gateway For Mess  
# ===========================

@login_required
def stripe_success(request):
    """
    Handle successful Stripe payment and display success page for mess payments
    """
    session_id = request.GET.get('session_id')
    if not session_id:
        messages.error(request, "No payment session found.")
        return redirect('add_mess_payment')
    
    try:
        # Retrieve the session details
        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.retrieve(session_id)
        payment_intent = session.payment_intent
        
        # First try to find by session ID
        stripe_payment = StripePayment.objects.filter(
            stripe_session_id=session_id
        ).first()
        
        # If not found, try to find by payment intent ID
        if not stripe_payment:
            stripe_payment = StripePayment.objects.filter(
                stripe_payment_intent_id=payment_intent
            ).first()
        
        # If still not found, try to find by student ID from session metadata
        if not stripe_payment and 'student_id' in session.metadata:
            student_id = session.metadata.get('student_id')
            payment_type = session.metadata.get('payment_type', 'MESS')
            
            stripe_payment = StripePayment.objects.filter(
                student_id=student_id,
                payment_type=payment_type,
                status='PENDING',
                stripe_payment_intent_id__isnull=True
            ).order_by('-created_at').first()
            
            # If found, update the payment intent ID
            if stripe_payment:
                stripe_payment.stripe_payment_intent_id = payment_intent
                stripe_payment.save()
        
        # Initialize context for the template
        context = {
            'success': False,
            'message': "Payment was processed, but we couldn't find your payment record.",
            'amount': None,
        }
        
        if stripe_payment:
            # Complete the payment and create a payment record
            try:
                # Create a new mess payment record
                payment = MessPayment.objects.create(
                    student=stripe_payment.student,
                    amount=stripe_payment.amount,
                    payment_date=timezone.now(),
                    payment_method='STRIPE',
                    payment_note=f'Payment via Stripe (Transaction ID: {payment_intent})'
                )
                
                # Update the stripe payment status
                stripe_payment.status = 'COMPLETED'
                stripe_payment.stripe_payment_intent_id = payment_intent
                stripe_payment.save()
                
                # Apply the payment to unpaid bills (oldest first)
                remaining_amount = payment.amount
                unpaid_bills = MessBill.objects.filter(
                    student=stripe_payment.student,
                    paid_status=False
                ).order_by('bill_date')
                
                for bill in unpaid_bills:
                    if remaining_amount <= 0:
                        break
                        
                    if remaining_amount >= bill.amount_due:
                        # Pay the bill in full
                        bill.paid_status = True
                        bill.paid_amount = bill.amount_due
                        bill.payment = payment
                        bill.payment_date = timezone.now()
                        bill.save()
                        
                        remaining_amount -= bill.amount_due
                    else:
                        # Partial payment
                        bill.paid_amount = remaining_amount
                        bill.payment = payment
                        bill.payment_date = timezone.now()
                        bill.save()
                        
                        remaining_amount = 0
                
                # Set success context
                context = {
                    'success': True,
                    'message': "Payment successful!",
                    'amount': stripe_payment.amount,
                    'payment_date': payment.payment_date,
                    'student_name': f"{stripe_payment.student.F_Name} {stripe_payment.student.L_Name}",
                    'registration_number': stripe_payment.student.Registration_Number
                }
                
                # Store success message in session for account_book view
                request.session['payment_success_message'] = f"Payment of Pkr{stripe_payment.amount} successful!"
                
                messages.success(request, f"Payment of Pkr{stripe_payment.amount} successful!")
                
            except Exception as e:
                context['message'] = f"Error completing payment: {str(e)}"
                messages.error(request, f"Error completing payment: {str(e)}")
                # Log the error for debugging
                print(f"Payment completion error: {str(e)}")
        
        # Use the provided success.html template to show payment success
        return render(request, 'mess_management/payment_success.html', context)
        
    except Exception as e:
        messages.error(request, f"Error processing payment: {str(e)}")
        return redirect('add_mess_payment')


@login_required
def stripe_cancel(request):
    """
    Handle cancelled Stripe payment for mess payments
    """
    messages.info(request, "Payment was cancelled.")
    return redirect('add_mess_payment')


@csrf_exempt
def stripe_webhook(request):
    """
    Handle Stripe webhook events for mess payments
    """
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
        
    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        
        # Get the payment intent ID
        payment_intent_id = session.get('payment_intent')
        
        if payment_intent_id:
            # Find the corresponding stripe payment
            stripe_payment = StripePayment.objects.filter(
                stripe_payment_intent_id=payment_intent_id
            ).first()
            
            # If not found by payment intent, try using session id
            if not stripe_payment:
                stripe_payment = StripePayment.objects.filter(
                    stripe_session_id=session.id
                ).first()
            
            # If still not found, try using metadata
            if not stripe_payment and 'student_id' in session.metadata:
                student_id = session.metadata.get('student_id')
                payment_type = session.metadata.get('payment_type', 'MESS')
                
                stripe_payment = StripePayment.objects.filter(
                    student_id=student_id,
                    payment_type=payment_type,
                    status='PENDING'
                ).order_by('-created_at').first()
                
                # Update the payment intent ID if found
                if stripe_payment:
                    stripe_payment.stripe_payment_intent_id = payment_intent_id
                    stripe_payment.save()
            
            if stripe_payment and stripe_payment.status == 'PENDING':
                try:
                    # Create a new mess payment record
                    payment = MessPayment.objects.create(
                        student=stripe_payment.student,
                        amount=stripe_payment.amount,
                        payment_date=timezone.now(),
                        payment_method='STRIPE',
                        payment_note=f'Payment via Stripe webhook (Transaction ID: {payment_intent_id})'
                    )
                    
                    # Update the stripe payment status
                    stripe_payment.status = 'COMPLETED'
                    stripe_payment.save()
                    
                    # Apply the payment to unpaid bills (oldest first)
                    remaining_amount = payment.amount
                    unpaid_bills = MessBill.objects.filter(
                        student=stripe_payment.student,
                        paid_status=False
                    ).order_by('bill_date')
                    
                    for bill in unpaid_bills:
                        if remaining_amount <= 0:
                            break
                            
                        if remaining_amount >= bill.amount_due:
                            # Pay the bill in full
                            bill.paid_status = True
                            bill.paid_amount = bill.amount_due
                            bill.payment = payment
                            bill.payment_date = timezone.now()
                            bill.save()
                            
                            remaining_amount -= bill.amount_due
                        else:
                            # Partial payment
                            bill.paid_amount = remaining_amount
                            bill.payment = payment
                            bill.payment_date = timezone.now()
                            bill.save()
                            
                            remaining_amount = 0
                    
                except Exception as e:
                    # Log error but return success to Stripe
                    print(f"Error completing payment via webhook: {str(e)}")
    
    return HttpResponse(status=200)



@login_required
def create_stripe_checkout_session(request):
    """
    Create a Stripe checkout session for mess payment
    """
    if request.method != 'POST':
        messages.error(request, "Invalid request method.")
        return redirect('add_mess_payment')
    
    # Only students can make mess payments
    if not hasattr(request.user, 'student'):
        messages.error(request, "Only students can make mess payments.")
        return redirect('dashboard')
        
    student = request.user.student
    
    try:
        amount = float(request.POST.get('amount', 0))
        payment_type = request.POST.get('payment_type', 'MESS')
        
        if amount <= 0:
            messages.error(request, "Payment amount must be greater than zero.")
            return redirect('add_mess_payment')
            
        # Convert to paise/cents for Stripe (smallest currency unit)
        stripe_amount = int(amount * 100)
        
        # Set up Stripe
        stripe.api_key = settings.STRIPE_SECRET_KEY
        
        # Create a payment record in our database
        stripe_payment = StripePayment.objects.create(
            student=student,
            amount=amount,
            payment_type=payment_type,
            status='PENDING',
            created_at=timezone.now()
        )
        
        # Success and cancel URLs
        success_url = request.build_absolute_uri(reverse('stripe_success')) + '?session_id={CHECKOUT_SESSION_ID}'
        cancel_url = request.build_absolute_uri(reverse('stripe_cancel'))
        
        # Create Stripe checkout session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'inr',
                        'product_data': {
                            'name': f"Mess Payment - {student.F_Name} {student.L_Name}",
                            'description': f"Mess fee payment for {student.Registration_Number}",
                        },
                        'unit_amount': stripe_amount,
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=success_url,
            cancel_url=cancel_url,
            metadata={
                'student_id': student.Student_ID,
                'payment_type': payment_type,
            }
        )
        
        # Save the session ID to our payment record
        stripe_payment.stripe_session_id = checkout_session.id
        stripe_payment.save()
        
        # Redirect to Stripe checkout
        return redirect(checkout_session.url)
        
    except ValueError:
        messages.error(request, "Invalid payment amount.")
        return redirect('add_mess_payment')
    except Exception as e:
        messages.error(request, f"Error creating payment: {str(e)}")
        return redirect('add_mess_payment')


def generate_daily_bill(student, date):
    """
    Generate or update a daily bill based on attendance for a specific date
    """
    # Get all attendance records for this student on this date where they were present
    attendance_records = MessAttendance.objects.filter(
        student=student,
        date=date,
        is_present=True
    )
    
    # Calculate total amount due
    total_amount = sum(record.price_charged for record in attendance_records)
    
    # Create or update the bill
    bill, created = MessBill.objects.get_or_create(
        student=student,
        bill_date=date,
        defaults={'amount_due': total_amount}
    )
    
    # If bill already existed, update the amount
    if not created:
        bill.amount_due = total_amount
        bill.save()
    
    return bill


@login_required
def mess_account_book(request, student_id=None):
    """
    View to display the mess account book for a specific student, including attendance, total cost,
    payment requests, and eligibility for payment requests.
    """
    # Check if student_id is provided; if not, show the logged-in user's account book
    if student_id is None:
        if hasattr(request.user, 'student'):
            student = request.user.student
        elif request.user.is_staff:
            return redirect('fee_management')  # Redirect to fee management if the user is staff
        else:
            return redirect('dashboard')  # Redirect to dashboard for non-students
    else:
        # Only staff can view other students' account books
        if not request.user.is_staff:
            return redirect('dashboard')
        student = get_object_or_404(Student, Student_ID=student_id)

    # Get the first and last day of the current month
    today = timezone.now().date()
    first_day = today.replace(day=1)

    if today.month == 12:
        last_day = today.replace(day=31)
    else:
        next_month = today.replace(month=today.month + 1, day=1)
        last_day = next_month - timezone.timedelta(days=1)

    # Get attendance records for the current month
    attendance_records = MessAttendance.objects.filter(
        student=student,
        date__range=[first_day, last_day]
    ).order_by('date')

    total_meals = 0
    total_cost = 0
    attendance_by_date = []

    # Process attendance records by date
    current_date = None
    daily_total = 0
    for record in attendance_records:
        # When the date changes, save the previous day's data
        if current_date and current_date != record.date:
            attendance_by_date.append({'date': current_date, 'daily_total': daily_total})
            daily_total = 0

        current_date = record.date

        # Assuming you have meal rates for each meal type
        breakfast_rate = 200
        lunch_rate = 300
        dinner_rate = 300

        # Calculate meal cost based on the meal type
        if record.meal_time == 'BF':
            meal_cost = breakfast_rate
        elif record.meal_time == 'LN':
            meal_cost = lunch_rate
        elif record.meal_time == 'DN':
            meal_cost = dinner_rate
        else:
            meal_cost = 0  # For any unexpected meal_time values

        # Add meal cost to daily total and accumulate total cost
        daily_total += meal_cost
        total_meals += 1
        total_cost += meal_cost

    # Append the last day's data if there were any records
    if current_date:
        attendance_by_date.append({'date': current_date, 'daily_total': daily_total})

    # Get payment requests for this student and calculate total paid and total due
    payment_requests = MessPaymentRequest.objects.filter(student=student).order_by('-request_date')
    total_paid = sum(payment.amount for payment in payment_requests if payment.status == 'APPROVED')
    total_due = total_cost - total_paid

    # Calculate attendance data to show progress bar and eligibility
    attendance_days = MessAttendance.objects.filter(
        student=student,
        is_present=True,
        date__gte=today - timezone.timedelta(days=30)
    ).values('date').distinct().count()

    # Calculate remaining days until payment eligibility
    days_until_payment = max(0, 5 - attendance_days)

    # Calculate attendance percentage based on attendance days
    attendance_percentage = (attendance_days / 5) * 100 if attendance_days >= 2 else 0

    # Check if the student is eligible for a payment request
    can_request_payment = attendance_days >= 5

    # Pass context data to the template
    context = {
        'student': student,
        'attendance_by_date': attendance_by_date,
        'total_meals': total_meals,
        'total_cost': total_cost,
        'total_paid': total_paid,
        'total_due': total_due,
        'attendance_days': attendance_days,
        'payment_requests': payment_requests,
        'days_until_payment': days_until_payment,
        'attendance_percentage': attendance_percentage,
        'can_request_payment': can_request_payment,  # Add eligibility to the context
    }

    # Render the template with the context data
    return render(request, 'mess_bill_payment/mess_account_book.html', context)



@login_required
def mess_bill(request):
    """
    View to display the mess bill for the current student.
    Shows attendance, bill breakdown, payment requests, and recent payments.
    """
    try:
        # Get the student associated with the current user
        student = Student.objects.get(user=request.user)
        
        # Calculate attendance for the last 30 days
        thirty_days_ago = timezone.now().date() - timedelta(days=30)
        today = timezone.now().date()
        
        # Get attendance records for the student in the last 30 days
        attendance_records = MessAttendance.objects.filter(
            student=student,
            date__gte=thirty_days_ago,
            date__lte=today
        ).order_by('-date')
        
        # Calculate the number of unique days the student has attended
        attendance_days = len(set(record.date for record in attendance_records if record.is_present))
        
        # Organize attendance by date with meal details
        attendance_by_date = []
        dates_processed = set()
        total_cost = Decimal('0.00')
        
        for record in attendance_records:
            if record.date in dates_processed:
                continue
                
            # Get all meals for this date
            day_meals = MessAttendance.objects.filter(
                student=student,
                date=record.date,
                is_present=True
            )
            
            # Create a meal dictionary
            meals = {}
            daily_total = Decimal('0.00')
            
            for meal in day_meals:
                meals[meal.meal_time] = meal.price_charged
                daily_total += meal.price_charged
            
            # Only add days with at least one meal
            if day_meals.exists():
                attendance_by_date.append({
                    'date': record.date,
                    'meals': meals,
                    'daily_total': daily_total
                })
                
                dates_processed.add(record.date)
                total_cost += daily_total
        
        # Get payment requests for this student
        payment_requests = MessPaymentRequest.objects.filter(
            student=student
        ).order_by('-request_date')
        
        # Get recent payments made by this student
        payments = MessPayment.objects.filter(
            student=student
        ).order_by('-payment_date')
        
        # Calculate total due - total cost minus total payments
        total_payments = sum(payment.amount for payment in payments)
        total_due = total_cost - total_payments if total_payments < total_cost else Decimal('0.00')
        
        context = {
            'student': student,
            'attendance_days': attendance_days,
            'attendance_by_date': attendance_by_date,
            'total_cost': total_cost,
            'payment_requests': payment_requests,
            'payments': payments,
            'total_due': total_due
        }
        
        return render(request, 'mess_bill_payment/mess_bill.html', context)
        
    except Student.DoesNotExist:
        messages.error(request, "Student profile not found.")
        return redirect('dashboard')


def is_admin(user):
    """Check if user is an admin or staff"""
    return user.is_staff or user.is_superuser



@login_required
def payment_request_form(request):
    """
    View for students to submit payment requests with proof of payment.
    """
    # Only students can make payment requests
    if not hasattr(request.user, 'student'):
        messages.error(request, "Only students can submit payment requests.")
        return redirect('dashboard')
    
    student = request.user.student
    
    # Calculate attendance days for the last 30 days
    thirty_days_ago = timezone.now().date() - timezone.timedelta(days=30)
    today = timezone.now().date()
    
    attendance_days = MessAttendance.objects.filter(
        student=student,
        date__gte=thirty_days_ago,
        date__lte=today,
        is_present=True
    ).values('date').distinct().count()

    # Check if the student has completed 5 days of attendance
    if attendance_days < 5:
        messages.error(request, "You need to complete at least 5 days of attendance before submitting a payment request.")
        return redirect('mess_bill')

    if request.method == 'POST':
        # Get the amount from the POST data
        amount = request.POST.get('amount')
        payment_method = request.POST.get('payment_method')
        transaction_id = request.POST.get('transaction_id', '')
        screenshot = request.FILES.get('payment_screenshot')
        
        # Check if amount is None or empty string
        if not amount:
            messages.error(request, "Please enter a valid amount.")
            return redirect('payment_request_form')
        
        try:
            # Convert amount to float
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be positive")
            
            # Create payment request
            payment_request = MessPaymentRequest.objects.create(
                student=student,
                amount=amount,
                payment_method=payment_method,
                transaction_id=transaction_id,
                status='PENDING',
                request_date=timezone.now()
            )
            
            # Save payment screenshot if provided
            if screenshot:
                payment_request.payment_screenshot = screenshot
                payment_request.save()
            
            # Get unpaid bills to associate with this payment request
            unpaid_bills = MessBill.objects.filter(
                student=student,
                paid_status=False
            )
            
            # Associate unpaid bills with this payment request
            for bill in unpaid_bills:
                payment_request.bills.add(bill)
            
            # Update milestone days
            payment_request.milestone_days = attendance_days
            payment_request.save()
            
            messages.success(request, "Payment request submitted successfully. Awaiting approval.")
            return redirect('mess_bill')
            
        except ValueError:
            messages.error(request, "Please enter a valid amount.")
            return redirect('payment_request_form')
    
    # Get current month's dues for reference
    today = timezone.now().date()
    first_day = today.replace(day=1)
    
    # Calculate the last day of the current month
    if today.month == 12:
        last_day = today.replace(day=31)
    else:
        next_month = today.replace(month=today.month + 1, day=1)
        last_day = next_month - timezone.timedelta(days=1)
    
    # Calculate current dues from attendance records
    attendance_records = MessAttendance.objects.filter(
        student=student,
        date__range=[first_day, last_day],
        is_present=True
    )
    
    # Calculate total due from attendance records
    total_cost = sum(record.price_charged for record in attendance_records)
    
    # Get approved payments for this month
    approved_payments = MessPaymentRequest.objects.filter(
        student=student,
        request_date__range=[first_day, last_day],
        status='APPROVED'
    )
    
    total_paid = sum(payment.amount for payment in approved_payments)
    current_dues = total_cost - total_paid if total_paid < total_cost else 0
    
    # Calculate attendance for the last 30 days
    attendance_days = MessAttendance.objects.filter(
        student=student,
        date__gte=thirty_days_ago,
        date__lte=today,
        is_present=True
    ).values('date').distinct().count()
    
    # Check if student meets the attendance requirement
    days_until_eligible = max(0, 5 - attendance_days)
    
    context = {
        'student': student,
        'current_dues': current_dues,
        'attendance_days': attendance_days,
        'days_until_eligible': days_until_eligible,
        'is_eligible': attendance_days >= 5,
        'payment_methods': [
            ('CASH', 'Cash'),
            ('BANK_TRANSFER', 'Bank Transfer'),
            ('UPI', 'UPI Payment'),
            ('OTHER', 'Other')
        ]
    }
    
    return render(request, 'mess_bill_payment/payment_request_form.html', context)

from django.db import models

@login_required
@staff_member_required
def admin_payment_requests(request):
    """
    View for admin to manage payment requests
    """
    # Get all payment requests sorted by status and date
    payment_requests = MessPaymentRequest.objects.all().order_by(
        'status', '-request_date'
    )

    # Apply filters if provided
    status_filter = request.GET.get('status', '')
    search_query = request.GET.get('search', '')
    
    if status_filter:
        payment_requests = payment_requests.filter(status=status_filter)
    
    if search_query:
        payment_requests = payment_requests.filter(
            Q(student__F_Name__icontains=search_query) | 
            Q(student__L_Name__icontains=search_query) |
            Q(student__Registration_Number__icontains=search_query)
        )
    
    # Remove duplicates using distinct if needed, based on primary key or specific attributes
    # You can modify this based on your requirement
    payment_requests = payment_requests.distinct('id')

    # Group payment requests by their status
    grouped_requests = {}
    for request_obj in payment_requests:
        status = request_obj.status
        if status not in grouped_requests:
            grouped_requests[status] = []
        grouped_requests[status].append(request_obj)

    context = {
        'grouped_requests': grouped_requests,
        'status_filter': status_filter,
        'search_query': search_query,
    }

    return render(request, 'mess_bill_payment/admin_payment_requests.html', context)



# Helper function to check if user is admin
def is_admin(user):
    """Check if user is an admin or staff"""
    return user.is_staff or user.is_superuser

@login_required
@staff_member_required
def admin_payment_requests(request):
    """
    View for admin to manage payment requests
    """
    # Get all payment requests sorted by status and date
    payment_requests = MessPaymentRequest.objects.all().order_by(
        'status', '-request_date'
    )

    # Apply filters if provided
    status_filter = request.GET.get('status', '')
    search_query = request.GET.get('search', '')
    
    if status_filter:
        payment_requests = payment_requests.filter(status=status_filter)
    
    if search_query:
        payment_requests = payment_requests.filter(
            Q(student__F_Name__icontains=search_query) | 
            Q(student__L_Name__icontains=search_query) |
            Q(student__Registration_Number__icontains=search_query)
        )

    # Group payment requests by their status
    grouped_requests = {}
    for request_obj in payment_requests:
        status = request_obj.status
        if status not in grouped_requests:
            grouped_requests[status] = []
        grouped_requests[status].append(request_obj)

    context = {
        'grouped_requests': grouped_requests,
        'status_filter': status_filter,
        'search_query': search_query,
    }

    return render(request, 'mess_bill_payment/admin_payment_requests.html', context)

@login_required
@user_passes_test(is_admin)
def payment_request_details(request, request_id):
    """
    View detailed information about a payment request
    """
    payment_request = get_object_or_404(MessPaymentRequest, id=request_id)
    
    # Get attendance records for this student
    attendance_records = MessAttendance.objects.filter(
        student=payment_request.student,
        date__gte=payment_request.request_date - timezone.timedelta(days=30),
        date__lte=payment_request.request_date
    ).order_by('-date')
    
    # Get attendance days
    attendance_days = attendance_records.values('date').distinct().count()
    
    # Get meal details
    meal_details = []
    for record in attendance_records.filter(is_present=True):
        meal_details.append({
            'date': record.date,
            'meal_time': record.get_meal_time_display(),
            'price': record.price_charged
        })
    
    context = {
        'payment_request': payment_request,
        'attendance_days': attendance_days,
        'meal_details': meal_details,
    }
    
    return render(request, 'mess_bill_payment/payment_request_details.html', context)

@login_required
@staff_member_required
def process_payment_request(request, request_id):
    payment_request = get_object_or_404(MessPaymentRequest, id=request_id)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        admin_note = request.POST.get('admin_note', '')
        
        if action == 'approve':
            # Approve the payment request
            payment_request.status = 'APPROVED'
            payment_request.processed_date = timezone.now()
            payment_request.admin_note = admin_note
            payment_request.save()

            # Get all unpaid bills for this student
            unpaid_bills = MessBill.objects.filter(
                student=payment_request.student,
                paid_status=False
            ).order_by('bill_date')  # Ensure bills are processed in the order they were created
            
            remaining_amount = payment_request.amount
            
            # Process each bill until the payment amount is exhausted
            for bill in unpaid_bills:
                if remaining_amount <= 0:
                    break
                
                # Get the remaining amount due for this bill
                bill_due = bill.amount_due()
                
                if bill_due > 0:
                    # Determine payment amount for this bill
                    payment_amount = min(remaining_amount, bill_due)
                    
                    # Create a payment record for this specific bill
                    payment = MessPayment.objects.create(
                        student=payment_request.student,
                        bill=bill,  # Associate with this specific bill
                        amount=payment_amount,
                        payment_date=timezone.now(),
                        payment_method=payment_request.payment_method,
                        payment_note=f'Payment request #{payment_request.id} approved. {admin_note}'
                    )
                    
                    # Update bill status if fully paid
                    if payment_amount >= bill_due:
                        bill.paid_status = True
                    
                    # Update remaining amount
                    remaining_amount -= payment_amount
            
            # If there's still remaining amount but no more bills,
            # create a payment with credit to the student's account
            if remaining_amount > 0:
                # Get the oldest bill (paid or unpaid) to associate the payment with
                any_bill = MessBill.objects.filter(
                    student=payment_request.student
                ).order_by('bill_date').first()
                
                if any_bill:
                    MessPayment.objects.create(
                        student=payment_request.student,
                        bill=any_bill,  # We need to associate with some bill
                        amount=remaining_amount,
                        payment_date=timezone.now(),
                        payment_method=payment_request.payment_method,
                        payment_note=f'Payment request #{payment_request.id} approved (credit). {admin_note}'
                    )
            
            messages.success(request, f"Payment request for {payment_request.student} approved successfully.")
            
        elif action == 'reject':
            # Reject the payment request
            payment_request.status = 'REJECTED'
            payment_request.processed_date = timezone.now()
            payment_request.admin_note = admin_note
            payment_request.save()
            
            messages.info(request, f"Payment request for {payment_request.student} rejected.")
        
        return redirect('admin_payment_requests')
    
    # Display the payment request details
    context = {
        'payment_request': payment_request
    }
    
    return render(request, 'mess_bill_payment/process_payment_request.html', context)


@login_required
def student_mess_payment_details(request, student_id):
    """
    View detailed information about a student's mess payment details
    """
    # Get the student object using Student_ID field, not id
    student = get_object_or_404(Student, Student_ID=student_id)
    
    # Get the most recent payment request for this student (if any)
    payment_request = MessPaymentRequest.objects.filter(student=student).order_by('-request_date').first()
    
    if not payment_request:
        messages.warning(request, f"No payment requests found for {student.F_Name} {student.L_Name}")
        # Redirect to an appropriate page if there's no payment request
        return redirect('student_dashboard')  # Adjust this to an appropriate fallback page
    
    # Get attendance records for this student
    attendance_records = MessAttendance.objects.filter(
        student=student,
        date__gte=payment_request.request_date - timezone.timedelta(days=30),
        date__lte=payment_request.request_date
    ).order_by('-date')
    
    # Get attendance days
    attendance_days = attendance_records.values('date').distinct().count()
    
    # Get meal details
    meal_details = []
    for record in attendance_records.filter(is_present=True):
        meal_details.append({
            'date': record.date,
            'meal_time': record.get_meal_time_display(),
            'price': record.price_charged
        })
    
    context = {
        'payment_request': payment_request,
        'student': student,
        'attendance_days': attendance_days,
        'meal_details': meal_details,
    }
    return render(request, 'mess_bill_payment/student_mess_payment_details.html', context)

# ===========================
# Search Management Of Student 
# Search Student 
# ===========================
@login_required
@user_passes_test(lambda u: u.is_staff)

def search_students(request):
    query = request.GET.get('q', '')
    students = []

    if query and len(query) >= 2:
        # Search by name (first name or last name) or registration number
        students = Student.objects.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) | 
            Q(registration_number__icontains=query)
        )[:20]  # Limit to 20 results for performance
        
        students = [
            {
                'id': student.id,
                'full_name': f"{student.first_name} {student.last_name}",
                'registration_number': student.registration_number
            }
            for student in students
        ]
    
    return JsonResponse({'students': students})

    query = request.GET.get('q', '')
    students = []
    
    if query and len(query) >= 2:
        # Search by name (first name or last name) or registration number
        students = Student.objects.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) | 
            Q(registration_number__icontains=query)
        )[:20]  # Limit to 20 results for performance
        
        students = [
            {
                'id': student.id,
                'full_name': f"{student.first_name} {student.last_name}",
                'registration_number': student.registration_number
            }
            for student in students
        ]
    
    return JsonResponse({'students': students})

    """
    Handle AJAX requests to search for students by name or registration number.
    Used by the Select2 widget in the create_showcase_notice form.
    """
    query = request.GET.get('q', '')
    students = []
    
    if query and len(query) >= 2:
        # Search by name (first name or last name) or registration number
        students = Student.objects.filter(
            models.Q(first_name__icontains=query) | 
            models.Q(last_name__icontains=query) | 
            models.Q(registration_number__icontains=query)
        )[:20]  # Limit to 20 results for performance
        
        # Format the results for Select2
        students = [
            {
                'id': student.id,
                'full_name': f"{student.first_name} {student.last_name}",
                'registration_number': student.registration_number
            }
            for student in students
        ]
    
    return JsonResponse({'students': students})

# ===========================
# Finger Print Management Of Student
# enrol finger print
# ===========================


# ==========================
# Hostel Payment System
# Add Payment
# H Student Account Book
# Fee Management
# Stripe PaymnetGateway
# ==========================


# Modified Stripe payment view
@login_required
def add_payment(request):
    """
    View to display add payment form and create Stripe checkout session
    """
    if not hasattr(request.user, 'student'):
        messages.error(request, "You don't have a student profile.")
        return redirect('student_dashboard')
    
    student = request.user.student
    
    # Calculate room fee and total fee
    if hasattr(student, 'room_price') and student.room_price > 0:
        per_installment = student.room_price
    else:
        # Fallback to determine room price
        room = student.Room_ID
        if room:
            if hasattr(room, 'Price') and room.Price > 0:
                per_installment = room.Price
            elif hasattr(room, 'room_type_info') and room.room_type_info and hasattr(room.room_type_info, 'price'):
                per_installment = room.room_type_info.price
            else:
                # Default prices based on room type
                room_type = getattr(room, 'Room_Type', '')
                room_type_prices = {
                    "One Seater": 12000,
                    "Two Seater": 10000,
                    "Three Seater": 9000,
                    "Four Seater": 8000,
                    "Five Seater": 7500,
                    "Six Seater": 7000,
                    "Seven Seater": 6500,
                    "Eight Seater": 6000,
                    "Nine Seater": 5500,
                    "Ten Seater": 5000,
                    # Add default fallback
                    "Default": 5000
                }
                per_installment = room_type_prices.get(room_type, room_type_prices["Default"])
        else:
            per_installment = 5000  # Default if no room assigned
    
    # Total fee is 8 semesters * per_installment fee
    total_fee = per_installment * 8
    
    # Get all payments for this student to calculate paid amount
    payments = student.payments.filter(Fee_Status='PAID')
    total_paid = sum(payment.Amount_Paid for payment in payments)
    
    # Calculate remaining fee
    remaining_fee = total_fee - total_paid
    
    # If no remaining fee, redirect to account book
    if remaining_fee <= 0:
        messages.info(request, "All fees have been paid.")
        return redirect('account_book')
    
    # Find next unpaid semester
    all_payments = student.payments.all().order_by('Installment_Number')
    next_unpaid = None
    
    for payment in all_payments:
        if payment.Fee_Status != 'PAID':
            next_unpaid = payment
            break
    
    # Determine recommended payment amount (next installment or remaining balance)
    recommended_amount = min(per_installment, remaining_fee) if next_unpaid else remaining_fee
    
    if request.method == 'POST':
        amount = request.POST.get('amount')
        try:
            # Convert to float for validation
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be greater than zero")
                
            if amount > remaining_fee:
                raise ValueError(f"Amount cannot be greater than the remaining fee ({remaining_fee})")
                
            # Create a payment intent
            stripe.api_key = settings.STRIPE_SECRET_KEY
            stripe_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'inr',  # Change to your currency
                        'product_data': {
                            'name': f'Hostel Fee Payment - {student.Registration_Number}',
                        },
                        'unit_amount': int(amount * 100),  # Amount in cents
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri(reverse('stripe_success')) + '?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=request.build_absolute_uri(reverse('stripe_cancel')),
                metadata={
                    'student_id': student.Student_ID,
                    'registration_number': student.Registration_Number,
                    'next_unpaid_id': next_unpaid.Payment_ID if next_unpaid else None,  # Fixed: using Payment_ID instead of id
                    'next_semester': next_unpaid.Fee_Type if next_unpaid else None,
                },
            )
            
            # Create a record in StripePayment model - Use the fields actually in the model
            stripe_payment = StripePayment.objects.create(
                student=student,
                amount=amount,
                stripe_payment_intent_id=stripe_session.payment_intent,
                status='PENDING',
                # Store the semester information, not the payment record directly
                semester=next_unpaid.Fee_Type if next_unpaid else None
                # Don't set payment_record here as it will be created in complete_payment
            )
            
            # Redirect to Stripe checkout
            return redirect(stripe_session.url)
            
        except ValueError as e:
            messages.error(request, str(e))
        except stripe.error.StripeError as e:
            messages.error(request, f"Stripe error: {str(e)}")
    
    context = {
        'remaining_fee': remaining_fee,
        'per_installment': per_installment,
        'recommended_amount': recommended_amount,
        'next_semester': next_unpaid.Fee_Type if next_unpaid else "Remaining Balance"
    }
    
    return render(request, 'payment_management/add_payment.html', context)

@login_required
def stripe_success(request):
    """
    Handle successful Stripe payment and display success page
    """
    session_id = request.GET.get('session_id')
    if not session_id:
        messages.error(request, "No payment session found.")
        return redirect('add_payment')
    
    try:
        # Retrieve the session details
        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.retrieve(session_id)
        payment_intent = session.payment_intent
        
        # First try to find by payment intent ID
        stripe_payment = StripePayment.objects.filter(
            stripe_payment_intent_id=payment_intent
        ).first()
        
        # If not found, try to find by student ID from session metadata
        if not stripe_payment and 'student_id' in session.metadata:
            student_id = session.metadata.get('student_id')
            stripe_payment = StripePayment.objects.filter(
                student_id=student_id,
                status='PENDING',
                stripe_payment_intent_id__isnull=True
            ).order_by('-created_at').first()
            
            # If found, update the payment intent ID
            if stripe_payment:
                stripe_payment.stripe_payment_intent_id = payment_intent
                stripe_payment.save()
        
        # Initialize context for the template
        context = {
            'success': False,
            'message': "Payment was processed, but we couldn't find your payment record.",
            'amount': None,
            'receipt_number': None
        }
        
        if stripe_payment:
            # Complete the payment and create a payment record
            try:
                payment = stripe_payment.complete_payment(stripe_payment_intent_id=payment_intent)
                
                # Set success context
                context = {
                    'success': True,
                    'message': "Payment successful!",
                    'amount': stripe_payment.amount,
                    'receipt_number': payment.Receipt_Number,
                    'semester': payment.Fee_Type,
                    'student_name': f"{stripe_payment.student.F_Name} {stripe_payment.student.L_Name}",
                    'registration_number': stripe_payment.student.Registration_Number
                }
                
                # Store success message in session for account_book view
                request.session['payment_success_message'] = f"Payment successful! Receipt number: {payment.Receipt_Number}"
                
                messages.success(request, f"Payment successful! Receipt number: {payment.Receipt_Number}")
                
                # Force refresh of student payment data
                Payment.update_student_fee_status(stripe_payment.student)
                
            except Exception as e:
                context['message'] = f"Error completing payment: {str(e)}"
                messages.error(request, f"Error completing payment: {str(e)}")
                # Log the error for debugging
                print(f"Payment completion error: {str(e)}")
        
        # Use the provided success.html template to show payment success
        return render(request, 'payment_management/success.html', context)
        
    except Exception as e:
        messages.error(request, f"Error processing payment: {str(e)}")
        return redirect('add_payment')   
@login_required
def stripe_cancel(request):
    """
    Handle cancelled Stripe payment
    """
    messages.info(request, "Payment was cancelled.")
    return redirect('add_payment')

@csrf_exempt
def stripe_webhook(request):
    """
    Handle Stripe webhook events
    """
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
        
    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        
        # Get the payment intent ID
        payment_intent_id = session.get('payment_intent')
        
        if payment_intent_id:
            # Find the corresponding stripe payment
            stripe_payment = StripePayment.objects.filter(
                stripe_payment_intent_id=payment_intent_id
            ).first()
            
            # If not found by payment intent, try using metadata
            if not stripe_payment and 'student_id' in session.metadata:
                student_id = session.metadata.get('student_id')
                stripe_payment = StripePayment.objects.filter(
                    student_id=student_id,
                    status='PENDING'
                ).order_by('-created_at').first()
                
                # Update the payment intent ID if found
                if stripe_payment:
                    stripe_payment.stripe_payment_intent_id = payment_intent_id
                    stripe_payment.save()
            
            if stripe_payment and stripe_payment.status == 'PENDING':
                try:
                    # Complete the payment
                    stripe_payment.complete_payment(stripe_payment_intent_id=payment_intent_id)
                except Exception as e:
                    # Log error but return success to Stripe
                    # You should implement proper logging here
                    print(f"Error completing payment via webhook: {str(e)}")
    
    return HttpResponse(status=200)


@login_required
def account_book(request, student_id=None):
    # Get success message from session if available
    success_message = request.session.pop('payment_success_message', None)
    
    # If no student ID is provided and the user is a student, show their own account book
    if student_id is None:
        if hasattr(request.user, 'student'):
            student = request.user.student
        elif request.user.is_staff:
            messages.error(request, "Please select a student to view their account book.")
            return redirect('fee_management')
        else:
            messages.error(request, "You are not authorized to view this page.")
            return redirect('dashboard')
    else:
        # Only staff can view other students' account books
        if not request.user.is_staff:
            messages.error(request, "You are not authorized to view other students' account books.")
            return redirect('dashboard')
        student = get_object_or_404(Student, Student_ID=student_id)
    
    # Get all payments for the student, ordered by semester and payment date
    payments = student.payments.all().order_by('Fee_Type', 'Payment_Date')
    
    # Calculate fee details based on room
    if hasattr(student, 'room_price') and student.room_price > 0:
        per_installment = student.room_price
    else:
        # Fallback to determine room price
        room = student.Room_ID
        if room:
            if hasattr(room, 'Price') and room.Price > 0:
                per_installment = room.Price
            elif hasattr(room, 'room_type_info') and room.room_type_info and hasattr(room.room_type_info, 'price'):
                per_installment = room.room_type_info.price
            else:
                # Default prices based on room type
                room_type_prices = {
                    "One Seater": 12000,
                    "Two Seater": 10000,
                    "Three Seater": 9000,
                    "Four Seater": 8000,
                    "Five Seater": 7500,
                    "Six Seater": 7000,
                    "Seven Seater": 6500,
                    "Eight Seater": 6000,
                    "Nine Seater": 5500,
                    "Ten Seater": 5000,
                    # Add default fallback
                    "Default": 5000
                }
                per_installment = room_type_prices.get(room.Room_Type, room_type_prices["Default"])
        else:
            per_installment = 5000  # Default if no room assigned
    
    # Total fee is 8 semesters * per_installment fee
    total_fee = per_installment * 8
    
    # Get or update student's total_fee field
    if hasattr(student, 'total_fee') and student.total_fee > 0:
        total_fee = student.total_fee
    else:
        # If total_fee field exists but isn't set, update it
        if hasattr(student, 'total_fee'):
            student.total_fee = total_fee
            student.save()
    
    # Calculate total paid amount accurately
    paid_payments = payments.filter(Fee_Status='PAID')
    total_paid = sum(payment.Amount_Paid for payment in paid_payments)
    
    # Count unique paid semesters to handle duplicate payments for the same semester
    paid_semesters = set()
    for payment in paid_payments:
        if payment.Fee_Type:
            paid_semesters.add(payment.Fee_Type)
    
    # Set paid installments count based on unique semesters
    paid_installments = len(paid_semesters)
    
    # Calculate remaining fee
    remaining_fee = total_fee - total_paid
    
    # Generate the expected payments for each semester
    start_year = timezone.now().year
    semesters = []
    for i in range(4):
        semesters.extend([f'Fall-{start_year + i}', f'Spring-{start_year + i + 1}'])
    
    # Format payments for display, handling multiple payments per semester
    semester_payment_map = {}
    
    # First, collect all payments by semester
    for payment in payments:
        semester = payment.Fee_Type
        if semester not in semester_payment_map:
            semester_payment_map[semester] = []
        semester_payment_map[semester].append(payment)
    
    # Create the display list ensuring each semester is represented
    expected_payments = []
    for i, semester in enumerate(semesters[:8], 1):
        # Get all payments for this semester
        semester_payments = semester_payment_map.get(semester, [])
        
        # If no payments, create a placeholder
        if not semester_payments:
            expected_payments.append({
                'challan_no': f'{student.Registration_Number}-{i}',
                'semester': semester,
                'amount': per_installment,
                'status': 'UNPAID',
                'voucher_no': '',
                'payment_date': '',
                'payment_mode': '-'
            })
        else:
            # Add all payments for the semester, most recent first
            for payment in sorted(semester_payments, key=lambda p: p.Payment_Date or timezone.now(), reverse=True):
                expected_payments.append({
                    'challan_no': payment.Receipt_Number or f'{student.Registration_Number}-{i}',
                    'semester': semester,
                    'amount': payment.Amount_Paid,
                    'status': payment.Fee_Status,
                    'voucher_no': payment.Voucher_No or '',
                    'payment_date': payment.Payment_Date.strftime('%Y-%m-%d') if payment.Payment_Date else '',
                    'payment_mode': payment.Payment_Mode or '-'
                })
    
    # Sort payments by semester in chronological order
    expected_payments.sort(key=lambda p: (
        semesters.index(p['semester']) if p['semester'] in semesters else 999,
        p['status'] != 'PAID'  # Show paid first
    ))
    
    # Include any Stripe payments in progress
    stripe_payments = StripePayment.objects.filter(student=student, status='PENDING')
    
    context = {
        'student': student,
        'total_fee': total_fee,
        'per_installment': per_installment,
        'paid_installments': f"{paid_installments}/8",
        'remaining_fee': remaining_fee,
        'payments': expected_payments,
        'stripe_payments': stripe_payments,
        'success_message': success_message
    }
    
    return render(request, 'payment_management/account_book.html', context)

@login_required
def fee_management(request):
    """
    View function to display and manage student fee information.
    Provides search functionality and fee status summaries.
    """
    # Fetch all students with related data to minimize database queries
    students = Student.objects.all().select_related(
        'user', 'Room_ID', 'Hostel_ID', 'Room_ID__room_type_info'
    ).prefetch_related('payments')
    
    # Implement search functionality across multiple fields
    search_query = request.GET.get('search', '')
    if search_query:
        students = students.filter(
            Q(F_Name__icontains=search_query) | 
            Q(L_Name__icontains=search_query) | 
            Q(user__email__icontains=search_query) | 
            Q(Department__icontains=search_query) |
            Q(Registration_Number__icontains=search_query)
        )
    
    # Initialize counters for summary statistics
    total_students = students.count()
    fully_paid = 0
    partially_paid = 0
    not_paid = 0
    total_fees_expected = 0
    total_fees_collected = 0
    
    # Calculate fee status and amounts for each student
    for student in students:
        # Make sure each student has accurate fee status by recalculating
        student.calculate_remaining_fee()
        
        # Update fee status based on payments
        Payment.update_student_fee_status(student)
        
        # Get room price
        room_price = student.get_per_semester_fee()
        
        # Get total fee (should now be updated in the DB)
        total_fee = student.total_fee
        total_fees_expected += total_fee
        
        # Get total paid amount (should now be updated in the DB)
        total_paid = student.total_paid_amount
        total_fees_collected += total_paid
        
        # Calculate remaining fee
        remaining_fee = max(0, total_fee - total_paid)
        
        # Set fee related attributes on student object for template display
        student.room_price_display = room_price
        student.total_fee_display = total_fee
        student.total_paid_display = total_paid
        student.remaining_fee_display = remaining_fee
        
        # Calculate paid installments - FIXED: Only count actual paid installments
        paid_payments = student.payments.filter(Fee_Status='PAID')
        student.paid_installments = paid_payments.count()
        
        # FIXED: Only display the actual number of paid installments, not all payments
        # student.paid_installments_display = f"{paid_payments.count()}/8"
        
        # Map the choice value to display value
        fee_status_mapping = dict(Student.PAYMENT_STATUS_CHOICES)
        student.fee_status_display = fee_status_mapping.get(student.fee_status, student.fee_status)
        
        # Set CSS class based on fee status
        if student.fee_status == 'FULLY_PAID':
            student.status_class = 'status-paid'
            fully_paid += 1
        elif student.fee_status == 'PARTIALLY_PAID':
            student.status_class = 'status-pending' 
            partially_paid += 1
        else:  # NOT_PAID
            student.status_class = 'status-unpaid'
            not_paid += 1
    
    # Apply sorting if requested
    sort_by = request.GET.get('sort', 'name')  # Default sort by name
    if sort_by == 'name':
        students = sorted(students, key=lambda s: f"{s.F_Name} {s.L_Name}")
    elif sort_by == 'fee_status':
        # Sort by payment status priority: NOT_PAID, PARTIALLY_PAID, FULLY_PAID
        status_priority = {'NOT_PAID': 0, 'PARTIALLY_PAID': 1, 'FULLY_PAID': 2}
        students = sorted(students, key=lambda s: status_priority.get(s.fee_status, 0))
    elif sort_by == 'remaining_fee':
        students = sorted(students, key=lambda s: s.remaining_fee_display, reverse=True)
    
    # Calculate fee collection percentage
    collection_percentage = (total_fees_collected / total_fees_expected * 100) if total_fees_expected > 0 else 0
    
    # Return the rendered template with context data
    return render(request, 'payment_management/fee_management.html', {
        'students': students,
        'search_query': search_query,
        'total_students': total_students,
        'fully_paid_count': fully_paid,
        'partially_paid_count': partially_paid,
        'not_paid_count': not_paid,
        'total_fees_expected': total_fees_expected,
        'total_fees_collected': total_fees_collected,
        'collection_percentage': round(collection_percentage, 2),
        'sort_by': sort_by
    })

def save(self, *args, **kwargs):
    """
    Generate Voucher number only for PAID payments and update the student's fee status.
    """
    # For paid payments, ensure voucher number and payment date
    if self.Fee_Status == 'PAID':
        if not self.Voucher_No or self.Voucher_No is None:
            # Generate voucher number for paid payments
            self.Voucher_No = f'STRIPE-{self.Student_ID.Registration_Number}-{self.Installment_Number}'
            
        # Ensure payment date exists
        if not self.Payment_Date:
            self.Payment_Date = timezone.now()
    
    super().save(*args, **kwargs)
    
    # Update student's payment information and status
    self.update_student_payment_info()
    
    # ADDED: Clear any cached display elements that might cause inconsistency
    if hasattr(self.Student_ID, 'paid_installments'):
        delattr(self.Student_ID, 'paid_installments')
    if hasattr(self.Student_ID, 'status_class'):
        delattr(self.Student_ID, 'status_class')

def _get_room_price(student):
    """
    Utility function to get room price for the student.
    """
    if hasattr(student, 'room_price') and student.room_price > 0:
        return student.room_price
    else:
        room = student.Room_ID
        if room:
            if hasattr(room, 'Price') and room.Price > 0:
                return room.Price
            elif hasattr(room, 'room_type_info') and room.room_type_info:
                return room.room_type_info.price
        return 5000  # Default room price if no specific price is available




    """
    Helper function to determine room price for a student.
    Returns the room price per semester based on available data.
    """
    # Check if student has room_price field set
    if hasattr(student, 'room_price') and student.room_price > 0:
        return float(student.room_price)
    
    # Check if student is assigned to a room
    if student.Room_ID:
        room = student.Room_ID
        
        # Try to get price directly from Room
        if hasattr(room, 'Price') and room.Price > 0:
            return float(room.Price)
        
        # Try to get price from room_type_info
        if hasattr(room, 'room_type_info') and room.room_type_info and hasattr(room.room_type_info, 'price'):
            return float(room.room_type_info.price)
        
        # Fallback to room type prices dictionary
        room_type_prices = {
            "One Seater": 12000,
            "Two Seater": 10000,
            "Three Seater": 9000,
            "Four Seater": 8000,
            "Five Seater": 7500,
            "Six Seater": 7000,
            "Seven Seater": 6500,
            "Eight Seater": 6000,
            "Nine Seater": 5500,
            "Ten Seater": 5000,
            "Default": 5000
        }
        return float(room_type_prices.get(room.Room_Type, room_type_prices["Default"]))
    
    # Default price if no room assigned
    return 5000.0
    # Fetch all students along with their payments, room, and hostel info
    students = Student.objects.all().prefetch_related('payments', 'Room_ID', 'Hostel_ID')
    
    # Implement search functionality based on multiple fields
    search_query = request.GET.get('search', '')
    if search_query:
        students = students.filter(
            Q(F_Name__icontains=search_query) | 
            Q(L_Name__icontains=search_query) | 
            Q(user__email__icontains=search_query) | 
            Q(Department__icontains=search_query) |
            Q(Registration_Number__icontains=search_query)
        )
    
    # Calculate fee status and amounts for each student
    for student in students:
        # Get room price
        if hasattr(student, 'room_price') and student.room_price > 0:
            room_price = student.room_price
        elif student.Room_ID:
            room = student.Room_ID
            if hasattr(room, 'Price') and room.Price > 0:
                room_price = room.Price
            elif hasattr(room, 'room_type_info') and room.room_type_info:
                room_price = room.room_type_info.price
            else:
                room_type_prices = {
                    "One Seater": 12000,
                    "Two Seater": 10000,
                    "Three Seater": 9000,
                    "Four Seater": 8000,
                    "Five Seater": 7500,
                    "Six Seater": 7000,
                    "Seven Seater": 6500,
                    "Eight Seater": 6000,
                    "Nine Seater": 5500,
                    "Ten Seater": 5000,
                    "Default": 5000
                }
                room_price = room_type_prices.get(room.Room_Type, room_type_prices["Default"])
        else:
            room_price = 5000
            
        # Calculate total fee (8 semesters)
        total_fee = room_price * 8
        
        # Calculate total paid amount
        paid_payments = student.payments.filter(Fee_Status='PAID')
        total_paid = sum(payment.Amount_Paid for payment in paid_payments)
        
        # Set fee related attributes on student
        student.room_price_display = room_price
        student.total_fee_display = total_fee
        student.total_paid_display = total_paid
        student.remaining_fee_display = total_fee - total_paid
        
        # Update fee status display
        if total_paid >= total_fee:
            student.fee_status_display = 'FULLY_PAID'
            student.status_class = 'status-paid'
        elif total_paid > 0:
            student.fee_status_display = 'PARTIALLY_PAID'
            student.status_class = 'status-pending'
        else:
            student.fee_status_display = 'NOT_PAID'
            student.status_class = 'status-unpaid'
        
        # Count paid installments
        student.paid_installments = paid_payments.count()
    
    # Calculate summary statistics
    total_students = students.count()
    fully_paid = sum(1 for student in students if student.fee_status_display == 'FULLY_PAID')
    partially_paid = sum(1 for student in students if student.fee_status_display == 'PARTIALLY_PAID')
    not_paid = sum(1 for student in students if student.fee_status_display == 'NOT_PAID')
    
    # Return the fee management view with students and search query
    return render(request, 'payment_management/fee_management.html', {
        'students': students,
        'search_query': search_query,
        'total_students': total_students,
        'fully_paid_count': fully_paid,
        'partially_paid_count': partially_paid,
        'not_paid_count': not_paid
    })
    
    
    
    # For fingerprint enrollment



from base64 import b64decode

@login_required
def enroll_fingerprint(request):
    """View for already approved members to enroll or update their fingerprint"""
    
    # Check if the student has a mess membership
    try:
        membership = MessMembership.objects.get(
            student=request.user.student,
            approved=True
        )
    except MessMembership.DoesNotExist:
        messages.error(request, "You must have an approved mess membership to enroll your fingerprint.")
        return redirect('apply_for_mess')
    
    # Check current fingerprint status
    try:
        fingerprint = Fingerprint.objects.get(student=request.user.student)
        fingerprint_exists = True
        fingerprint_date = fingerprint.created_at
    except Fingerprint.DoesNotExist:
        fingerprint_exists = False
        fingerprint_date = None
    
    if request.method == 'POST':
        fingerprint_data = request.POST.get('fingerprint_data')
        
        if fingerprint_data:
            try:
                # Decode base64 data if the fingerprint data is in base64 format
                fingerprint_binary_data = b64decode(fingerprint_data)
                
                # Create or update fingerprint record
                fingerprint, created = Fingerprint.objects.update_or_create(
                    student=request.user.student,
                    defaults={'fingerprint_template': fingerprint_binary_data}
                )
                
                # Link fingerprint to the student's mess membership if not already linked
                if membership.fingerprint is None:
                    membership.fingerprint = fingerprint
                    membership.save()
                
                messages.success(request, "Fingerprint successfully enrolled!")
                return redirect('mess_status')
            except Exception as e:
                messages.error(request, f"Error enrolling fingerprint: {str(e)}")
        else:
            messages.error(request, "No fingerprint data received. Please scan your fingerprint.")
    
    context = {
        'membership': membership,
        'fingerprint_exists': fingerprint_exists,
        'fingerprint_date': fingerprint_date,
    }
    
    return render(request, 'mess_management/enroll_fingerprint.html', context)


# For fingerprint-based attendance marking
@staff_member_required
def fingerprint_attendance(request):
    """View for staff to mark student attendance using fingerprints"""
    if request.method == 'POST':
        try:
            # Import the digitalpersona library inside the function
            import digitalpersona
            
            # Initialize the fingerprint device
            fingerprint_device = digitalpersona.Device()
            
            # Capture fingerprint for verification
            capture_data = fingerprint_device.capture()
            
            if not capture_data:
                messages.error(request, "Failed to capture fingerprint. Please try again.")
                return redirect('fingerprint_attendance')
            
            # Get meal time from form
            meal_time = request.POST.get('meal_time')
            if not meal_time:
                messages.error(request, "Please select a meal time.")
                return redirect('fingerprint_attendance')
            
            # Identify the student by matching fingerprint
            found_student = None
            found_fingerprint = None
            
            # Get all fingerprints and try to match
            fingerprints = Fingerprint.objects.all()
            for fingerprint in fingerprints:
                # Use digitalpersona to verify fingerprint match
                match_result = digitalpersona.verify(fingerprint.fingerprint_template, capture_data)
                if match_result:
                    found_fingerprint = fingerprint
                    found_student = fingerprint.student
                    break
            
            if not found_student:
                messages.error(request, "No matching fingerprint found. Please try again or enroll this fingerprint.")
                return redirect('fingerprint_attendance')
            
            # Check if student is an approved mess member
            membership = MessMembership.objects.filter(
                student=found_student,
                approved=True,
                is_active=True
            ).first()
            
            if not membership:
                messages.error(request, f"Student {found_student.F_Name} {found_student.L_Name} is not an active mess member.")
                return redirect('fingerprint_attendance')
            
            # Check if attendance for this meal has already been marked today
            today = timezone.now().date()
            existing_attendance = MessAttendance.objects.filter(
                student=found_student,
                date=today,
                meal_time=meal_time
            ).exists()
            
            if existing_attendance:
                messages.warning(request, f"{found_student.F_Name} {found_student.L_Name} has already marked attendance for this meal today.")
                return redirect('fingerprint_attendance')
            
            # Get current meal price from menu
            menu_item = MessMenu.objects.filter(meal_time=meal_time, date=today).first()
            price = menu_item.price if menu_item else 0
            
            # Create attendance record
            MessAttendance.objects.create(
                student=found_student,
                date=today,
                meal_time=meal_time,
                is_present=True,
                price_charged=price
            )
            
            messages.success(request, f"Attendance for {found_student.F_Name} {found_student.L_Name} marked successfully for {dict(MessMenu.MEAL_CHOICES)[meal_time]}!")
        
        except ImportError:
            messages.error(request, "Fingerprint system is not available. Please contact the administrator.")
        except Exception as e:
            messages.error(request, f"Error processing fingerprint: {str(e)}")
    
    # Get all meal times for the form
    meal_times = [
        {'code': 'BF', 'name': 'Breakfast'},
        {'code': 'LN', 'name': 'Lunch'},
        {'code': 'ET', 'name': 'Evening Tea'},
        {'code': 'DN', 'name': 'Dinner'}
    ]
    
    return render(request, 'mess_bill_payment/fingerprint_attendance.html', {'meal_times': meal_times})

@login_required
def fingerprint_status(request):
    student = request.user.student
    
    # Check if student has a fingerprint enrolled
    try:
        fingerprint = Fingerprint.objects.get(student=student)
        fingerprint_enrolled = True
        enrollment_date = fingerprint.created_at
    except Fingerprint.DoesNotExist:
        fingerprint_enrolled = False
        enrollment_date = None
    
    # Check mess membership status
    try:
        membership = MessMembership.objects.get(
            student=student,
            approved=True,
            is_active=True
        )
        has_membership = True
    except MessMembership.DoesNotExist:
        has_membership = False
    
    context = {
        'fingerprint_enrolled': fingerprint_enrolled,
        'enrollment_date': enrollment_date,
        'has_membership': has_membership
    }
    
    return render(request, 'mess_bill_payment/fingerprint_status.html', context)
