import unittest
from flask import json
from app import app, db, bcrypt  # Replace with your actual app name
from src.models.user import User  # Replace with your actual model name

class TestLoginRoute(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_login_with_valid_credentials(self):
        user = User(username='testuser', password=bcrypt.generate_password_hash('testpassword').decode('utf-8'))
        db.session.add(user)
        db.session.commit()

        response = self.app.post('/login', data=json.dumps({'username': 'testuser', 'password': 'testpassword'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', json.loads(response.data))

    def test_login_with_invalid_username(self):
        response = self.app.post('/login', data=json.dumps({'username': 'invaliduser', 'password': 'testpassword'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data.decode('utf-8'), 'Wrong username or password')

    def test_login_with_invalid_password(self):
        user = User(username='testuser', password=bcrypt.generate_password_hash('testpassword').decode('utf-8'))
        db.session.add(user)
        db.session.commit()

        response = self.app.post('/login', data=json.dumps({'username': 'testuser', 'password': 'invalidpassword'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data.decode('utf-8'), 'Wrong username or password')

    def test_login_with_empty_username(self):
        response = self.app.post('/login', data=json.dumps({'username': '', 'password': 'testpassword'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data.decode('utf-8'), 'Wrong username or password')

    def test_login_with_empty_password(self):
        response = self.app.post('/login', data=json.dumps({'username': 'testuser', 'password': ''}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data.decode('utf-8'), 'Wrong username or password')

    def test_login_with_invalid_route(self):
        response = self.app.get('/invalid_route')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()