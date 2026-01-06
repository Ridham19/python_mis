import os
from dotenv import load_dotenv

load_dotenv()

# Roles
ROLES = ["student", "teacher", "hod", "dean", "admin"]

# Secrets
JWT_SECRET = os.getenv("JWT_SECRET", "your-secret-key")
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")

# Config
TOKEN_EXPIRY = 3600