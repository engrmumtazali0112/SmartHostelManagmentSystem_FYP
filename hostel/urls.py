from django.urls import path
from . import views
from .views import fingerprint_attendance, fingerprint_status , enroll_fingerprint 
urlpatterns = [
   
    # ===========================#
    # User Authentication URLs   #
    # ===========================#
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),

   
    # ===========================#
    # Student Management URLs    #
    # ===========================#
    path('students/add/', views.add_student, name='add_student'),
    path('students/', views.list_students, name='list_students'),
    path('students/edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('student/<int:student_id>/', views.view_student, name='view_student'),
    
    # ===========================#
    # Hostel Management URLs    #
    # ===========================#
     # Your existing URL patterns...
    path('students/export/pdf/', views.export_students_pdf, name='export_students_pdf'),
    # If you don't already have it, add this for the CSV export as well:
    path('students/export/csv/', views.export_students_csv, name='export_students_csv'),
    # Hostel Management URLs
    path('hostels/add/', views.add_hostel, name='add_hostel'),
    
    path('bulk_fee_reminder/', views.bulk_fee_reminder, name='bulk_fee_reminder'),
    path('hostels/edit/<int:hostel_id>/', views.edit_hostel, name='edit_hostel'),
    path('hostels/delete/<int:hostel_id>/', views.delete_hostel, name='delete_hostel'),
    path('assign_hostel/', views.assign_hostel, name='assign_hostel'),  # Adjust the view name as needed
    path('hostels/<int:hostel_id>/rooms/', views.view_hostel_rooms, name='view_hostel_rooms'),
    path('hostels/', views.list_hostels, name='list_hostels'),

    # ===========================#
    # Room Management URLs    #
    # ===========================#
    path('rooms/', views.list_rooms, name='list_rooms'),
    path('rooms/add/', views.add_room, name='add_room'),
    path('rooms/edit/<int:room_id>/', views.edit_room, name='edit_room'),
    path('rooms/delete/<int:room_id>/', views.delete_room, name='delete_room'),


    # ===========================#
    # Dashboard, Std_Profile Management URLs    #
    # ===========================#
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    # Student Dashboard
    path('student/profile/', views.std_profile, name='std_profile'),
    # Admin Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),


    # ===========================#
    # Notice Board Management URLs    
    # ===========================#
    path('admin/notices/', views.list_of_notices, name='list_of_notices'),
    path('admin/notice/add/', views.add_notice, name='add_notice'),
    path('admin/notice/<int:notice_id>/', views.view_notice, name='view_notice'),
    path('admin/notice/<int:notice_id>/edit/', views.edit_notice, name='edit_notice'),
    path('admin/notice/<int:notice_id>/delete/', views.delete_notice, name='delete_notice'),
    path('notices/', views.student_notices, name='student_notices'),
    path('notice/<int:notice_id>/', views.student_view_notice, name='student_view_notice'),


    # ===========================#
    # Complaints Management URLs #
    # ===========================#
    path('submit_complaint/', views.submit_complaint, name='submit_complaint'),
    path('complaints/', views.list_complaints, name='list_complaints'),
    path('complaint/<int:complaint_id>/', views.view_complaint, name='view_complaint'),

   
    # ===========================#
    # Visitor Management URLs
    # ===========================#
    path('request_visitor/', views.request_visitor, name='request_visitor'),
    path('visitor_requests/', views.visitor_requests, name='visitor_requests'),
    path('update-visitor-request/<int:id>/', views.update_visitor_request, name='update_visitor_request'),
    path('student/request_history/', views.std_request_history, name='std_request_history'),
    path('admin/manage_visitor_requests/', views.admin_manage_visitor_requests, name='admin_manage_visitor_requests'),

    # ===========================
    # Admin Showcase Notice URLs
    # Student Showcase Notice URLs
    # ===========================
    path('admin/showcase-notices/', views.admin_showcase_notices, name='admin_showcase_notices'),
    path('search/students/', views.search_students, name='search_students'),  # Search Students for Admin
    path('admin/showcase-notices/<int:notice_id>/', views.view_showcase_notice, name='view_showcase_notice'),
    path('admin/showcase-notices/<int:notice_id>/edit/', views.edit_showcase_notice, name='edit_showcase_notice'),
    path('admin/showcase-notices/<int:notice_id>/delete/', views.delete_showcase_notice, name='delete_showcase_notice'),
    path('admin/showcase-notices/create/', views.create_showcase_notice, name='create_showcase_notice'),
    path('student/showcase-notices/', views.student_showcase_notices, name='student_showcase_notices'),
    path('student/showcase-notices/<int:notice_id>/', views.view_student_showcase_notice, name='view_student_showcase_notice'),

    # ===========================#
    # Hostel Payment management
    # ===========================#
    path('add-payment/', views.add_payment, name='add_payment'),
    path('account-book/', views.account_book, name='account_book'),
    path('mess-account-book/', views.mess_account_book, name='mess_account_book'),
    path('account-book/<int:student_id>/', views.account_book, name='account_book_with_id'),
    path('fee-management/', views.fee_management, name='fee_management'),

    
    # ===========================#
    # Stripe payment Gateway routes
    # ===========================#
    path('stripe-success/', views.stripe_success, name='stripe_success'),
    path('stripe-cancel/', views.stripe_cancel, name='stripe_cancel'),
    path('stripe-webhook/', views.stripe_webhook, name='stripe_webhook'),
    path('hostel/mess/stripe/checkout-session/', views.create_stripe_checkout_session, name='create_stripe_checkout_session'), 
 
    # ===========================#
    # Mess Management URLs
    # ===========================#
    path('apply-mess/', views.apply_for_mess, name='apply_for_mess'),
    path('mess-menu/', views.view_mess_menu, name='mess_menu'),
    path('mess-request/', views.mess_request, name='mess_request'),
    path('mess/attendance/', views.mess_attendance, name='mess_attendance'),
    path('mess-status/', views.mess_status, name='mess_status'),
    path('admin/mess-management/', views.admin_mess_management, name='admin_mess_management'),
    path('add-mess-menu/', views.add_mess_menu, name='add_mess_menu'),
    path('view-mess-menu/', views.view_mess_menu, name='view_mess_menu'),
    path('add-multiple-menu-items/', views.add_multiple_menu_items, name='add_multiple_menu_items'),
    path('mess-attendance/', views.manage_attendance, name='manage_attendance'),
    
    path('enroll-fingerprint/', views.enroll_fingerprint, name='enroll_fingerprint'),
    path('mark-attendance/', views.mark_attendance, name='mark_attendance'),
    
    path('mess/admin/inactive/', views.inactive_memberships, name='inactive_memberships'),
    path('mess/admin/rejected/', views.rejected_applications, name='rejected_applications'),
   
    
    path('breakfast-attendance/', views.breakfast_attendance, name='breakfast_attendance'),
    path('lunch-attendance/', views.lunch_attendance, name='lunch_attendance'),
    path('tea-break-attendance/', views.tea_break_attendance, name='tea_break_attendance'),
    path('dinner-attendance/', views.dinner_attendance, name='dinner_attendance'),
    
    
    path('mess/bill/', views.mess_bill, name='mess_bill'),

    path('admin/payment-requests/', views.admin_payment_requests, name='admin_payment_requests'),
    path('admin/payment-requests/<int:request_id>/', views.process_payment_request, name='process_payment_request'),
    path('payment-request/', views.payment_request_form, name='payment_request_form'),
    path('admin/payment-requests/details/<int:request_id>/', views.payment_request_details, name='payment_request_details'),
    path('student/mess-payment-details/<int:student_id>/', views.student_mess_payment_details, name='student_mess_payment_details'),

    path('fingerprint/enroll/', enroll_fingerprint, name='enroll_fingerprint'),
    path('fingerprint/attendance/', fingerprint_attendance, name='fingerprint_attendance'),
    path('fingerprint/status/', fingerprint_status, name='fingerprint_status'),



]
