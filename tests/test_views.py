import unittest
from app import create_app, db
from app.models import User
from flask import json
from unittest.mock import patch  # For mocking external dependencies
import pytest
from app.extensions import jwt # Import jwt from extensions

# Mock JWT token generation (replace with your actual token generation logic for tests)
def generate_test_token(user_id):
    with create_app('testing').app_context():
        access_token = jwt.create_access_token(identity=user_id)
    return access_token
    #return "test_token"  # Replace with your actual token generation

class TestUserViews(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all() # ensure database is created for tests
        # Create a test user
        test_user = User(username='testuser', email='test@example.com')
        db.session.add(test_user)
        db.session.commit()
        self.test_user_id = test_user.id
        self.test_token = generate_test_token(self.test_user_id)
        # Create a test admin user
        test_admin = User(username='testadmin', email='testadmin@example.com', is_professional=True)
        db.session.add(test_admin)
        db.session.commit()
        self.test_admin_id = test_admin.id
        self.test_admin_token = generate_test_token(self.test_admin_id)


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
