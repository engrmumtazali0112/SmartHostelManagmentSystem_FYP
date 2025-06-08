# 🏢 Smart Hostel Management System

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![Stripe](https://img.shields.io/badge/Stripe-626CD9?style=for-the-badge&logo=Stripe&logoColor=white)

[![GitHub issues](https://img.shields.io/github/issues/engrmumtazali0112/SmartHostelManagmentSystem_FYP)](https://github.com/engrmumtazali0112/SmartHostelManagmentSystem_FYP/issues)
[![GitHub forks](https://img.shields.io/github/forks/engrmumtazali0112/SmartHostelManagmentSystem_FYP)](https://github.com/engrmumtazali0112/SmartHostelManagmentSystem_FYP/network)
[![GitHub stars](https://img.shields.io/github/stars/engrmumtazali0112/SmartHostelManagmentSystem_FYP)](https://github.com/engrmumtazali0112/SmartHostelManagmentSystem_FYP/stargazers)
[![GitHub license](https://img.shields.io/github/license/engrmumtazali0112/SmartHostelManagmentSystem_FYP)](https://github.com/engrmumtazali0112/SmartHostelManagmentSystem_FYP/blob/main/LICENSE)

</div>

---

## 🎯 **About The Project**

> *A comprehensive web-based solution revolutionizing hostel management with cutting-edge technology*

The **Smart Hostel Management System** is an innovative software solution designed to automate and streamline hostel operations, replacing outdated manual processes with an intelligent, user-friendly digital platform that serves administrators, staff, and students seamlessly.

<div align="center">

### 🏛️ **Academic Information!**

| 🎓 **University** | 👥 **Department** | 📅 **Academic Year** | 🎯 **Project Type** |
|:---:|:---:|:---:|:---:|
| University of Engineering & Technology Mardan | Computer Science | 2024-2025 | Final Year Project (FYP) |

</div>

---

## 👨‍💻 **Meet Our Team**

<div align="center">

| 👤 **Developer** | 🎫 **Registration** | 📧 **Contact** | 🌟 **Role** |
|:---:|:---:|:---:|:---:|
| **Mumtaz Ali** | 21MDBCS124 | [📧](mailto:Engrmumtazali01@gmail.com) | Lead Developer |
| **Muhammad Maaz** | 21MDBCS151 | [📧](mailto:maazkhan29456@gmail.com) | Backend Developer |
| **Muhammad Abubakar** | 21MDBCS169 | [📧](mailto:m.abubaakar755@gmail.com) | Frontend Developer |

**🎓 Supervisor:** Dr. Sarwar Shah Saib

</div>

---

## 🚀 **Key Features**

<div align="center">

### 🌟 **Core Capabilities**

</div>

| 🏠 **Feature** | 📝 **Description** | ✅ **Status** |
|:---|:---|:---:|
| 🏠 **Room Management** | Intelligent room allocation and hostel administration | ✅ |
| 🍽️ **Mess Management** | Automated mess billing and menu management | ✅ |
| 📱 **Smart Notifications** | Real-time notifications for fees and announcements | ✅ |
| 👆 **Biometric Integration** | Fingerprint-based attendance tracking | ✅ |
| 💳 **Payment Gateway** | Secure online payments via Stripe | ✅ |
| 📞 **Complaint System** | Streamlined complaint handling and resolution | ✅ |
| 👥 **Visitor Management** | Digital visitor tracking and approval system | ✅ |
| 📊 **Analytics Dashboard** | Comprehensive reporting and insights | ✅ |

---



## 📁 Complete Project Directory Structure
<details>
<summary><strong>🔍 Click to view complete project structure</strong></summary>


```
SmartHostelManagmentSystem_FYP/
├── 📄 README.md                                 # Project documentation
├── 📄 LICENSE                                   # MIT License file
├── 📄 requirements.txt                          # Python dependencies
├── 📄 manage.py                                 # Django management script
├── 📄 .gitignore                               # Git ignore rules
├── 📄 .env.example                             # Environment variables template
│
├── 📁 hostel_management_system/                # Django project settings
│   ├── 📄 __init__.py                          # Python package marker
│   ├── 📄 settings.py                          # Django configuration
│   ├── 📄 urls.py                              # Main URL configuration
│   ├── 📄 wsgi.py                              # WSGI server configuration
│   ├── 📄 asgi.py                              # ASGI server configuration
│   └── 📁 __pycache__/                         # Python cache files
│
├── 📁 hostel/                                  # Main Django application
│   ├── 📄 __init__.py                          # Python package marker
│   ├── 📄 admin.py                             # Django admin configuration
│   ├── 📄 apps.py                              # App configuration
│   ├── 📄 models.py                            # Database models
│   ├── 📄 views.py                             # Business logic & views
│   ├── 📄 urls.py                              # URL routing
│   ├── 📄 forms.py                             # Form definitions
│   ├── 📄 tests.py                             # Unit tests
│   ├── 📄 digitalpersona.py                    # Biometric integration
│   ├── 📄 custom_filters.py                    # Template filters
│   │
│   ├── 📁 migrations/                          # Database migrations
│   │   ├── 📄 __init__.py
│   │   ├── 📄 0001_initial.py
│   │   ├── 📄 0002_payment_due_date_payment_payment_mode_and_more.py
│   │   ├── 📄 0003_payment_installment_number_and_more.py
│   │   ├── 📄 0004_alter_payment_payment_mode.py
│   │   ├── 📄 0005_remove_student_total_fee_amount_payment_pdf_file.py
│   │   ├── 📄 0006_paymentrequest.py
│   │   ├── 📄 0007_remove_payment_pdf_file.py
│   │   ├── 📄 0008_payment_pdf_file.py
│   │   ├── 📄 0009_delete_paymentrequest.py
│   │   ├── 📄 0010_complaint_is_read.py
│   │   ├── 📄 0011_admin_user.py
│   │   ├── 📄 0012_alter_admin_user.py
│   │   ├── 📄 0013_alter_admin_user.py
│   │   ├── 📄 0014_remove_admin_user.py
│   │   ├── 📄 0015_admin_user.py
│   │   ├── 📄 0016_remove_admin_user.py
│   │   ├── 📄 0017_admin_user.py
│   │   ├── 📄 0018_alter_admin_user.py
│   │   ├── 📄 0019_remove_admin_user_delete_noticeboard.py
│   │   ├── 📄 0020_noticeboard.py
│   │   ├── 📄 0021_paymentrequest.py
│   │   ├── 📄 0022_delete_paymentrequest.py
│   │   ├── 📄 0023_delete_noticeboard.py
│   │   ├── 📄 0024_admin_user.py
│   │   ├── 📄 0025_remove_admin_user_noticeboard.py
│   │   ├── 📄 0026_admin_user.py
│   │   ├── 📄 0027_remove_admin_user.py
│   │   ├── 📄 0028_profile.py
│   │   ├── 📄 0029_profile_contact_info.py
│   │   ├── 📄 0030_visitors_is_read.py
│   │   ├── 📄 0031_alter_attendance_date_alter_attendance_status_and_more.py
│   │   ├── 📄 0032_messrequest.py
│   │   ├── 📄 0033_remove_student_mess_status.py
│   │   ├── 📄 0034_messmenu_remove_mess_hostel_id_and_more.py
│   │   ├── 📄 0035_alter_messattendance_date_facedetectionrecord_and_more.py
│   │   ├── 📄 0036_remove_facedetectionrecord_date_and_more.py
│   │   ├── 📄 0037_alter_visitors_approval_status_and_more.py
│   │   ├── 📄 0038_alter_visitors_approval_status_and_more.py
│   │   ├── 📄 0039_alter_visitors_approval_status_and_more.py
│   │   ├── 📄 0040_paymentrequest.py
│   │   ├── 📄 0041_paymentrequest_is_read.py
│   │   ├── 📄 0042_notification.py
│   │   ├── 📄 0043_remove_visitors_student_id_and_more.py
│   │   ├── 📄 0044_visitorrequest_time_in_visitorrequest_time_out.py
│   │   ├── 📄 0045_alter_messattendance_date.py
│   │   ├── 📄 0046_visitor_visitor_id_proof_visitor_purpose_of_visit.py
│   │   ├── 📄 0047_visitorrequest_is_read.py
│   │   ├── 📄 0048_paymentrequest_is_read.py
│   │   ├── 📄 0049_messmenu_meal_time.py
│   │   ├── 📄 0050_alter_messmenu_options_messmenu_day_messmenu_month_and_more.py
│   │   ├── 📄 0051_alter_messmenu_meal_time.py
│   │   ├── 📄 0052_messmembership_approved_messmembership_date_applied_and_more.py
│   │   ├── 📄 0053_remove_student_hostel_id_and_more.py
│   │   ├── 📄 0054_student_hostel_id.py
│   │   ├── 📄 0055_showcasenotice.py
│   │   ├── 📄 0056_messmembership_department_messmembership_status.py
│   │   ├── 📄 0057_messattendance_meal_time_and_more.py
│   │   ├── 📄 0058_remove_showcasenotice_evidence_and_more.py
│   │   ├── 📄 0059_alter_student_room_id.py
│   │   ├── 📄 0060_alter_showcasenotice_title.py
│   │   ├── 📄 0061_showcasenotice_registration_number.py
│   │   ├── 📄 0062_messrequest.py
│   │   ├── 📄 0063_messbill_payment_date_messpayment.py
│   │   ├── 📄 0064_alter_messpayment_payment_method_messpaymentrequest.py
│   │   ├── 📄 0065_studentshowcasenotice_paid.py
│   │   ├── 📄 0066_fingerprint_messmembership_fingerprint.py
│   │   ├── 📄 0067_stripepayment.py
│   │   ├── 📄 0068_roomtype_and_more.py
│   │   ├── 📄 0069_room_is_available.py
│   │   ├── 📄 0070_remove_room_is_available_room_price_and_more.py
│   │   ├── 📄 0071_room_is_available.py
│   │   ├── 📄 0072_student_room_price.py
│   │   ├── 📄 0073_alter_room_price.py
│   │   ├── 📄 0074_hostel_eight_seater_price_hostel_five_seater_price_and_more.py
│   │   ├── 📄 0075_student_total_fee.py
│   │   ├── 📄 0076_stripepayment_payment_type.py
│   │   ├── 📄 0077_payment_amount_due.py
│   │   ├── 📄 0078_remove_payment_amount_due_and_more.py
│   │   ├── 📄 0079_payment_amount_due.py
│   │   ├── 📄 0080_alter_payment_payment_date_and_more.py
│   │   ├── 📄 0081_student_paid_installments_count_and_more.py
│   │   ├── 📄 0082_remove_student_paid_installments_count_and_more.py
│   │   ├── 📄 0083_student_paid_installment_count.py
│   │   ├── 📄 0084_remove_stripepayment_stripe_charge_id_and_more.py
│   │   ├── 📄 0085_alter_messbill_options_remove_messbill_amount_due_and_more.py
│   │   ├── 📄 0086_alter_stripepayment_options_and_more.py
│   │   ├── 📄 0087_stripepayment_semester.py
│   │   ├── 📄 0088_alter_stripepayment_options_and_more.py
│   │   ├── 📄 0089_alter_stripepayment_options_and_more.py
│   │   ├── 📄 0090_stripepayment_semester.py
│   │   ├── 📄 0091_alter_stripepayment_options_and_more.py
│   │   ├── 📄 0092_alter_stripepayment_options.py
│   │   ├── 📄 0093_alter_stripepayment_options.py
│   │   ├── 📄 0094_rename_request_note_messpaymentrequest_admin_note_and_more.py
│   │   ├── 📄 0095_messfee.py
│   │   ├── 📄 0096_fingerprint_last_updated.py
│   │   ├── 📄 0097_feereminder.py
│   │   └── 📁 __pycache__/                      # Compiled migration files
│   │
│   ├── 📁 static/                               # Static files (CSS, JS, Images)
│   │   ├── 📄 FeeChallan.pdf                    # Fee challan template
│   │   ├── 📁 css/                              # Stylesheets
│   │   │   ├── 📄 admin_showcasenotices.css
│   │   │   ├── 📄 all.min.css
│   │   │   ├── 📄 bootstrap.min.css
│   │   │   ├── 📄 notice-detail-additional-styles.css
│   │   │   ├── 📄 notice-detail-styles.css
│   │   │   └── 📄 showcase_notice.css
│   │   ├── 📁 js/                               # JavaScript files
│   │   │   ├── 📄 bootstrap-datetimepicker.min.js
│   │   │   ├── 📄 bootstrap.bundle.min.js
│   │   │   ├── 📄 jquery-3.5.1.min.js
│   │   │   ├── 📄 jquery-3.5.1.slim.min.js
│   │   │   ├── 📄 jquery.min.js
│   │   │   ├── 📄 moment.min.js
│   │   │   └── 📄 notice-detail-scripts.js
│   │   └── 📁 images/                           # Image assets
│   │       ├── 📄 default-avatar.png
│   │       └── 📁 slider/                       # Slider images
│   │           ├── 📄 1.png
│   │           ├── 📄 2.png
│   │           ├── 📄 3.png
│   │           ├── 📄 4.png
│   │           └── 📄 5.png
│   │
│   ├── 📁 templates/                            # HTML templates
│   │   ├── 📄 base.html                         # Base template layout
│   │   ├── 📄 dashboard.html                    # Admin dashboard
│   │   ├── 📄 student_dashboard.html            # Student dashboard
│   │   ├── 📄 student_dues.html                 # Student dues view
│   │   │
│   │   ├── 📁 hostel_management/                # Hostel management templates
│   │   │   ├── 📄 add_hostel.html
│   │   │   ├── 📄 edit_hostel.html
│   │   │   ├── 📄 list_hostels.html
│   │   │   ├── 📄 manage_room_prices.html
│   │   │   └── 📄 view_hostel_rooms.html
│   │   │
│   │   ├── 📁 room_management/                  # Room management templates
│   │   │   ├── 📄 add_room.html
│   │   │   ├── 📄 edit_room.html
│   │   │   ├── 📄 list_rooms.html
│   │   │   └── 📄 delete_room_confirmation.html
│   │   │
│   │   ├── 📁 student_management/               # Student management templates
│   │   │   ├── 📄 add_student.html
│   │   │   ├── 📄 edit_student.html
│   │   │   ├── 📄 list_students.html
│   │   │   ├── 📄 view_student.html
│   │   │   └── 📄 delete_student_confirmation.html
│   │   │
│   │   ├── 📁 mess_management/                  # Mess management templates
│   │   │   ├── 📄 add_mess_menu.html
│   │   │   ├── 📄 admin_mess_management.html
│   │   │   ├── 📄 mess_apply.html
│   │   │   ├── 📄 mess_request.html
│   │   │   ├── 📄 mess_status.html
│   │   │   ├── 📄 mess_membership_status.html
│   │   │   ├── 📄 view_mess_menu.html
│   │   │   ├── 📄 student_mess_bills.html
│   │   │   ├── 📄 inactive_memberships.html
│   │   │   ├── 📄 rejected_applications.html
│   │   │   ├── 📄 enroll_fingerprint.html
│   │   │   ├── 📄 manage_attendance.html
│   │   │   ├── 📄 mark_attendance.html
│   │   │   ├── 📄 mess_attendance.html
│   │   │   ├── 📄 breakfast_attendance.html
│   │   │   ├── 📄 lunch_attendance.html
│   │   │   ├── 📄 dinner_attendance.html
│   │   │   └── 📄 tea_break_attendance.html
│   │   │
│   │   ├── 📁 mess_bill_payment/                # Mess payment management
│   │   │   ├── 📄 add_mess_payment.html
│   │   │   ├── 📄 mess_bill.html
│   │   │   ├── 📄 mess_account_book.html
│   │   │   ├── 📄 admin_payment_requests.html
│   │   │   ├── 📄 payment_request_form.html
│   │   │   ├── 📄 payment_request_details.html
│   │   │   ├── 📄 process_payment_request.html
│   │   │   ├── 📄 payment_success.html
│   │   │   ├── 📄 student_mess_payment_details.html
│   │   │   ├── 📄 enroll_fingerprint.html
│   │   │   ├── 📄 fingerprint_attendance.html
│   │   │   └── 📄 fingerprint_status.html
│   │   │
│   │   ├── 📁 payment_management/               # Fee payment management
│   │   │   ├── 📄 add_payment.html
│   │   │   ├── 📄 account_book.html
│   │   │   ├── 📄 admin_payment_requests.html
│   │   │   ├── 📄 fee_management.html
│   │   │   ├── 📄 view_student_fee.html
│   │   │   ├── 📄 success.html
│   │   │   ├── 📄 1.JPG                        # Payment screenshots/docs
│   │   │   ├── 📄 2.JPG
│   │   │   ├── 📄 3.JPG
│   │   │   ├── 📄 4.JPG
│   │   │   ├── 📄 5.JPG
│   │   │   ├── 📄 6.JPG
│   │   │   ├── 📄 11.JPG
│   │   │   ├── 📄 21.JPG
│   │   │   ├── 📄 23.JPG
│   │   │   ├── 📄 112.JPG
│   │   │   ├── 📄 212.JPG
│   │   │   └── 📄 213.JPG
│   │   │
│   │   ├── 📁 notice_complaint_management/      # Notice & complaint system
│   │   │   ├── 📄 add_notice.html
│   │   │   ├── 📄 edit_notice.html
│   │   │   ├── 📄 view_notice.html
│   │   │   ├── 📄 view_notice_student.html
│   │   │   ├── 📄 list_of_noticeboard.html
│   │   │   ├── 📄 student_notices.html
│   │   │   ├── 📄 delete_notice_confirmation.html
│   │   │   ├── 📄 submit_complaint.html
│   │   │   ├── 📄 list_complaints.html
│   │   │   └── 📄 view_complaint.html
│   │   │
│   │   ├── 📁 student_showcaseNotice/           # Student showcase system
│   │   │   ├── 📄 create_showcase_notice.html
│   │   │   ├── 📄 edit_showcase_notice.html
│   │   │   ├── 📄 admin_showcase_notices.html
│   │   │   ├── 📄 student_showcase_notices.html
│   │   │   ├── 📄 showcase_notice_detail.html
│   │   │   ├── 📄 view_showcase_notice.html
│   │   │   ├── 📄 view_student_showcase_notice.html
│   │   │   ├── 📄 resolved_showcase_notices.html
│   │   │   └── 📄 delete_showcase_notice.html
│   │   │
│   │   ├── 📁 visitor_management/               # Visitor management system
│   │   │   ├── 📄 create_visitor_request.html
│   │   │   ├── 📄 request_visitor.html
│   │   │   ├── 📄 visitor_requests.html
│   │   │   ├── 📄 update_visitor_request.html
│   │   │   ├── 📄 admin_manage_visitor_requests.html
│   │   │   └── 📄 all_std_request_history.html
│   │   │
│   │   └── 📁 user_auth/                        # User authentication
│   │       ├── 📄 login.html
│   │       ├── 📄 register.html
│   │       └── 📄 std_profile.html
│   │
│   ├── 📁 templatetags/                         # Custom template tags
│   │   ├── 📄 __init__.py
│   │   ├── 📄 custom_filters.py
│   │   ├── 📄 filters.py
│   │   └── 📁 __pycache__/                      # Compiled template tags
│   │       ├── 📄 __init__.cpython-312.pyc
│   │       ├── 📄 custom_filters.cpython-312.pyc
│   │       ├── 📄 filters.cpython-312.pyc
│   │       └── 📄 mess_tags.cpython-312.pyc
│   │
│   └── 📁 __pycache__/                          # Compiled Python files
│       ├── 📄 __init__.cpython-312.pyc
│       ├── 📄 admin.cpython-312.pyc
│       ├── 📄 apps.cpython-312.pyc
│       ├── 📄 forms.cpython-312.pyc
│       ├── 📄 models.cpython-312.pyc
│       ├── 📄 urls.cpython-312.pyc
│       └── 📄 views.cpython-312.pyc
│
├── 📁 media/                                    # User uploaded files
│   ├── 📁 profile_pictures/                     # Student profile images
│   ├── 📁 documents/                           # Student documents
│   ├── 📁 payment_receipts/                    # Payment receipts
│   └── 📁 complaint_attachments/               # Complaint attachments
│
├── 📁 docs/                                     # Project documentation
│   ├── 📄 INSTALLATION.md                      # Installation guide
│   ├── 📄 API_DOCUMENTATION.md                 # API documentation
│   ├── 📄 CONTRIBUTING.md                      # Contribution guidelines
│   ├── 📄 CHANGELOG.md                         # Version history
│   └── 📁 screenshots/                         # Application screenshots
│       ├── 📄 admin-dashboard.png
│       ├── 📄 student-dashboard.png
│       └── 📄 payment-interface.png
│
├── 📁 scripts/                                  # Utility scripts
│   ├── 📄 backup_database.py                   # Database backup script
│   ├── 📄 deploy.sh                           # Deployment script
│   └── 📄 setup_initial_data.py               # Initial data setup
│
├── 📁 tests/                                   # Test files
│   ├── 📄 __init__.py
│   ├── 📄 test_models.py                       # Model tests
│   ├── 📄 test_views.py                        # View tests
│   ├── 📄 test_forms.py                        # Form tests
│   └── 📄 test_utils.py                        # Utility tests
│
└── 📁 .github/                                 # GitHub configuration
    ├── 📁 workflows/                           # GitHub Actions
    │   ├── 📄 ci.yml                          # Continuous Integration
    │   └── 📄 deploy.yml                      # Deployment workflow
    ├── 📄 ISSUE_TEMPLATE.md                   # Issue template
    ├── 📄 PULL_REQUEST_TEMPLATE.md            # PR template
    └── 📄 CONTRIBUTING.md                     # Contributing guidelines
```
</details>

## 📊 Directory Statistics

| 📁 **Category** | 🔢 **Count** | 📝 **Description** |
|:---|:---:|:---|
| **📄 Core Python Files** | 8 | Main application logic files |
| **🗄️ Database Migrations** | 97 | Schema evolution history |
| **🎨 HTML Templates** | 60+ | User interface templates |
| **🎯 Static Files** | 15+ | CSS, JS, and image assets |
| **🏷️ Template Tags** | 3 | Custom Django template filters |
| **📱 Template Directories** | 9 | Organized by functionality |
| **💾 Cache Files** | 100+ | Compiled Python bytecode |


## 🛠️ **Technology Stack**

<div align="center">

### 💻 **Backend Technologies**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=flat-square&logo=sqlite&logoColor=white)

### 🎨 **Frontend Technologies**

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=flat-square&logo=bootstrap&logoColor=white)

### 🔧 **Tools & Platforms**

![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat-square&logo=github&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Stripe](https://img.shields.io/badge/Stripe-626CD9?style=flat-square&logo=Stripe&logoColor=white)

</div>

---

## 📸 **System Showcase**

<div align="center">

### 🖥️ **Admin Dashboard**

| ![Admin Dashboard](https://github.com/user-attachments/assets/932158c0-09ce-4d30-a198-5e698f73bb74) | ![Hostel Management](https://github.com/user-attachments/assets/e3fbf0cb-b232-4d2f-b544-6956bf6f9f17) |
|:---:|:---:|
| **📊 Comprehensive Dashboard** | **🏠 Hostel Management** |

### 👨‍🎓 **Student Interface**

| ![Student Dashboard](https://github.com/user-attachments/assets/2ac394ab-a23e-4831-af05-af917033eca8) | ![Payment History](https://github.com/user-attachments/assets/d6ebecfb-0f9b-4f51-9298-5d5feb850be6) |
|:---:|:---:|
| **📱 Student Dashboard** | **💰 Payment History** |

### 🍽️ **Mess Management**

| ![Mess Menu](https://github.com/user-attachments/assets/6df5fe26-450f-4553-90f2-4a86e33e993b) | ![Mess Billing](https://github.com/user-attachments/assets/9d78bc2c-2ca1-40d3-921d-7a08fc56d1fd) |
|:---:|:---:|
| **📋 Digital Menu** | **💳 Smart Billing** |

</div>

---

## 🚀 **Quick Start Guide**

### 📋 **Prerequisites**

Before you begin, ensure you have the following installed:

- 🐍 **Python 3.8+** - [Download Here](https://python.org)
- 📦 **pip** - Python package manager
- 🗄️ **Git** - Version control system

### ⚡ **Installation Steps**

1. **📥 Clone the Repository**
   ```bash
   git clone https://github.com/engrmumtazali0112/SmartHostelManagmentSystem_FYP.git
   cd SmartHostelManagmentSystem_FYP
   ```

2. **🔧 Create Virtual Environment**
   ```bash
   python -m venv hostel_env
   # Windows
   hostel_env\Scripts\activate
   # macOS/Linux
   source hostel_env/bin/activate
   ```

3. **📦 Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **🗄️ Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **👤 Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **🚀 Launch Application**
   ```bash
   python manage.py runserver
   ```

7. **🌐 Access the System**
   - Open your browser and navigate to: `http://127.0.0.1:8000`
   - Admin panel: `http://127.0.0.1:8000/admin`

---

## 💳 **Stripe Payment Integration**

### 🔐 **Setup Stripe API**

1. **Create Stripe Account**
   - Sign up at [Stripe Dashboard](https://stripe.com)

2. **Install Stripe SDK**
   ```bash
   pip install stripe
   ```

3. **Configure API Keys**
   ```python
   # settings.py
   STRIPE_TEST_PUBLIC_KEY = 'pk_test_your_publishable_key'
   STRIPE_TEST_SECRET_KEY = 'sk_test_your_secret_key'
   ```

4. **Environment Variables**
   ```bash
   # .env file
   STRIPE_PUBLIC_KEY=your_publishable_key
   STRIPE_SECRET_KEY=your_secret_key
   ```

---

## 📊 **System Modules**

<div align="center">

### 🏗️ **Module Overview**

</div>

| 🏠 **Module** | 📝 **Description** | 🔧 **Features** | ⚡ **Status** |
|:---|:---|:---|:---:|
| **🏠 Room Management** | Intelligent room allocation system | Room booking, availability tracking, capacity management | ✅ Complete |
| **🍽️ Mess Management** | Comprehensive dining facility management | Menu planning, billing, attendance tracking | ✅ Complete |
| **💰 Payment System** | Secure financial transaction handling | Online payments, fee tracking, receipt generation | ✅ Complete |
| **📞 Complaint Management** | Streamlined issue resolution platform | Ticket system, status tracking, admin responses | ✅ Complete |
| **👥 Visitor Management** | Digital visitor control system | Registration, approval workflow, entry logs | ✅ Complete |
| **📊 Attendance System** | Biometric-enabled tracking | Fingerprint recognition, automated logs, reports | ✅ Complete |
| **🔔 Notification Hub** | Real-time communication center | SMS, email, in-app notifications | ✅ Complete |
| **📢 Notice Board** | Digital announcement platform | News updates, important notices, event alerts | ✅ Complete |

---

## 📈 **Project Statistics**

<div align="center">

### 📊 **Development Metrics**

| 📁 **Category** | 🔢 **Count** | 📝 **Details** |
|:---:|:---:|:---|
| **📄 Python Files** | **25+** | Core application logic and utilities |
| **🗄️ Database Migrations** | **97** | Comprehensive schema evolution |
| **🎨 Templates** | **30+** | Responsive UI components |
| **🔧 Custom Features** | **15+** | Specialized functionality modules |
| **⚡ API Endpoints** | **50+** | RESTful service interfaces |

### 🏆 **Achievement Highlights**

- ✅ **100%** Module Completion Rate
- 🔐 **Advanced Security** Implementation
- 📱 **Responsive Design** Across All Devices
- ⚡ **Real-time** Notification System
- 💳 **Secure Payment** Gateway Integration

</div>

---

## 🤝 **Contributing Guidelines**

We welcome contributions from the community! Here's how you can help:

### 🔄 **How to Contribute**

1. **🍴 Fork the Project**
   ```bash
   git fork https://github.com/engrmumtazali0112/SmartHostelManagmentSystem_FYP.git
   ```

2. **🌿 Create Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. **💾 Commit Your Changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```

4. **📤 Push to Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```

5. **🔄 Open Pull Request**

### 📋 **Contribution Areas**

- 🐛 Bug fixes and improvements
- ✨ New feature development
- 📚 Documentation enhancements
- 🎨 UI/UX improvements
- 🔒 Security enhancements
- ⚡ Performance optimizations

---

## 🆘 **Support & Help**

<div align="center">

### 💬 **Get Support**

| 📞 **Support Type** | 🔗 **Channel** | ⏰ **Response Time** |
|:---:|:---:|:---:|
| **🐛 Bug Reports** | [GitHub Issues](https://github.com/engrmumtazali0112/SmartHostelManagmentSystem_FYP/issues) | 24-48 hours |
| **💡 Feature Requests** | [GitHub Discussions](https://github.com/engrmumtazali0112/SmartHostelManagmentSystem_FYP/discussions) | 2-3 days |
| **📧 Direct Contact** | [Email Support](mailto:engrmumtazali01@gmail.com) | 1-2 days |
| **💬 Community Chat** | [Discord Server](https://discord.gg/DZgwHzEb) | Real-time |

</div>

---

## 📜 **License**

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Smart Hostel Management System Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🌟 **Acknowledgments**

<div align="center">

### 🙏 **Special Thanks**

- **🎓 University of Engineering & Technology Mardan** - For academic support
- **👨‍🏫 Dr. Sarwar Shah Saib** - Project supervision and guidance
- **💻 Django Community** - For the robust framework
- **🔧 Open Source Contributors** - For invaluable tools and libraries
- **👥 Beta Testers** - For feedback and bug reports

</div>

---

## 📞 **Connect With Us**

<div align="center">

### 🌐 **Stay Connected**

<p align="center">
  <a href="mailto:engrmumtazali01@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
  </a>
  <a href="https://www.linkedin.com/in/mumtaz-ali">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
  </a>
  <a href="https://www.instagram.com/its_maliyzi">
    <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram"/>
  </a>
  <a href="https://x.com/mumtazali1223/status/1846913595021328672?s=51">
    <img src="https://img.shields.io/badge/X-1DA1F2?style=for-the-badge&logo=x&logoColor=white" alt="X"/>
  </a>
  <a href="https://discord.gg/DZgwHzEb">
    <img src="https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"/>
  </a>
  <a href="https://wa.me/923476338292">
    <img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp"/>
  </a>
  <a href="https://www.hackerrank.com/profile/engrmumtazali01">
    <img src="https://img.shields.io/badge/HackerRank-2EC866?style=for-the-badge&logo=hackerrank&logoColor=white" alt="HackerRank"/>
  </a>
</p>

### 📊 **GitHub Statistics**

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=engrmumtazali0112&show_icons=true&theme=radical&count_private=true" alt="GitHub Stats" />
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=engrmumtazali0112&theme=radical" alt="GitHub Streak" />
</p>

</div>

---

<div align="center">

### 🎉 **Thank You for Your Interest!**

<h3>⭐ If you found this project helpful, please consider giving it a star!</h3>

<p>
  <strong>Made with ❤️ by the Smart Hostel Management System Team</strong>
</p>

<p>
  <em>"Transforming hostel management through innovative technology"</em>
</p>

</div>

---

<div align="center">

![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer)

</div>