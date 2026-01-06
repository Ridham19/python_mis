from functools import wraps
from flask import request, jsonify
import jwt
from config import JWT_SECRET

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            data = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
            # Inject current user context if needed, e.g.
            # request.current_user_id = data['user_id']
            # request.current_user_role = data['role']
            request.user_token_data = data
        except Exception as e:
            return jsonify({'message': 'Token is invalid!', 'error': str(e)}), 401
            
        return f(*args, **kwargs)
    return decorated

def role_required(allowed_roles):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            # Ensure token_required was called first
            if not hasattr(request, 'user_token_data'):
                return jsonify({'message': 'Authorization context missing'}), 500
                
            user_role = request.user_token_data.get('role')
            if user_role not in allowed_roles:
                return jsonify({'message': 'Permission denied!'}), 403
                
            return f(*args, **kwargs)
        return decorated
    return decorator
