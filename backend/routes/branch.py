from flask import Blueprint, request, jsonify
from models.branch import create_branch, get_all_branches, delete_branch
from middleware.auth_middleware import token_required, role_required

branch_bp = Blueprint('branch', __name__)

@branch_bp.route('/branches', methods=['GET'])
def get_branches():
    branches = get_all_branches(request.db)
    return jsonify(branches)

@branch_bp.route('/branches', methods=['POST'])
@token_required
@role_required(['admin'])
def add_branch():
    data = request.json
    create_branch(request.db, data['name'], data['code'])
    return jsonify({'message': 'Branch added successfully'})

@branch_bp.route('/branches/<code>', methods=['DELETE'])
@token_required
@role_required(['admin'])
def remove_branch(code):
    delete_branch(request.db, code)
    return jsonify({'message': 'Branch removed'})