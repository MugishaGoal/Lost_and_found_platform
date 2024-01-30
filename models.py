#!/usr/bin/python3

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, UserMixin):
    """
    Represents a user in the Lost and Found platform.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user.
        email (str): The email address of the user.
        password_hash (str): The hashed password of the user.
        registration_date (datetime): The date and time when the user registered.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    registration_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    def set_password(self, password):
        """Set the user's password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check if the provided password matches the user's password."""
        return check_password_hash(self.password_hash, password)


"""New function for Flask-Login to load a user by ID"""
@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class LostItem(db.Model):
    """
    Represents a lost item in the Lost and Found platform.

    Attributes:
        id (int): The unique identifier for the lost item.
        item_name (str): The name of the lost item.
        description (str): A description of the lost item.
        category (str): The category of the lost item.
        lost_location (str): The location where the item was lost.
        date_lost (datetime): The date and time when the item was lost.
        is_found (bool): Indicates whether the item has been found.
        file_path (str): The file path of an uploaded image or document.
    """
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    category = db.Column(db.String(100), nullable=True)
    lost_location = db.Column(db.String(255), nullable=False)
    date_lost = db.Column(db.DateTime, default=datetime.utcnow)
    is_found = db.Column(db.Boolean, default=False)
    file_path = db.Column(db.String(255), nullable=True)  # New field for file path

    def save_to_db(self):
        """
        Save the lost item to the database.
        """
        db.session.add(self)
        db.session.commit()
