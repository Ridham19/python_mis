from flask import Blueprint, request, jsonify
from models.notice import create_notice, get_notices_for_role

notice_bp = Blueprint('notice', __name__)

@notice_bp.route('/notice', methods=['POST'])
def create():
    data = request.json
    # Ensure visible_to is a list
    visible_to = data.get('visible_to', [])
    if isinstance(visible_to, str):
        visible_to = [visible_to]
        
    result = create_notice(request.db, data['title'], data['content'], visible_to)
    return jsonify({'inserted_id': str(result.inserted_id)})

@notice_bp.route('/notice/<role>', methods=['GET'])
def get(role):
    notices = get_notices_for_role(request.db, role)
    # Fix: Convert ObjectId to string
    for notice in notices:
        notice['_id'] = str(notice['_id'])
    return jsonify(notices)