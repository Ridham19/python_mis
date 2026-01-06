def init_indexes(db):
    try:
        # User Indexes
        db.users.create_index("email", unique=True)
        db.users.create_index("admission_number", unique=True, sparse=True)
        
        # Branch Indexes
        db.branches.create_index("code", unique=True)
        
        # Subject Indexes
        db.subjects.create_index("code", unique=True)
        
        print("Database indexes ensured.")
    except Exception as e:
        print(f"Error creating indexes: {e}")
