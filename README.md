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

## 🏗️ **Project Architecture**

<div align="center">

### 📁 **Directory Structure**

</div>

# Smart Hostel Management System - Project Structure

```
SmartHostelManagmentSystem_FYP/
├── 📁 hostel/                                    # Main Django Application
│   ├── 📄 admin.py                               # Django Admin Configuration
│   ├── 📄 apps.py                                # App Configuration
│   ├── 📄 models.py                              # Database Models
│   ├── 📄 views.py                               # Business Logic & Views
│   ├── 📄 urls.py                                # URL Routing
│   ├── 📄 forms.py                               # Form Definitions
│   ├── 📄 digitalpersona.py                     # Biometric Integration
│   │
│   ├── 📁 migrations/                            # Database Migrations
│   │   ├── 📄 0001_initial.py
│   │   ├── 📄 0002_payment_due_date_...
│   │   └── 📄 ... (97+ migration files)
│   │
│   ├── 📁 templatetags/                          # Custom Template Tags
│   │   ├── 📄 custom_filters.py
│   │   └── 📄 filters.py
│   │
│   └── 📁 templates/                             # HTML Templates
│       ├── 📄 base.html                          # Base Template Layout
│       ├── 📄 dashboard.html                     # Admin Dashboard
│       ├── 📄 student_dashboard.html             # Student Dashboard
│       ├── 📄 student_dues.html                  # Student Dues View
│       │
│       ├── 📁 hostel_management/                 # Hostel Management Templates
│       │   ├── 📄 add_hostel.html
│       │   ├── 📄 edit_hostel.html
│       │   ├── 📄 list_hostels.html
│       │   ├── 📄 manage_room_prices.html
│       │   └── 📄 view_hostel_rooms.html
│       │
│       ├── 📁 room_management/                   # Room Management Templates
│       │   ├── 📄 add_room.html
│       │   ├── 📄 edit_room.html
│       │   ├── 📄 list_rooms.html
│       │   └── 📄 delete_room_confirmation.html
│       │
│       ├── 📁 student_management/                # Student Management Templates
│       │   ├── 📄 add_student.html
│       │   ├── 📄 edit_student.html
│       │   ├── 📄 list_students.html
│       │   ├── 📄 view_student.html
│       │   └── 📄 delete_student_confirmation.html
│       │
│       ├── 📁 mess_management/                   # Mess Management Templates
│       │   ├── 📄 add_mess_menu.html
│       │   ├── 📄 admin_mess_management.html
│       │   ├── 📄 mess_apply.html
│       │   ├── 📄 mess_request.html
│       │   ├── 📄 mess_status.html
│       │   ├── 📄 mess_membership_status.html
│       │   ├── 📄 view_mess_menu.html
│       │   ├── 📄 student_mess_bills.html
│       │   ├── 📄 inactive_memberships.html
│       │   ├── 📄 rejected_applications.html
│       │   ├── 📄 enroll_fingerprint.html
│       │   ├── 📄 manage_attendance.html
│       │   ├── 📄 mark_attendance.html
│       │   ├── 📄 mess_attendance.html
│       │   ├── 📄 breakfast_attendance.html
│       │   ├── 📄 lunch_attendance.html
│       │   ├── 📄 dinner_attendance.html
│       │   └── 📄 tea_break_attendance.html
│       │
│       ├── 📁 mess_bill_payment/                 # Mess Payment Management
│       │   ├── 📄 add_mess_payment.html
│       │   ├── 📄 mess_bill.html
│       │   ├── 📄 mess_account_book.html
│       │   ├── 📄 admin_payment_requests.html
│       │   ├── 📄 payment_request_form.html
│       │   ├── 📄 payment_request_details.html
│       │   ├── 📄 process_payment_request.html
│       │   ├── 📄 payment_success.html
│       │   ├── 📄 student_mess_payment_details.html
│       │   ├── 📄 enroll_fingerprint.html
│       │   ├── 📄 fingerprint_attendance.html
│       │   └── 📄 fingerprint_status.html
│       │
│       ├── 📁 payment_management/                # Fee Payment Management
│       │   ├── 📄 add_payment.html
│       │   ├── 📄 account_book.html
│       │   ├── 📄 admin_payment_requests.html
│       │   ├── 📄 fee_management.html
│       │   ├── 📄 view_student_fee.html
│       │   └── 📄 success.html
│       │
│       ├── 📁 notice_complaint_management/       # Notice & Complaint System
│       │   ├── 📄 add_notice.html
│       │   ├── 📄 edit_notice.html
│       │   ├── 📄 view_notice.html
│       │   ├── 📄 view_notice_student.html
│       │   ├── 📄 list_of_noticeboard.html
│       │   ├── 📄 student_notices.html
│       │   ├── 📄 delete_notice_confirmation.html
│       │   ├── 📄 submit_complaint.html
│       │   ├── 📄 list_complaints.html
│       │   └── 📄 view_complaint.html
│       │
│       ├── 📁 student_showcaseNotice/            # Student Showcase System
│       │   ├── 📄 create_showcase_notice.html
│       │   ├── 📄 edit_showcase_notice.html
│       │   ├── 📄 admin_showcase_notices.html
│       │   ├── 📄 student_showcase_notices.html
│       │   ├── 📄 showcase_notice_detail.html
│       │   ├── 📄 view_showcase_notice.html
│       │   ├── 📄 view_student_showcase_notice.html
│       │   ├── 📄 resolved_showcase_notices.html
│       │   └── 📄 delete_showcase_notice.html
│       │
│       ├── 📁 visitor_management/                # Visitor Management System
│       │   ├── 📄 create_visitor_request.html
│       │   ├── 📄 request_visitor.html
│       │   ├── 📄 visitor_requests.html
│       │   ├── 📄 update_visitor_request.html
│       │   ├── 📄 admin_manage_visitor_requests.html
│       │   └── 📄 all_std_request_history.html
│       │
│       └── 📁 user_auth/                         # User Authentication
│           ├── 📄 login.html
│           ├── 📄 register.html
│           └── 📄 std_profile.html
│
├── 📁 hostel_management_system/                  # Django Project Settings
│   ├── 📄 settings.py                            # Django Configuration
│   ├── 📄 urls.py                                # Main URL Configuration
│   ├── 📄 wsgi.py                                # WSGI Server Configuration
│   └── 📄 asgi.py                                # ASGI Server Configuration
│
├── 📄 manage.py                                  # Django Management Script
└── 📄 requirements.txt                           # Python Dependencies


```
---

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
