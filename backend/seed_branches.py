from pymongo import MongoClient

def seed_branches():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["student_management_v2"]
    
    branches = [
        {"name": "Computer Science", "code": "CS"},
        {"name": "Mechanical Engineering", "code": "ME"},
        {"name": "Civil Engineering", "code": "CE"},
        {"name": "Electrical Engineering", "code": "EE"}
    ]
    
    for b in branches:
        if not db.branches.find_one({"code": b["code"]}):
            db.branches.insert_one(b)
            print(f"Added {b['name']}")
        else:
            print(f"Skipped {b['name']} (Exists)")

if __name__ == "__main__":
    seed_branches()
