#!/usr/bin/python3

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class UserProfileViewForm(FlaskForm):
    """
    Form for viewing user profile.
    """
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Edit Profile')

class UserProfileEditForm(FlaskForm):
    """
    Form for editing user profile.
    """
    new_username = StringField('New Username', validators=[DataRequired(), Length(min=4, max=100)])
    new_email = StringField('New Email', validators=[DataRequired(), Email()])
    new_password = PasswordField('New Password', validators=[Length(min=6)])
    confirm_new_password = PasswordField('Confirm New Password', validators=[EqualTo('new_password')])
    submit = SubmitField('Save Changes')
