# 🎓 Django Marksheet Management System

A simple but powerful **Django-based Marksheet Management System** with Role-Based Authentication (Admin, Teacher, Student).  
This project allows managing students, marks, and user roles with a clean dashboard UI using Bootstrap.

---

# 🚀 Features

## 🔐 Authentication System
- Login / Logout system
- Role-based access control
- Secure session handling

## 👥 User Roles
- 👑 Admin → Full access (add/edit/delete users & marks)
- 👨‍🏫 Teacher → Can add & edit student marks
- 👨‍🎓 Student → View-only access (future enhancement)

## 📊 Marksheet System
- Add student marks
- Auto calculate total marks
- Auto percentage calculation
- Display all student results in table

## 🎛️ Admin Dashboard
- Total students count
- Average percentage
- Clean Bootstrap UI
- Quick actions (Add/Edit/Delete)

## ✏️ CRUD Features
- Create student
- Read student list
- Update student marks
- Delete student records

---

# 🛠️ Technologies Used

- 🐍 Python 3
- 🌐 Django Framework
- 🎨 HTML5
- 🎨 CSS3
- 🎨 Bootstrap 5
- 🗄️ SQLite (default database)

---

# 📦 Django Modules Used

- django.contrib.admin
- django.contrib.auth
- django.contrib.contenttypes
- django.contrib.sessions
- django.contrib.messages
- django.shortcuts
- django.forms
- django.db.models
- django.contrib.auth.decorators

---

| Page        | URL       |
| ----------- | --------- |
| Login       | `/login/` |
| Dashboard   | `/`       |
| Add Student | `/add/`   |
| Admin Panel | `/admin/` |


📚 What I Learned from This Project
- Django project structure
- CRUD operations in Django
- Role-based authentication system
- Session handling
- Django forms & models
- Bootstrap UI integration
- Signals (auto profile creation)
- URL routing system

⚠️ Problems Faced & Solutions
❌ 1. Random Logout Issue

Problem:
User was getting redirected to login page while adding student.

Solution:

Fixed user_passes_test
Ensured Profile exists for every user
Correct session middleware usage

❌ 2. Role System Not Working

Problem:
Teacher/Admin role was not detected.

Solution:

Created Profile model
Added signal to auto-create profile
Fixed admin panel registration

❌ 3. Profile Not Showing in Admin Panel

Problem:
Role field not visible.

Solution:

Registered Profile in admin.py
Ran migrations properly

❌ 4. Login Redirect Confusion

Problem:
Users thought they were logged out.

Solution:

Fixed redirect to dashboard
Proper login_required usage

🎯 Future Improvements
📄 PDF Marksheet download
📊 Graph-based analytics
👨‍🎓 Student personal dashboard
🔍 Search & filter system
🎨 Advanced UI (AdminLTE / Tailwind)
🔐 Password reset system

👨‍💻 Author

Developed by: Django Learner 🚀


