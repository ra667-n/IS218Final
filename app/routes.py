from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import User
from app.schemas import UserSchema

user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('/me', methods=['GET'])
@jwt_required()
def get_user():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    user_schema = UserSchema()
    return jsonify(user_schema.dump(user))

@user_bp.route('/me', methods=['PUT'])
@jwt_required()
def update_user():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    user_data = request.get_json()
    for key, value in user_data.items():
        setattr(user, key, value)
    db.session.commit()
    user_schema = UserSchema()
    return jsonify(user_schema.dump(user))

@user_bp.route('/<int:user_id>/upgrade', methods=['PUT'])
@jwt_required() 
def upgrade_user(user_id):
    # Add authorization check for managers/admins
    user = User.query.get_or_404(user_id)
    user.is_professional = True
    db.session.commit()
    return jsonify({'message': 'User upgraded to professional'})

@app.route('/api/user/profile', methods=['PUT'])
def update_profile():
    # Logic to update user profile fields

@app.route('/api/user/upgrade', methods=['POST'])
@admin_required
def upgrade_user():
    # Logic to upgrade user to professional status
