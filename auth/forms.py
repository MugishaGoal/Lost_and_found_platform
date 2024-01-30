#!/usr/bin/python3

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    """
    Form for user registration.

    Attributes:
        full_name (StringField): Full name of the user.
        email (StringField): Email address of the user.
        password (PasswordField): Password for the user.
        confirm_password (PasswordField): Confirmation of the password.
        submit (SubmitField): Submit button for the registration form.
    """
    full_name = StringField('Full Name', validators=[DataRequired(), Length(min=4, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    """
    Form for user login.

    Attributes:
        email (StringField): Email address of the user.
        password (PasswordField): Password for the user.
        submit (SubmitField): Submit button for the login form.
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
