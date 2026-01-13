# 🎓 UNIMIS - Student Management System

![Status](https://img.shields.io/badge/Status-Live-success?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Framework-Flask-black?style=for-the-badge&logo=flask)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-green?style=for-the-badge&logo=mongodb)

A robust, role-based School Management System that streamlines academic processes. From tracking attendance to generating official PDF reports, UNIMIS handles it all.

---

## 🌐 Live Demo & Access

**🚀 Deployment Link:** [https://unimis.onrender.com/](https://unimis.onrender.com/)

### 🔑 Demo Credentials (Student)
| Role | User ID | Password |
| :--- | :--- | :--- |
| **Student** | `2023CS001` | `studentpassword` |

---

## ✨ Key Highlights

### 📄 One-Click Official PDF Downloads
UNIMIS automates the generation of official documents, saving administrative time and giving students instant access to their records.
* **🏆 Result Generation:** Students can view their semester marks and instantly download a formatted **Official Result PDF**.
* **💰 Fee Receipts:** Real-time fee status checks with an option to download **Fee Payment Receipts/Statements** as PDFs.

---

## 📸 Application Gallery

### 👨‍💼 Admin Control Center
Comprehensive tools for managing faculty, students, and notices.
<p align="center">
  <img src="screenshots/admin/admin_dashboard.png" width="45%" alt="Admin Dashboard">
  <img src="screenshots/admin/admins_faculty_view.png" width="45%" alt="Faculty Management">
</p>
<p align="center"><em>Left: Main Admin Dashboard | Right: Faculty Management View</em></p>

<p align="center">
  <img src="screenshots/admin/notice_upload.png" width="45%" alt="Notice Board Config">
  <img src="screenshots/admin/branch_management.png" width="45%" alt="Branch Management">
</p>
<p align="center"><em>Notice Board Configuration & Branch Management</em></p>

### 👩‍🏫 Teacher Portal
Dedicated interface for class management and attendance tracking.
<p align="center">
  <img src="screenshots/teacher/Screenshot 2026-01-09 142213.png" width="30%" alt="Teacher Dashboard">
  <img src="screenshots/teacher/Screenshot 2026-01-09 142252.png" width="30%" alt="Attendance Marking">
  <img src="screenshots/teacher/Screenshot 2026-01-09 142314.png" width="30%" alt="Student List">
</p>
<p align="center"><em>Teacher Dashboard, Attendance Marking, and Student Lists</em></p>

### 👨‍🎓 Student Dashboard & Reports
<p align="center">
  <img src="screenshots/student/student_dashboard.png" width="45%" alt="Student Dashboard">
  <img src="screenshots/student/time_table.png" width="45%" alt="Timetable">
</p>

### 📑 PDF Generation (Results & Fees)
<p align="center">
  <img src="screenshots/student/result_pdf.png" width="45%" alt="Result PDF">
  <img src="screenshots/student/fees_pdf.png" width="45%" alt="Fees PDF">
</p>
<p align="center"><em>Auto-generated Official PDF Reports</em></p>

---

## 🚀 Features by Role

### 👨‍🎓 Student
* **Secure Login:** Access via Admission Number or Email.
* **📊 Insightful Dashboard:** View attendance stats (Present/Absent %) at a glance.
* **📥 Downloads:** **(Highlight)** Instant PDF downloads for Marksheets and Fee Receipts.
* **📅 Schedule:** Visual weekly class time table.
* **💸 Financials:** Track Tuition, Hostel, and Library fee status.

### 👩‍🏫 Teacher
* **Class Management:** View assigned subjects and classes.
* **📝 Attendance:** Digital interface to mark and update student attendance.
* **✅ Approvals:** Verify and approve new student registrations.

### 👨‍💼 Admin
* **👥 User Management:** Manage Faculty and Students by Branch/Year.
* **🏫 Academic Config:** Map subjects to branches, manage departments.
* **📢 Notices:** Broadcast announcements to the entire institution.

---

## 🛠️ Tech Stack

* **Backend:** Python 3, Flask (Blueprints)
* **Database:** MongoDB (PyMongo)
* **Reports:** ReportLab (PDF Generation)
* **Frontend:** HTML5, CSS3, JavaScript
* **Deployment:** Render / Gunicorn

---

## ⚙️ Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/ridham19/unimis.git](https://github.com/ridham19/unimis.git)
    cd unimis
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r backend/requirements.txt
    ```

3.  **Environment Setup**
    Set your `MONGO_URI` (local or Atlas) in your environment variables.
    ```bash
    export MONGO_URI="mongodb://localhost:27017/"
    ```

4.  **Seed Database**
    Initialize the system with the admin user and default data.
    ```bash
    python backend/seed_admin.py
    python backend/seed_branches.py
    ```

5.  **Run Application**
    ```bash
    python backend/app.py
    ```
    Visit `http://localhost:5000`

---

**Author:** [Ridham19](https://github.com/Ridham19)
