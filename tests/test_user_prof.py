#!/usr/bin/python3

import os, unittest
from flask import Flask, session
from flask_testing import TestCase
from app import db
from user_prof.routes import users_bp
from models import User

class UserProfileTestCase(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.register_blueprint(users_bp)

        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_view_profile(self):
        # Create a test user
        test_user = User(username='test_user', email='test@example.com')
        db.session.add(test_user)
        db.session.commit()

        # Log in the test user
        with self.client as client:
            client.post('/login', data=dict(email='test@example.com', password='password'))

        # Access the user profile page
        response = self.client.get('/profile', follow_redirects=True)

        # Check if the response contains the username of the test user
        self.assertIn(b'test_user', response.data)

    def test_edit_profile(self):
        # Create a test user
        test_user = User(username='test_user', email='test@example.com')
        db.session.add(test_user)
        db.session.commit()

        # Log in the test user
        with self.client as client:
            client.post('/login', data=dict(email='test@example.com', password='password'))

        # Access the edit profile page
        response = self.client.get('/profile/edit')
        self.assertEqual(response.status_code, 200)

        # Edit the profile
        response = self.client.post('/profile/edit', data=dict(new_username='new_test_user', new_email='new_test@example.com', new_password='new_password', confirm_new_password='new_password'))

        # Check if the profile is updated successfully
        self.assertIn(b'Profile updated successfully', response.data)

if __name__ == '__main__':
    unittest.main()
