#!/usr/bin/python3

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from .forms import UserProfileViewForm, UserProfileEditForm
from .models import User
from app import db

users_bp = Blueprint('users', __name__)

@users_bp.route('/profile', methods=['GET'])
@login_required
def view_profile():
    """View user profile."""
    form = UserProfileViewForm(obj=current_user)
    return render_template('users/profile.html', form=form)

@users_bp.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    """Edit user profile."""
    form = UserProfileEditForm()

    if form.validate_on_submit():
        current_user.username = form.new_username.data
        current_user.email = form.new_email.data

        if form.new_password.data:
            current_user.set_password(form.new_password.data)

        db.session.commit()
        flash('Profile updated successfully', 'success')
        return redirect(url_for('users.view_profile'))

    # Populate the form with current user details
    form.new_username.data = current_user.username
    form.new_email.data = current_user.email

    return render_template('users/edit_profile.html', form=form)
