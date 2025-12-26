from bson import ObjectId

def create_user(db, name, email, password, role):
    # Default is_approved to False for everyone except maybe the first admin (handled manually)
    user = {
        "name": name,
        "email": email,
        "password": password, 
        "role": role,
        "is_approved": False  # New Flag
    }
    return db.users.insert_one(user)

def find_user_by_email(db, email):
    return db.users.find_one({"email": email})

def get_user_by_id(db, user_id):
    try:
        return db.users.find_one({"_id": user_id})
    except:
        return None

# --- New Functions for Approval System ---
def get_pending_users_by_role(db, role):
    # Find users of a specific role who are NOT approved
    return list(db.users.find({"role": role, "is_approved": False}))

def approve_user_by_id(db, user_id):
    return db.users.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {"is_approved": True}}
    )