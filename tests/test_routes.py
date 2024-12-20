import unittest
from app import create_app
from flask import json
import pytest

class TestUserViews(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_get_user(self):
        # Assuming you have a test client with a valid JWT access token
        response = self.client.get('/users/me', headers={'Authorization': 'Bearer your_test_token'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('id', data)
        self.assertIn('username', data)
        self.assertIn('email', data)

    def test_update_user(self):
        # Assuming you have a test client with a valid JWT access token
        response = self.client.put('/users/me', 
                                  headers={'Authorization': 'Bearer your_test_token'}, 
                                  json={'name': 'Test User'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'Test User')

    def test_upgrade_user(self):
        # Assuming you have a test client with a valid JWT access token and admin/manager role
        response = self.client.put('/users/1/upgrade', 
                                  headers={'Authorization': 'Bearer your_test_token'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'User upgraded to professional')

if __name__ == '__main__':
    unittest.main()
