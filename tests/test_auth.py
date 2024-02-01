#!/usr/bin/python3

import os, unittest
from flask import Flask
from app import db
from auth.forms import RegistrationForm, LoginForm
from auth.routes import auth_bp
from models import User

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment.
        """
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.config['SQLALCHEMY_DATABASE_URI'] =  os.getenv('DATABASE_URL')
        self.app.register_blueprint(auth_bp)
        self.client = self.app.test_client()

        # Create all tables in the database
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """
        Tear down the test environment.
        """
        with self.app.app_context():
            db.drop_all()

    def test_registration_form(self):
        """
        Test user registration form validation.
        """
        with self.app.app_context():
            form = RegistrationForm()
            form.full_name.data = 'John Doe'
            form.email.data = 'john@example.com'
            form.password.data = 'password123'
            form.confirm_password.data = 'password123'

            self.assertTrue(form.validate())

    def test_registration_route(self):
        """
        Test user registration route.
        """
        with self.app.app_context():
            response = self.client.post('/register', data=dict(
                full_name='John Doe',
                email='john@example.com',
                password='password123',
                confirm_password='password123'
            ), follow_redirects=True)

            self.assertIn(b'Registration successful!', response.data)

    def test_login_form(self):
        """
        Test user login form validation.
        """
        with self.app.app_context():
            form = LoginForm()
            form.email.data = 'john@example.com'
            form.password.data = 'password123'

            self.assertTrue(form.validate())

    def test_login_route(self):
        """
        Test user login route.
        """
        with self.app.app_context():
            # Register a user first
            user = User(fullname='John Doe', email='john@example.com')
            user.set_password('password123')
            db.session.add(user)
            db.session.commit()

            # Test login with correct credentials
            response = self.client.post('/login', data=dict(
                email='john@example.com',
                password='password123'
            ), follow_redirects=True)

            self.assertIn(b'Login successful!', response.data)

            # Test login with incorrect credentials
            response = self.client.post('/login', data=dict(
                email='john@example.com',
                password='wrongpassword'
            ), follow_redirects=True)

            self.assertIn(b'Invalid email or password. Please try again.', response.data)

    def test_logout_route(self):
        """
        Test user logout route.
        """
        with self.app.app_context():
            # Log in a user first
            user = User(fullname='John Doe', email='john@example.com')
            user.set_password('password123')
            db.session.add(user)
            db.session.commit()

            response = self.client.post('/login', data=dict(
                email='john@example.com',
                password='password123'
            ), follow_redirects=True)

            # Test logout
            response = self.client.get('/logout', follow_redirects=True)
            self.assertIn(b'You have been logged out.', response.data)

if __name__ == '__main__':
    unittest.main()
