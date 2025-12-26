from flask import Blueprint, request, jsonify
from models.user import find_user_by_email, create_user
import jwt
import datetime

auth_bp = Blueprint('auth', __name__)
SECRET_KEY = "your_secret_key"

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    
    # Check if user already exists
    if find_user_by_email(request.db, data['email']):
        return jsonify({'error': 'Email already exists'}), 400

    # Create new user (is_approved will be False by default)
    create_user(request.db, data['name'], data['email'], data['password'], data['role'])
    
    return jsonify({'message': 'Registration successful. Please wait for approval.'})

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = find_user_by_email(request.db, data['email'])

    if user and user['password'] == data['password']:
        # --- NEW: Check Approval Status ---
        if not user.get('is_approved', False):
            return jsonify({'error': 'Account not approved yet. Contact your Administrator/Teacher.'}), 403

        token = jwt.encode({
            'user_id': str(user['_id']),
            'role': user['role'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
        }, SECRET_KEY, algorithm='HS256')
        
        if isinstance(token, bytes): token = token.decode('utf-8')
        return jsonify({'token': token})

    return jsonify({'error': 'Invalid credentials'}), 401