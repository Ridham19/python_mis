from flask import Blueprint, request, jsonify
from models.user import create_user, get_user_by_id, get_pending_users_by_role, approve_user_by_id
from bson import ObjectId

user_bp = Blueprint('user', __name__)

@user_bp.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = get_user_by_id(request.db, ObjectId(user_id))
        if user:
            user['_id'] = str(user['_id'])
            # Don't send password back
            user.pop('password', None)
            return jsonify(user)
        return jsonify({'error': 'User not found'}), 404
    except:
        return jsonify({'error': 'Invalid ID'}), 400

# --- New Approval Routes ---

@user_bp.route('/users/pending/<role>', methods=['GET'])
def get_pending(role):
    # Security: In a real app, check if requester is Admin or Teacher here
    users = get_pending_users_by_role(request.db, role)
    for u in users:
        u['_id'] = str(u['_id'])
        u.pop('password', None)
    return jsonify(users)

@user_bp.route('/users/approve/<user_id>', methods=['POST'])
def approve(user_id):
    approve_user_by_id(request.db, user_id)
    return jsonify({'message': 'User approved'})