#!/usr/bin/python3

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class CreateItemForm(FlaskForm):
    # Form for creating a new lost item
    item_name = StringField('Item Name', validators=[DataRequired(), Length(min=1, max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    lost_location = StringField('Lost Location', validators=[DataRequired()])
    date_lost = StringField('Date Lost', validators=[DataRequired()])
    submit = SubmitField('Create Item')

class UpdateItemForm(FlaskForm):
    # Form for updating item details
    item_name = StringField('Item Name', validators=[DataRequired(), Length(min=1, max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    lost_location = StringField('Lost Location', validators=[DataRequired()])
    date_lost = StringField('Date Lost', validators=[DataRequired()])
    submit = SubmitField('Update Item')

class MarkAsFoundForm(FlaskForm):
    # Form for marking an item as found
    submit = SubmitField('Mark as Found')

class DeleteItemForm(FlaskForm):
    # Form for deleting an item
    submit = SubmitField('Delete Item')

    class ItemImageForm(FlaskForm):
    # Add fields for image upload form
    image = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'], 'Images only!')])
    submit = SubmitField('Upload')
