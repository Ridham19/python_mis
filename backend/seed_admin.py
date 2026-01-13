from pymongo import MongoClient
import os

# --- CONFIGURATION ---
# REPLACE THIS with your actual MongoDB connection string
MONGO_URI = "your url"

def seed_admin():
    try:

        client = MongoClient(MONGO_URI)
        db = client.get_database("circuit_project_db")
        users_collection = db.users
        
        print("✅ Connected to MongoDB.")


        admin_id = "Admin"
        plain_password = "admin"
        

        admin_user = {
            "user_id": admin_id,
            "password": plain_password,
            "role": "admin"
        }


        result = users_collection.update_one(
            {"user_id": admin_id},    # Filter
            {"$set": admin_user},     # Update
            upsert=True               # Create if doesn't exist
        )

        if result.upserted_id:
            print(f"🎉 Success! Admin user '{admin_id}' created.")
        else:
            print(f"🔄 Success! Admin user '{admin_id}' updated.")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    seed_admin()