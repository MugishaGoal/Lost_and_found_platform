#!/usr/bin/python3

from app import db
from flask import render_template, Blueprint, redirect, url_for, flash, session
from .forms import RegistrationForm, LoginForm
from ..models import User

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle user registration.

    - GET: Render the registration form.
    - POST: Process the form data and register the user.

    Returns:
        - If successful: Redirect to the index page.
        - If form validation fails: Render the registration form.
    """
    form = RegistrationForm()

    if form.validate_on_submit():
        # Checks if the Use ris registered
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email address is already registered. Please use a different email.', 'danger')
            return render_template('register.html', form=form)

        # Creates a New User
        new_user = User(fullname=form.full_name.data, email=form.email.data)
        new_user.set_password(form.password.data)

        # Adds a User to the Database
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful!', 'success')
        return redirect(url_for('index'))

    return render_template('register.html', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle user login.

    - GET: Render the login form.
    - POST: Process the form data and log in the user.

    Returns:
        - If successful: Redirect to the index page.
        - If form validation fails or login fails: Render the login form.
    """
    form = LoginForm()

    if form.validate_on_submit():
        # Checks if the user exists
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
             session['user'] = {'full_name': user.fullname, 'email': user.email}
             flash('Login successful!', 'success')
             return redirect(url_for('index'))
        else:
            flash('Invalid email or password. Please try again.', 'danger')

    return render_template('login.html', form=form)


@auth_bp.route('/logout')
def logout():
    """
    Handle user logout.

    Clears the session and redirects to the index page.

    Returns:
        Redirect to the index page.
    """
    session.pop('user', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))
