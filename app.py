#!/usr/bin/python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from file_handler import create_uploads_directory
import os

# Loads environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configures the Flask app
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initializes SQLAlchemy
db = SQLAlchemy(app)

# Creates the 'uploads' directory and get its path
uploads_directory = create_uploads_directory(app)

# Imports models
from models import User, ItemCategory, LostItem, ItemImage, LostLocation, Notification

# Imports routes from components
from auth.routes import auth_bp
from items.routes import items_bp, item_images_bp, lost_locations_bp
from notifications.routes import notifications_bp
from user_prof.routes import users_bp

# Registers blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(items_bp)
app.register_blueprint(item_images_bp)
app.register_blueprint(lost_locations_bp)
app.register_blueprint(notifications_bp)
app.register_blueprint(users_bp)

if __name__ == '__main__':
    app.run(debug=True)
