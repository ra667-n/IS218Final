from flask import Blueprint, request, jsonify
from flask_jwtextended import create_access_token, jwt_required
from app import db
from app.models import User 

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

auth_bp.route('/register', methods=['POST'])
def register():
    # Implement registration logic 

    auth_bp.route('/login', methods=['POST'])
def login():
    # Implement login logic 
