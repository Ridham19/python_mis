# UNIMIS - Student Management System

A robust, role-based School Management System built with **Python Flask** and **MongoDB**. This application streamlines academic processes including attendance tracking, marks management, fee status, and scheduling for students, teachers, and administrators.

## 🌐 Live Demo

**Deployment Link:** [https://unimis.onrender.com/](https://unimis.onrender.com/)

### 🔑 Demo Credentials (Student)
* **ID:** `2023CS001`
* **Password:** `studentpassword`

---

## 🚀 Features by Role

### 👨‍🎓 Student
* **Secure Login:** Access via Admission Number (e.g., `2023CS001`) or Email.
* **Dashboard Overview:** Quick stats on attendance and performance.
* **Attendance Tracking:** detailed statistics per subject (Total Classes, Present, Absent, Percentage).
* **Academic Results:** View semester marks and download **Official Result PDFs**.
* **Fee Status:** Real-time status for Tuition, Hostel, and Library fees.
* **Class Schedule:** Weekly time table visualization.
* **Course Management:** List of enrolled subjects for the current semester.

### 👩‍🏫 Teacher
* **Class Management:** View assigned subjects and classes.
* **Mark Attendance:** Digital interface to record student attendance.
* **Student Verification:** Approve new student registrations.

### 👨‍💼 Admin
* **Faculty Management:** View, filter, and manage faculty members by branch.
* **Student Management:** Search and manage students by Year and Branch.
* **Academic Configuration:**
    * **Manage Subjects:** Add and map subjects to specific branches and years.
    * **Manage Branches:** Configure department/branch details.
* **Approvals:** Review and approve teacher registrations.
* **Notices:** Broadcast announcements to students and staff.

---

## 🛠️ Tech Stack

* **Backend:** Python 3, Flask (Blueprints architecture)
* **Database:** MongoDB (PyMongo)
* **Authentication:** JWT (JSON Web Tokens)
* **PDF Generation:** ReportLab
* **Frontend:** HTML5, CSS3, JavaScript
* **Deployment:** Render / Gunicorn

---

## ⚙️ Local Installation & Setup

### 1. Prerequisites
* Python 3.11+
* MongoDB (installed locally or a cloud URI)

### 2. Clone the Repository
```bash
git clone [https://github.com/ridham19/unimis.git](https://github.com/ridham19/unimis.git)
cd unimis
```
3. Install Dependencies
```Bash

pip install -r backend/requirements.txt
```
4. Configuration
Set up your environment variables. You can create a .env file or export them directly:

```Bash

export MONGO_URI="mongodb://localhost:27017/"
```
5. Seed the Database
Initialize your database with admin users, branches, and subjects using the provided scripts:

```Bash

# Create Admin User
python backend/seed_admin.py

# Populate Initial Data (Optional)
python backend/seed_branches.py
python backend/seed_subjects.py
```
6. Run the Application
```Bash

python backend/app.py
```
Visit http://localhost:5000 in your browser.

📂 Project Structure
```Plaintext

unimis/
├── backend/
│   ├── app.py              # Application entry point
│   ├── config.py           # Configuration settings
│   ├── models/             # Database models (User, Marks, Attendance, etc.)
│   ├── routes/             # API Blueprints (Auth, Admin, Student, etc.)
│   ├── utils/              # Utilities (PDF Generator)
│   └── seed_*.py           # Database seeding scripts
├── frontend/
│   ├── index.html          # Landing page
│   ├── dashboard.html      # Main dashboard interface
│   ├── css/                # Stylesheets
│   └── js/                 # Frontend logic (API calls, UI updates)
└── README.md
```
