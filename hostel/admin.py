# ==========================
# Admin Registrations
# ==========================
from django.contrib import admin
from django.utils import timezone
from django.contrib import admin
from .models import ShowcaseNotice, StudentShowcaseNotice
from hostel.models import Student  # Assuming the Student model is in the students app

from .models import (
    Hostel, Room, Admin, Student, Visitor, Complaint, 
    Payment, NoticeBoard, MessMembership, MessAttendance,
    MessMenu, MessBill, VisitorRequest
)

# ==========================
# Mess Membership Admin
# ==========================
class MessMembershipAdmin(admin.ModelAdmin):
    list_display = ['student', 'start_date', 'end_date', 'is_active']
    search_fields = ['student__F_Name', 'student__L_Name']
admin.site.register(MessMembership, MessMembershipAdmin)

# ==========================
# Mess Attendance Admin
# ==========================
@admin.register(MessAttendance)
class MessAttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'date', 'is_present']
    list_filter = ['date']
    search_fields = ['student__F_Name', 'student__L_Name']

# ==========================
# Mess Menu Admin
# ==========================
@admin.register(MessMenu)
class MessMenuAdmin(admin.ModelAdmin):
    list_display = ['date', 'dish_name', 'price']
    search_fields = ['dish_name']

# ==========================
# Mess Bill Admin
# ==========================
from django.contrib import admin
from .models import MessBill

class MessBillAdmin(admin.ModelAdmin):
    list_display = ('student', 'bill_date', 'bill_month', 'bill_year', 'total_amount', 'amount_paid', 'amount_due', 'paid_status')

    def amount_paid(self, obj):
        return obj.amount_paid()

    def amount_due(self, obj):
        return obj.amount_due()

admin.site.register(MessBill, MessBillAdmin)

# ==========================
# Hostel Admin
# ==========================
@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
    # List display should reference attributes correctly from the model
    list_display = ['Hostel_ID', 'Hostel_Name', 'No_Of_Rooms', 'No_Of_Students']
    search_fields = ['Hostel_Name']
    list_filter = ['Hostel_Name']

# ==========================
# Notice Board Admin
# ==========================
@admin.register(NoticeBoard)
class NoticeBoardAdmin(admin.ModelAdmin):
    list_display = ('Notice_ID', 'Title', 'Created_At', 'Expiry_Date', 'Is_Active', 'Admin_ID')
    search_fields = ('Title', 'Content')
    list_filter = ('Is_Active', 'Created_At')
    ordering = ('-Created_At',)

    def save_model(self, request, obj, form, change):
        if obj.Expiry_Date and obj.Expiry_Date < timezone.now():
            obj.Is_Active = False
        super().save_model(request, obj, form, change)

# ==========================
# Room Admin
# ==========================
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['Room_ID', 'Room_Type', 'Capacity', 'Location', 'Room_No', 'Floor_No']

# ==========================
# Admin Model Admin
# ==========================
@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ['Admin_ID', 'Name', 'Email', 'Contact_Information', 'Admin_Role']

# ==========================
# Student Admin
# ==========================
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['Student_ID', 'F_Name', 'L_Name', 'get_email', 'Department', 'fee_status', 'get_last_payment']
    list_filter = ['fee_status', 'Department']
    search_fields = ['F_Name', 'L_Name', 'user__email']

    def get_email(self, obj):
        return obj.user.email if obj.user else 'N/A'
    get_email.short_description = 'Email'

    def get_last_payment(self, obj):
        last_payment = Payment.objects.filter(Student_ID=obj).order_by('-Payment_Date').first()
        return f"{last_payment.Amount_Paid} on {last_payment.Payment_Date.date()}" if last_payment else 'No Payment'
    get_last_payment.short_description = 'Last Payment'

# ==========================
# Complaint Admin
# ==========================
@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['Complaint_ID', 'Student_ID', 'Admin_ID', 'Complaint_Type', 'Created_At']

# ==========================
# Payment Admin
# ==========================
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('Payment_ID', 'Student_ID', 'Fee_Type', 'Amount_Paid', 'Payment_Date', 'Fee_Status')
    list_filter = ('Fee_Status', 'Payment_Mode', 'Payment_Date')  # Changed 'status' to 'Fee_Status'
    search_fields = ('Student_ID__F_Name', 'Student_ID__L_Name', 'Fee_Type', 'Receipt_Number')


# ==========================
# Visitor Admin
# ==========================
@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_info', 'visit_date', 'student']
    search_fields = ['name', 'contact_info']

# ==========================
# Visitor Request Admin
# ==========================
@admin.register(VisitorRequest)
class VisitorRequestAdmin(admin.ModelAdmin):
    list_display = ['student', 'visitor', 'request_date', 'status']
    list_filter = ['status']
    search_fields = ['student__F_Name', 'student__L_Name', 'visitor__name']

# ==========================
# ShowCashe Notics Admin
# ==========================

class StudentShowcaseNoticeInline(admin.TabularInline):
    model = StudentShowcaseNotice
    extra = 1  # Number of empty inline forms to display by default

class ShowcaseNoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'notice_type', 'created_date', 'resolved', 'fine_amount', 'due_date')
    list_filter = ('notice_type', 'resolved', 'created_date')
    search_fields = ('title', 'description',)
    ordering = ('-created_date',)
    inlines = [StudentShowcaseNoticeInline]  # Add inline to manage students linked to the notice
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('created_by')

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user  # Automatically assign current user if not specified
        super().save_model(request, obj, form, change)

class StudentShowcaseNoticeAdmin(admin.ModelAdmin):
    list_display = ('student', 'notice', 'read', 'read_date')
    list_filter = ('read', 'read_date')
    search_fields = ('student__name', 'notice__title')
    list_select_related = ('student', 'notice')  # Optimizing database queries

admin.site.register(ShowcaseNotice, ShowcaseNoticeAdmin)
admin.site.register(StudentShowcaseNotice, StudentShowcaseNoticeAdmin)
