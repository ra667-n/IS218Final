import unittest
from app import db, create_app
from app.models import User

class TestUserModel(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_user(self):
        user = User(username='testuser', email='test@example.com')
        db.session.add(user)
        db.session.commit()
        self.assertIsNotNone(user.id)

    def test_user_repr(self):
        user = User(username='testuser', email='test@example.com')
        self.assertEqual(str(user), '<User testuser>')

    def test_user_is_professional(self):
        user = User(username='testuser', email='test@example.com', is_professional=True)
        db.session.add(user)
        db.session.commit()
        self.assertTrue(user.is_professional)

if __name__ == '__main__':
    unittest.main()
