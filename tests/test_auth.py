import unittest
from app import create_app
from flask import json

class TestAuth(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_register(self):
        response = self.client.post('/auth/register', 
                                   json={'username': 'testuser', 'email': 'test@example.com', 'password': 'password'})
        self.assertEqual(response.status_code, 201) 

    def test_login(self):
        # Register a user first
        self.client.post('/auth/register', 
                         json={'username': 'testuser', 'email': 'test@example.com', 'password': 'password'})
        response = self.client.post('/auth/login', 
                                   json={'username': 'testuser', 'password': 'password'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('access_token', data)

if __name__ == '__main__':
    unittest.main()
