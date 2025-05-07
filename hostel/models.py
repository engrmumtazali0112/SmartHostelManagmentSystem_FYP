from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import datetime
import stripe

# ==========================
# Hostel Model
# ==========================

class Hostel(models.Model):
    Hostel_ID = models.AutoField(primary_key=True)
    Hostel_Name = models.CharField(max_length=255, unique=True)
    No_Of_Rooms = models.IntegerField(default=0)
    No_Of_Students = models.IntegerField(default=0)
    # Dynamic room capacity fields (1-10 seaters)
    One_Seater_Rooms = models.IntegerField(default=0)
    Two_Seater_Rooms = models.IntegerField(default=0)
    Three_Seater_Rooms = models.IntegerField(default=0)
    Four_Seater_Rooms = models.IntegerField(default=0)
    Five_Seater_Rooms = models.IntegerField(default=0)
    Six_Seater_Rooms = models.IntegerField(default=0)
    Seven_Seater_Rooms = models.IntegerField(default=0)
    Eight_Seater_Rooms = models.IntegerField(default=0)
    Nine_Seater_Rooms = models.IntegerField(default=0)
    Ten_Seater_Rooms = models.IntegerField(default=0)
    
    # Room prices for each type
    One_Seater_Price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Two_Seater_Price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Three_Seater_Price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Four_Seater_Price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Five_Seater_Price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Six_Seater_Price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Seven_Seater_Price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Eight_Seater_Price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Nine_Seater_Price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Ten_Seater_Price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def total_rooms(self):
        return (self.One_Seater_Rooms + self.Two_Seater_Rooms + 
                self.Three_Seater_Rooms + self.Four_Seater_Rooms + 
                self.Five_Seater_Rooms + self.Six_Seater_Rooms + 
                self.Seven_Seater_Rooms + self.Eight_Seater_Rooms + 
                self.Nine_Seater_Rooms + self.Ten_Seater_Rooms)

    def total_price(self):
        """ Method to calculate the total price for all rooms based on their room count and price """
        return {
            'One_Seater': self.One_Seater_Rooms * self.One_Seater_Price,
            'Two_Seater': self.Two_Seater_Rooms * self.Two_Seater_Price,
            'Three_Seater': self.Three_Seater_Rooms * self.Three_Seater_Price,
            'Four_Seater': self.Four_Seater_Rooms * self.Four_Seater_Price,
            'Five_Seater': self.Five_Seater_Rooms * self.Five_Seater_Price,
            'Six_Seater': self.Six_Seater_Rooms * self.Six_Seater_Price,
            'Seven_Seater': self.Seven_Seater_Rooms * self.Seven_Seater_Price,
            'Eight_Seater': self.Eight_Seater_Rooms * self.Eight_Seater_Price,
            'Nine_Seater': self.Nine_Seater_Rooms * self.Nine_Seater_Price,
            'Ten_Seater': self.Ten_Seater_Rooms * self.Ten_Seater_Price
        }

    def save(self, *args, **kwargs):
        """
        Override save method to ensure that the number of students in the hostel is at least 300.
        """
        if self.No_Of_Students < 300:
            raise ValidationError("Number of students must be at least 300.")
        if self.No_Of_Rooms != self.total_rooms():
            raise ValidationError("The total number of rooms must match the sum of individual room types.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Hostel_Name

# ==========================
# Room Model
# ==========================

class Room(models.Model):
    Room_ID = models.AutoField(primary_key=True)
    Room_Type = models.CharField(max_length=20)
    Capacity = models.IntegerField()
    Location = models.CharField(max_length=100)
    Room_No = models.CharField(max_length=10, unique=True)
    Floor_No = models.IntegerField()
    Students_Alloted = models.IntegerField(default=0)
    Hostel_ID = models.ForeignKey('Hostel', on_delete=models.CASCADE)
    room_type_info = models.ForeignKey('RoomType', on_delete=models.SET_NULL, null=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Add price field with default value 0
    is_available = models.BooleanField(default=True)  # Room availability status

    def __str__(self):
        return f"{self.Room_No} - {self.Room_Type}"

    @property
    def remaining_capacity(self):
        """ Returns the remaining capacity of the room. """
        return self.Capacity - self.Students_Alloted

class RoomType(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=20, unique=True)
    capacity = models.IntegerField()
    price = models.IntegerField(default=0)  # Price for the room type

    def __str__(self):
        return self.type_name

# ==========================
# Student Model
# ==========================

class Student(models.Model):
    Room_ID = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, related_name="students")
    Hostel_ID = models.ForeignKey(Hostel, on_delete=models.SET_NULL, null=True)
    
    PAYMENT_STATUS_CHOICES = [
        ('NOT_PAID', 'Not Paid'),
        ('PARTIALLY_PAID', 'Partially Paid'),
        ('FULLY_PAID', 'Fully Paid'),
    ]
    
    Student_ID = models.AutoField(primary_key=True)
    Registration_Number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile_picture = models.ImageField(upload_to='student_profiles/', null=True, blank=True)
    
    F_Name = models.CharField(max_length=50)
    L_Name = models.CharField(max_length=50)
    Contact_Info = models.CharField(max_length=100)
    Address = models.TextField()
    Department = models.CharField(max_length=100)
    FatherName = models.CharField(max_length=50)
    fee_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='NOT_PAID')
    
    total_paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    room_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Added for storing total fee
    paid_installment_count = models.IntegerField(default=0)  # Added missing field
    
    def update_fee_status(self):
        """
        Update the fee status of the student based on the total paid amount.
        """
        # Ensure we're working with the latest data
        total_paid = self.total_paid_amount
        total_fee = self.total_fee
        
        # If total_fee is not set, calculate it
        if not total_fee or total_fee == 0:
            per_semester_fee = self.get_per_semester_fee()
            total_fee = per_semester_fee * 8
            self.total_fee = total_fee

        # Update fee status based on payment amount
        if total_paid == 0:
            self.fee_status = 'NOT_PAID'
        elif total_paid < total_fee:
            self.fee_status = 'PARTIALLY_PAID'
        else:
            self.fee_status = 'FULLY_PAID'
            
        # Only update fee_status field to avoid race conditions
        self.save(update_fields=['fee_status', 'total_fee'])
    
    def calculate_remaining_fee(self):
        """
        Calculate the remaining fee to be paid based on room price and payment history.
        Returns the remaining amount to be paid by the student.
        """
        # Get room price (per semester)
        per_installment = self.get_per_semester_fee()
        
        # Total fee is 8 semesters * per_installment fee
        total_fee = per_installment * 8
        
        # Update the total_fee field if we have a new value
        if self.total_fee != total_fee:
            self.total_fee = total_fee
            self.save(update_fields=['total_fee'])
        
        # Calculate total paid amount from payment records - ensure we get fresh data
        paid_payments = self.payments.filter(Fee_Status='PAID')
        total_paid = sum(float(payment.Amount_Paid) for payment in paid_payments)
        
        # Calculate the number of paid installments
        self.paid_installment_count = len(paid_payments)
        
        # Update the total_paid_amount field if it doesn't match
        if self.total_paid_amount != total_paid:
            self.total_paid_amount = total_paid
            self.save(update_fields=['total_paid_amount', 'paid_installment_count'])
            
            # Update fee status based on new payment info
            self.update_fee_status()
        
        # Return the remaining fee (never less than zero)
        return max(0, total_fee - total_paid)
    
    def get_per_semester_fee(self):
        """
        Get the fee amount per semester based on room price or room type.
        """
        # First check if we have a stored room_price
        if hasattr(self, 'room_price') and self.room_price > 0:
            return float(self.room_price)
            
        # If not, try to get from Room
        elif self.Room_ID:
            # Try to get price directly from Room
            if hasattr(self.Room_ID, 'Price') and self.Room_ID.Price and self.Room_ID.Price > 0:
                return float(self.Room_ID.Price)
                
            # Fall back to room_type_info
            elif hasattr(self.Room_ID, 'room_type_info') and self.Room_ID.room_type_info:
                return float(self.Room_ID.room_type_info.price)
                
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
                    "Default": 5000
                }
                return float(room_type_prices.get(self.Room_ID.Room_Type, room_type_prices["Default"]))
        return 5000.0  # Default if no room assigned

# ==========================
# Admin Model
# ==========================

class Admin(models.Model):
    Admin_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Password = models.CharField(max_length=128)
    Email = models.EmailField()
    Contact_Information = models.CharField(max_length=255)
    Admin_Role = models.CharField(max_length=100)
    Created_At = models.DateTimeField(auto_now_add=True)
    Updated_At = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name

# ==========================
# AdminRole Model (For Admin roles and permissions)
# ==========================

class AdminRole(models.Model):
    ROLE_CHOICES = [
        ('superuser', 'Superuser - Full System Access'),
        ('staff', 'Staff - Limited Administrative Access'),
        ('manager', 'Manager - Intermediate Administrative Access')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    # Contact Information
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', 
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    
    # Additional fields specific to admin
    department = models.CharField(max_length=100, blank=True)
    hire_date = models.DateField(null=True, blank=True)
    
    # Permissions tracking
    can_manage_users = models.BooleanField(default=False)
    can_manage_system = models.BooleanField(default=False)
    can_view_reports = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"

    def get_permissions(self):
        
        permissions = {
            'superuser': {
                'can_manage_users': True,
                'can_manage_system': True,
                'can_view_reports': True,
                'access_level': 3
            },
            'staff': {
                'can_manage_users': False,
                'can_manage_system': False,
                'can_view_reports': True,
                'access_level': 2
            },
            'manager': {
                'can_manage_users': True,
                'can_manage_system': False,
                'can_view_reports': True,
                'access_level': 1
            }
        }
        return permissions.get(self.role, {})

# ==========================
# NoticeBoard Model
# ==========================

class NoticeBoard(models.Model):
    Notice_ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Content = models.TextField()
    Created_At = models.DateTimeField(auto_now_add=True)
    Expiry_Date = models.DateTimeField(null=True, blank=True)
    Admin_ID = models.ForeignKey(Admin, on_delete=models.CASCADE)
    Is_Active = models.BooleanField(default=True)

    def __str__(self):
        return self.Title


# ==========================
# ShowcaseNotice Model
# ==========================

class ShowcaseNotice(models.Model):
    NOTICE_TYPES = (
        ('noise', 'Noise Complaint'),
        ('fine', 'Fine'),
        ('damage', 'Property Damage'),
        ('conduct', 'Misconduct'),
        ('other', 'Other'),
    )
    
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    notice_type = models.CharField(max_length=20, choices=NOTICE_TYPES)
    created_date = models.DateTimeField(default=timezone.now)
    fine_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    resolved = models.BooleanField(default=False)
    registration_number = models.CharField(max_length=100, unique=True, null=True, blank=True)
    students = models.ManyToManyField('Student', through='StudentShowcaseNotice', related_name='showcase_notices')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_showcase_notices')
    
    def save(self, *args, **kwargs):
        if not self.title:
            self.title = f"{self.get_notice_type_display()} - {timezone.now().strftime('%Y-%m-%d')}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class StudentShowcaseNotice(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    notice = models.ForeignKey(ShowcaseNotice, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    read_date = models.DateTimeField(null=True, blank=True)
    paid = models.BooleanField(default=False)  # Added Paid status
  
    def mark_as_read(self):
        self.read = True
        self.read_date = timezone.now()
        self.save()

    def mark_as_paid(self):
        self.paid = True
        self.save()

    class Meta:
        unique_together = ('student', 'notice')

# ==========================
# Visitor Model
# Visitor Request Model
# ==========================

class Visitor(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    visit_date = models.DateTimeField(default=timezone.now)
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='visitors')
    Visitor_ID_Proof = models.CharField(max_length=50, help_text="ID card number or other identification")
    purpose_of_visit = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class VisitorRequest(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='visitor_requests')
    visitor = models.ForeignKey('Visitor', on_delete=models.CASCADE, related_name='requests')
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')], default='PENDING')
    is_read = models.BooleanField(default=False)
    time_in = models.DateTimeField(null=True, blank=True)
    time_out = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Request for {self.visitor.name} by {self.student.F_Name} {self.student.L_Name}"

# ==========================
# Payment Model
# ==========================

class Payment(models.Model):
    pdf_file = models.FileField(upload_to='payments_pdfs/', null=True, blank=True)
    PAYMENT_STATUS_CHOICES = [
        ('PAID', 'Paid'),
        ('UNPAID', 'Unpaid'),
        ('PENDING', 'Pending')
    ]
    PAYMENT_MODE_CHOICES = [
        ('CASH', 'Cash'),
        ('ONLINE', 'Online'),
        ('BANK', 'Bank')
    ]
    
    Payment_ID = models.AutoField(primary_key=True)
    Student_ID = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='payments')
    Fee_Type = models.CharField(max_length=255)
    Amount_Due = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Payment_Date = models.DateTimeField(null=True, blank=True)
    Due_Date = models.DateTimeField(null=True, blank=True)
    Amount_Paid = models.DecimalField(max_digits=10, decimal_places=2)
    Receipt_Number = models.CharField(max_length=255)
    Fee_Status = models.CharField(max_length=50, choices=PAYMENT_STATUS_CHOICES, default='UNPAID')
    Voucher_No = models.CharField(max_length=255, null=True, blank=True)
    Payment_Mode = models.CharField(max_length=50, choices=PAYMENT_MODE_CHOICES, null=True, blank=True)
    Installment_Number = models.IntegerField(null=True, blank=True)
    
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
    
    def update_student_payment_info(self):
        """Update student's payment information and fee status"""
        student = self.Student_ID
        
        # Calculate the total amount paid by the student
        total_paid = Payment.objects.filter(
            Student_ID=student,
            Fee_Status='PAID'
        ).aggregate(total=models.Sum('Amount_Paid'))['total'] or 0
        
        # Update student's total_paid_amount
        student.total_paid_amount = total_paid
        
        # Calculate total fee
        if hasattr(student, 'total_fee') and student.total_fee > 0:
            total_fee = student.total_fee
        else:
            # Calculate if not set
            per_installment = student.get_per_semester_fee()
            total_fee = per_installment * 8
            student.total_fee = total_fee
        
        # Calculate how many full installments have been paid
        per_installment = total_fee / 8
        paid_installments = min(8, int(total_paid / per_installment))
        
        # Store the paid installments count for display purposes
        student.paid_installment_count = paid_installments
        
        # Update student's fee status
        if total_paid == 0:
            student.fee_status = 'NOT_PAID'
        elif total_paid < total_fee:
            student.fee_status = 'PARTIALLY_PAID'
        else:
            student.fee_status = 'FULLY_PAID'
        
        # Save with only the necessary fields
        if hasattr(student, 'paid_installment_count'):
            student.save(update_fields=['fee_status', 'total_paid_amount', 'total_fee', 'paid_installment_count'])
        else:
            student.save(update_fields=['fee_status', 'total_paid_amount', 'total_fee'])
    
    @staticmethod
    def update_student_fee_status(student):
        """Update student fee status based on payments"""
        # Calculate total paid amount
        total_paid = student.payments.filter(Fee_Status='PAID').aggregate(
            total=models.Sum('Amount_Paid'))['total'] or 0
        
        # Get or calculate total fee
        if hasattr(student, 'total_fee') and student.total_fee > 0:
            total_fee = student.total_fee
        else:
            per_installment = student.get_per_semester_fee()
            total_fee = per_installment * 8
            student.total_fee = total_fee
        
        # Update student's total_paid_amount
        student.total_paid_amount = total_paid
        
        # Calculate how many full installments have been paid
        per_installment = total_fee / 8
        paid_installments = min(8, int(total_paid / per_installment))
        
        # Store the paid installments count for display purposes
        student.paid_installment_count = paid_installments
        
        # Update fee status based on payment
        if total_paid == 0:
            student.fee_status = 'NOT_PAID'
        elif total_paid < total_fee:
            student.fee_status = 'PARTIALLY_PAID'
        else:
            student.fee_status = 'FULLY_PAID'
        
        # Save with the necessary fields including paid_installment_count
        if hasattr(Student, 'paid_installment_count'):
            student.save(update_fields=['fee_status', 'total_paid_amount', 'total_fee', 'paid_installment_count'])
        else:
            student.save(update_fields=['fee_status', 'total_paid_amount', 'total_fee'])
    
    @classmethod
    def process_payment(cls, payment_id, amount, payment_mode='ONLINE'):
       
        try:
            payment = cls.objects.get(Payment_ID=payment_id)
            
            payment.Amount_Paid = amount
            payment.Fee_Status = 'PAID'
            payment.Payment_Mode = payment_mode
            payment.Payment_Date = timezone.now()
            payment.save()  # This will trigger the save method which updates student info
            
            # Explicitly update the student model to ensure proper counting
            student = payment.Student_ID
            
            # Count actual paid installments instead of relying on calculations
            paid_count = student.payments.filter(Fee_Status='PAID').count()
            if hasattr(student, 'paid_installment_count'):
                student.paid_installment_count = paid_count
                student.save(update_fields=['paid_installment_count'])
            
            return True, "Payment processed successfully"
        except cls.DoesNotExist:
            return False, "Payment record not found"


# ==========================
# Profile Model (For User Profile)
# ==========================

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username

# ==========================
# Complaint Model (For Complaints)
# ==========================

class Complaint(models.Model):
    Complaint_ID = models.AutoField(primary_key=True)
    Student_ID = models.ForeignKey('Student', on_delete=models.CASCADE)
    Admin_ID = models.ForeignKey('Admin', on_delete=models.CASCADE)
    Complaint_Description = models.TextField()
    Complaint_Type = models.CharField(max_length=255)
    Created_At = models.DateTimeField(auto_now_add=True)
    Updated_At = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False)  # Track if complaint is read
    
    def __str__(self):
        return f"Complaint {self.Complaint_ID}"


# ==========================
# Finger Print Membership Model
# ==========================

# Define the Fingerprint model before MessMembership
class Fingerprint(models.Model):
    student = models.OneToOneField('Student', on_delete=models.CASCADE)
    fingerprint_template = models.BinaryField()  # Store the fingerprint data as binary data
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"Fingerprint for {self.student.F_Name} {self.student.L_Name}"

# ==========================
# Mess Membership Model
# ==========================

class MessMembership(models.Model):
    student = models.OneToOneField('Student', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    fingerprint = models.OneToOneField(Fingerprint, on_delete=models.SET_NULL, null=True, blank=True, related_name='membership')
    department = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    fingerprint = models.OneToOneField(Fingerprint, on_delete=models.SET_NULL, null=True, blank=True)  # Refer to Fingerprint here
    date_applied = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="Pending", choices=[
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected")
    ])  

    def __str__(self):
        return f"{self.student.F_Name} {self.student.L_Name} Mess Membership"

class MessRequest(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)  # Tracks if the request has been read
    description = models.TextField()  # Description or details of the mess request
    
    def __str__(self):
        return f"Mess Request by {self.student.full_name} on {self.request_date}"
    
    from django.db import models

# ==========================
# Mess Menu Model
# ==========================


class MessMenu(models.Model):
    # Meal time choices
    BREAKFAST = 'BF'
    LUNCH = 'LN'
    EVENING_TEA = 'ET'
    DINNER = 'DN'
    
    MEAL_CHOICES = [
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (EVENING_TEA, 'Evening Tea/Squash'),
        (DINNER, 'Dinner'),
    ]
    
    # Days of the week for easier filtering
    MONDAY = 'MON'
    TUESDAY = 'TUE'
    WEDNESDAY = 'WED'
    THURSDAY = 'THU'
    FRIDAY = 'FRI'
    SATURDAY = 'SAT'
    SUNDAY = 'SUN'
    
    DAY_CHOICES = [
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    ]
    
    # Fields in the model
    date = models.DateField()
    day = models.CharField(max_length=3, choices=DAY_CHOICES, blank=True)
    meal_time = models.CharField(max_length=2, choices=MEAL_CHOICES)
    dish_name = models.TextField()  # TextField to accommodate multiple dishes
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    # Fields for easy organization
    week_number = models.IntegerField(blank=True, null=True)
    month = models.CharField(max_length=20, blank=True)
    year = models.IntegerField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        # Auto-populate the 'day' field based on the 'date' field
        if self.date and not self.day:
            self.day = self.date.strftime('%a').upper()[:3]
        
        # Auto-populate month and year if not provided
        if self.date and (not self.month or not self.year):
            self.month = self.date.strftime('%B')
            self.year = self.date.year
            self.week_number = self.date.isocalendar()[1]
            
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.get_meal_time_display()} on {self.date.strftime('%A')}: {self.dish_name[:30]}..."
    
    class Meta:
        # Order by date and meal time
        ordering = ['date', 'meal_time']
        # Add indexes to optimize queries for date and meal time
        indexes = [
            models.Index(fields=['date']),
            models.Index(fields=['meal_time']),
            models.Index(fields=['month', 'year']),
        ]


# ==========================
# Mess Attandance Model
# ==========================

class MessAttendance(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    meal_time = models.CharField(max_length=2, choices=MessMenu.MEAL_CHOICES)
    is_present = models.BooleanField()
    price_charged = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    
    def __str__(self):
        return f"{self.student.F_Name} {self.student.L_Name} - {self.date} - {self.get_meal_time_display()} - {'Present' if self.is_present else 'Absent'}"
        
    def save(self, *args, **kwargs):
        if self.is_present:
            # Fetch the meal price for the given date and meal time
            menu_item = MessMenu.objects.filter(date=self.date, meal_time=self.meal_time).first()
            if menu_item:
                self.price_charged = menu_item.price
        super().save(*args, **kwargs)
        
        # After saving, check if student has completed 5 days of attendance (changed from 10)
        self.check_attendance_milestone()
    
    def check_attendance_milestone(self):
        # Count the number of unique days with attendance in the last 30 days
        today = timezone.now().date()
        thirty_days_ago = today - timezone.timedelta(days=30)
        
        # Get distinct dates where the student was present for at least one meal
        attendance_days = MessAttendance.objects.filter(
            student=self.student,
            date__gte=thirty_days_ago,
            date__lte=today,
            is_present=True
        ).values('date').distinct()
        
        # Count the number of unique days
        days_count = attendance_days.count()
        
        # If exactly 5 days completed (changed from 10), create payment request and process with Stripe
        if days_count == 5:
            # Check if payment request already exists for this milestone
            existing_request = MessPaymentRequest.objects.filter(
                student=self.student,
                status='PENDING',
                milestone_days=5  # Changed from 10 to 5
            ).exists()
            
            # Get unpaid bills
            unpaid_bills = MessBill.objects.filter(
                student=self.student,
                paid_status=False
            )
            
            # Calculate total due amount
            total_due = sum(bill.remaining_due() for bill in unpaid_bills)
            
            # Only create request if none exists and there are unpaid bills
            if not existing_request and unpaid_bills.exists() and total_due > 0:
                # Create payment request
                payment_request = MessPaymentRequest.objects.create(
                    student=self.student,
                    request_date=timezone.now(),
                    amount=total_due,
                    status='PENDING',
                    milestone_days=5,  # Changed from 10 to 5
                    request_note=f"Payment request after {days_count} days attendance. Registration: {self.student.reg_no}",
                    payment_method='STRIPE'  # Set Stripe as payment method
                )
                
                # Associate bills with the payment request
                for bill in unpaid_bills:
                    payment_request.bills.add(bill)
                
                # Process the payment automatically using Stripe
                self.process_payment_with_stripe(payment_request, total_due)
    
    def process_payment_with_stripe(self, payment_request, amount):
        # """Process the payment using Stripe"""
        try:
            # Get or create Stripe customer for this student
            stripe_customer = self.get_or_create_stripe_customer()
            
            # Create a payment intent
            payment_intent = stripe.PaymentIntent.create(
                amount=int(amount * 100),  # Convert to cents
                currency='usd',  # Change based on your currency
                customer=stripe_customer.id,
                description=f"Mess payment for {self.student.F_Name} {self.student.L_Name} (Reg No: {self.student.reg_no})",
                metadata={
                    'student_id': self.student.id,
                    'payment_request_id': payment_request.id,
                    'registration_number': self.student.reg_no
                },
                payment_method_types=['card'],
                # Attempt to use saved payment method if available
                payment_method=stripe_customer.invoice_settings.default_payment_method if hasattr(stripe_customer, 'invoice_settings') and hasattr(stripe_customer.invoice_settings, 'default_payment_method') else None,
                confirm=True if hasattr(stripe_customer, 'invoice_settings') and hasattr(stripe_customer.invoice_settings, 'default_payment_method') else False,
            )
            
            # Record the payment intent ID
            payment_request.stripe_payment_intent_id = payment_intent.id
            payment_request.save()
            
            # If payment method is saved and confirm=True was successful
            if payment_intent.status == 'succeeded':
                self.record_successful_payment(payment_request, amount)
            
        except stripe.error.StripeError as e:
            # Handle Stripe errors
            payment_request.status = 'FAILED'
            payment_request.request_note += f" | Stripe Error: {str(e)}"
            payment_request.save()
    
    def get_or_create_stripe_customer(self):
        # """Get or create a Stripe customer for this student"""
        try:
            # Check if student already has a Stripe customer ID
            if hasattr(self.student, 'stripe_customer_id') and self.student.stripe_customer_id:
                return stripe.Customer.retrieve(self.student.stripe_customer_id)
            
            # Create a new customer
            customer = stripe.Customer.create(
                email=self.student.email,
                name=f"{self.student.F_Name} {self.student.L_Name}",
                metadata={
                    'student_id': self.student.id,
                    'registration_number': self.student.reg_no
                }
            )
            
            # Save the customer ID to the student model
            self.student.stripe_customer_id = customer.id
            self.student.save()
            
            return customer
            
        except stripe.error.StripeError as e:
            # Log the error
            print(f"Stripe Error: {str(e)}")
            raise
    
    def record_successful_payment(self, payment_request, amount):
        # """Record successful payment in the system"""
        # Update payment request status
        payment_request.status = 'COMPLETED'
        payment_request.save()
        
        # Mark bills as paid
        for bill in payment_request.bills.all():
            bill.paid_status = True
            bill.save()
            
            # Create payment record
            MessPayment.objects.create(
                student=self.student,
                bill=bill,
                payment_date=timezone.now(),
                amount=bill.remaining_due(),
                payment_method='STRIPE',
                payment_note=f"Automated Stripe payment after 5 days attendance. Payment Intent ID: {payment_request.stripe_payment_intent_id}"
            )

class MessFee(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)  # Assuming Student model exists
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mess Fee for {self.student}"

    # Additional methods if needed, like `remaining_due`
    @property
    def remaining_due(self):
        return self.total_cost - self.paid_amount
# ==========================
# Mess Payment System Model
# Mess Bill
# ==========================

from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator

class MessPaymentRequest(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    )

    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    request_date = models.DateTimeField(default=timezone.now)
    payment_method = models.CharField(max_length=20, default='CASH')
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    processed_date = models.DateTimeField(blank=True, null=True)
    admin_note = models.TextField(blank=True, null=True)
    payment_screenshot = models.FileField(
        upload_to='payment_screenshots/',
        validators=[FileExtensionValidator(['pdf', 'jpg', 'jpeg', 'png'])],
        blank=True, null=True
    )
    milestone_days = models.IntegerField(default=0)  # Days attended in last 30 days
    bills = models.ManyToManyField('MessBill', blank=True)

    def __str__(self):
        return f"{self.student} - {self.amount} ({self.status})"


class MessPayment(models.Model):
    PAYMENT_METHODS = [
        ('CASH', 'Cash'),
        ('BANK', 'Bank Transfer'),
        ('ADMIN', 'Admin Approved'),
        ('STRIPE', 'Stripe'),
        ('OTHER', 'Other')
    ]
    
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    bill = models.ForeignKey('MessBill', on_delete=models.CASCADE, related_name='payments')
    payment_date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS, default='CASH')
    payment_note = models.CharField(max_length=255, blank=True, null=True)
    stripe_payment_id = models.CharField(max_length=100, blank=True, null=True)  # Store Stripe payment ID
    
    def __str__(self):
        return f"Payment of {self.amount} for {self.student.F_Name} {self.student.L_Name} on {self.payment_date}"


class MessBill(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    bill_date = models.DateField(default=timezone.now)
    bill_month = models.CharField(max_length=20)
    bill_year = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Bill for {self.student.F_Name} {self.student.L_Name} - {self.bill_month} {self.bill_year}"

    def amount_paid(self):
        # Calculate the amount paid so far by summing payments related to this bill
        return self.payments.aggregate(total=models.Sum('amount'))['total'] or 0

    def remaining_due(self):
        # Calculate the remaining amount due, i.e., total_amount - amount_paid
        return self.total_amount - self.amount_paid()

    # If the bill is not fully paid, return the remaining due amount
    def amount_due(self):
        return self.remaining_due()

    class Meta:
        ordering = ['bill_date']


# ==========================
# Stripe PaymnetGateway
# ==========================

class StripePayment(models.Model):
    # """
    # Model to track Stripe payments and their status
    # """
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
        ('REFUNDED', 'Refunded')
    ]
    
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='stripe_payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_payment_intent_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    semester = models.CharField(max_length=255, blank=True, null=True)
    payment_record = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True, null=True, related_name='stripe_record')
    
    def __str__(self):
        return f"Payment {self.id} - {self.student.Registration_Number} - {self.status}"
    
    def complete_payment(self, stripe_payment_intent_id=None):
        # """
        # Complete the payment and create a Payment record
        # """
        if stripe_payment_intent_id:
            self.stripe_payment_intent_id = stripe_payment_intent_id
        
        # Get student's info
        student = self.student
        
        # Find next unpaid semester or payment record
        next_unpaid = student.payments.filter(Fee_Status='UNPAID').order_by('Installment_Number').first()
        
        # If there's no unpaid record, create a new payment record
        if not next_unpaid:
            # Find the last payment to determine next installment number
            last_payment = student.payments.order_by('-Installment_Number').first()
            next_installment = (last_payment.Installment_Number + 1) if last_payment else 1
            
            # Generate receipt number
            receipt_number = f"{student.Registration_Number}-{next_installment}"
            
            # Determine the semester
            semester = self.semester or self._determine_semester(next_installment)
            
            # Create new payment record
            payment = Payment.objects.create(
                Student_ID=student,
                Fee_Type=semester,
                Amount_Due=self.amount,
                Amount_Paid=self.amount,
                Receipt_Number=receipt_number,
                Fee_Status='PAID',
                Payment_Date=timezone.now(),
                Payment_Mode='ONLINE',
                Installment_Number=next_installment
            )
        else:
            # Update existing payment record
            next_unpaid.Amount_Paid = self.amount
            next_unpaid.Fee_Status = 'PAID'
            next_unpaid.Payment_Date = timezone.now()
            next_unpaid.Payment_Mode = 'ONLINE'
            next_unpaid.save()
            payment = next_unpaid
        
        # Update this record
        self.status = 'COMPLETED'
        self.payment_record = payment
        self.save()
        
        # Force update of student's fee status
        Payment.update_student_fee_status(student)
        
        return payment
    
    def _determine_semester(self, installment_number):
        # """
        # Determine semester based on installment number
        # """
        current_year = timezone.now().year
        sem_index = installment_number - 1
        year_offset = sem_index // 2
        
        # Even numbers are Fall, odd are Spring
        if sem_index % 2 == 0:
            return f"Fall-{current_year + year_offset}"
        else:
            return f"Spring-{current_year + year_offset + 1}"
        
        