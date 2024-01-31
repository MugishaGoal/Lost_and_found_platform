#!/usr/bin/python3

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

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
    fullname = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    registration_date = db.Column(db.DateTime, default=datetime.utcnow)

    # Define relationships
    reported_items = db.relationship('LostItem', backref='reporter', lazy=True)
    item_images = db.relationship('ItemImage', backref='uploader', lazy=True)
    notifications = db.relationship('Notification', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.fullname}', '{self.email}')"

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


class ItemCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)


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
    category_id = db.Column(db.Integer, db.ForeignKey('ItemCategory.id'), nullable=True)
    category = db.relationship('ItemCategory', backref='LostItem', lazy=True)
    lost_location_id = db.Column(db.Integer, db.ForeignKey('LostLocation.id'), nullable=False)
    date_lost = db.Column(db.DateTime, default=datetime.utcnow)
    is_found = db.Column(db.Boolean, default=False)
    file_path = db.Column(db.String(255), nullable=True)  # New field for file path

    # Define relationships
    reporter_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    item_images = db.relationship('ItemImage', backref='LostItem', lazy=True)
    location = db.relationship('LostLocation', backref='LostItem', lazy=True)
    notifications = db.relationship('Notification', backref='LostItem', lazy=True)

    def save_to_db(self):
        """
        Save the lost item to the database.
        """
        db.session.add(self)
        db.session.commit()


class ItemImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('LostItem.id'), nullable=False)
    file_path = db.Column(db.LargeBinary, nullable=True)

class LostLocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street_address = db.Column(db.String(255), nullable=False)
    cell = db.Column(db.String(100), nullable=False)
    sector = db.Column(db.String(100), nullable=False)
    district = db.Column(db.String(100), nullable=False)
    province = db.Column(db.String(100), nullable=False)

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('LostItem.id'), nullable=False)
    notification_type = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
