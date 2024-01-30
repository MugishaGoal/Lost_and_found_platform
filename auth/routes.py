#!/usr/bin/python3

from flask import render_template, redirect, url_for, flash, session
from your_flask_app import app
from .forms import RegistrationForm, LoginForm

# Dummy user data (to be replaced with the database logic)
dummy_users = [
    {'full_name': 'John Doe', 'email': 'john@example.com', 'password': 'password123'},
    {'full_name': 'Alice Smith', 'email': 'alice@example.com', 'password': 'password456'}
]

@app.route('/register', methods=['GET', 'POST'])
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
        # Dummy registration logic (To be replaced with the database logic)
        session['user'] = {'full_name': form.full_name.data, 'email': form.email.data}
        flash('Registration successful!', 'success')
        return redirect(url_for('index'))

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
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
        # Dummy login logic (Replace with your database logic)
        user = next((u for u in dummy_users if u['email'] == form.email.data and u['password'] == form.password.data), None)

        if user:
            session['user'] = {'full_name': user['full_name'], 'email': user['email']}
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password. Please try again.', 'danger')

    return render_template('login.html', form=form)

@app.route('/logout')
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
