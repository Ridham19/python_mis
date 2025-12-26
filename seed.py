from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["student_management"]

print("--- Seeding Database ---")

# 1. Define Users
users = [
    {
        "name": "Ridham Student",
        "email": "student@example.com",
        "password": "password123",
        "role": "student",
        "is_approved": True
    },
    {
        "name": "Ridham Teacher",
        "email": "teacher@example.com",
        "password": "admin",
        "role": "teacher",
        "is_approved": True
    },
    {
        "name": "Super Admin",
        "email": "admin@school.com",
        "password": "adminpassword",
        "role": "admin",
        "is_approved": True
    }
]

# 2. Insert Users (if they don't exist)
for user in users:
    if not db.users.find_one({"email": user["email"]}):
        result = db.users.insert_one(user)
        print(f"Created {user['role']}: {user['email']} (ID: {result.inserted_id})")
    else:
        # If user exists, ensure they are approved (fixes old data)
        db.users.update_one(
            {"email": user["email"]}, 
            {"$set": {"is_approved": True, "role": user["role"]}}
        )
        print(f"Updated/Verified {user['role']}: {user['email']}")

# 3. Add Dummy Marks for the Student
student_record = db.users.find_one({"email": "student@example.com"})
if student_record:
    # Check if marks already exist to avoid duplicates
    if not db.marks.find_one({"student_id": str(student_record["_id"])}):
        db.marks.insert_many([
            {"student_id": str(student_record["_id"]), "subject": "Mathematics", "score": 95},
            {"student_id": str(student_record["_id"]), "subject": "Physics", "score": 88},
            {"student_id": str(student_record["_id"]), "subject": "Computer Science", "score": 92}
        ])
        print("Dummy marks added for Student.")
    else:
        print("Marks already exist.")

print("--- Database Seeded Successfully ---")
print("Login Credentials:")
print("1. Student: student@example.com / password123")
print("2. Teacher: teacher@example.com / admin")
print("3. Admin:   admin@school.com    / adminpassword")