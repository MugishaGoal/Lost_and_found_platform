#!/usr/bin/python3

from flask import Blueprint, render_template, redirect, url_for, flash
from flask import jsonify, request
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os

from models import db, LostItem, ItemImage
from items.forms import ItemImageForm

items_bp = Blueprint('items', __name__)
item_images_bp = Blueprint('item_images', __name__)


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'doc', 'docx'}

def allowed_file(filename):
    """
    Check if the file extension is allowed.

    Args:
        filename (str): The name of the file.

    Returns:
        bool: True if the file extension is allowed, False otherwise.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@items_bp.route('/api/items', methods=['POST'])
def create_lost_item():
    """
    Create a new lost item.

    Returns:
        jsonify: A JSON response indicating the status of the operation.
    """
    data = request.form

    new_item = LostItem(
        item_name=data.get('item_name'),
        description=data.get('description'),
        category=data.get('category'),
        lost_location=data.get('lost_location')
    )

    file = request.files.get('file')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join('uploads', filename))
        new_item.file_path = filename

    new_item.save_to_db()

    return jsonify({'message': 'Lost item created successfully'}), 201


@items_bp.route('/api/items', methods=['GET'])
def get_lost_items():
    """
    Retrieve a list of lost items.

    Returns:
        jsonify: A JSON response containing the list of lost items.
    """
    lost_items = LostItem.query.all()
    items_list = []

    for item in lost_items:
        items_list.append({
            'id': item.id,
            'item_name': item.item_name,
            'description': item.description,
            'category': item.category,
            'lost_location': item.lost_location,
            'date_lost': item.date_lost.strftime('%Y-%m-%d %H:%M:%S'),
            'is_found': item.is_found,
            'file_path': item.file_path
        })

    return jsonify({'lost_items': items_list})


@items_bp.route('/api/items/<int:item_id>', methods=['PUT'])
def update_lost_item(item_id):
    """
    Update details of a specific lost item.

    Args:
        item_id (int): The ID of the lost item.

    Returns:
        jsonify: A JSON response indicating the status of the operation.
    """
    item = LostItem.query.get(item_id)

    if item:
        data = request.form
        item.item_name = data.get('item_name', item.item_name)
        item.description = data.get('description', item.description)
        item.category = data.get('category', item.category)
        item.lost_location = data.get('lost_location', item.lost_location)
        
        file = request.files.get('file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('uploads', filename))
            item.file_path = filename

        db.session.commit()
        return jsonify({'message': 'Lost item updated successfully'})
    else:
        return jsonify({'error': 'Lost item not found'}), 404


@items_bp.route('/api/items/<int:item_id>/found', methods=['PATCH'])
def mark_item_as_found(item_id):
    """
    Mark a lost item as found.

    Args:
        item_id (int): The ID of the lost item.

    Returns:
        jsonify: A JSON response indicating the status of the operation.
    """
    item = LostItem.query.get(item_id)

    if item:
        item.is_found = True
        db.session.commit()
        return jsonify({'message': 'Lost item marked as found'})
    else:
        return jsonify({'error': 'Lost item not found'}), 404


@items_bp.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_lost_item(item_id):
    """
    Delete a specific lost item.

    Args:
        item_id (int): The ID of the lost item.

    Returns:
        jsonify: A JSON response indicating the status of the operation.
    """
    item = LostItem.query.get(item_id)

    if item:
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'Lost item deleted successfully'})
    else:
        return jsonify({'error': 'Lost item not found'}), 404


@item_images_bp.route('/upload_image/<int:item_id>', methods=['GET', 'POST'])
@login_required
def upload_image(item_id):
    form = ItemImageForm()

    if form.validate_on_submit():
        # Save the image to the database
        image = form.image.data
        item_image = ItemImage(item_id=item_id, image=image.read())
        db.session.add(item_image)
        db.session.commit()

        flash('Image uploaded successfully!', 'success')
        return redirect(url_for('items.item_details', item_id=item_id))

    return render_template('items/upload_image.html', form=form)


@lost_locations_bp.route('', methods=['GET'])
def get_all_lost_locations(item_id):
    item = LostItem.query.get_or_404(item_id)
    locations = item.locations.all()
    locations_json = [location.to_dict() for location in locations]
    return jsonify(locations_json)

@lost_locations_bp.route('/<int:location_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_lost_location(item_id, location_id):
    item = LostItem.query.get_or_404(item_id)
    location = LostLocation.query.get_or_404(location_id)

    if request.method == 'GET':
        return jsonify(location.to_dict())

    elif request.method == 'PUT':
        data = request.get_json()
        # Update location details based on request data
        location.street_address = data.get('street_address', location.street_address)
        location.cell = data.get('cell', location.cell)
        location.sector = data.get('sector', location.sector)
        location.district = data.get('district', location.district)
        location.province = data.get('province', location.province)
        db.session.commit()
        return jsonify({'message': 'Location updated successfully'})

    elif request.method == 'DELETE':
        db.session.delete(location)
        db.session.commit()
        return jsonify({'message': 'Location deleted successfully'})

@lost_locations_bp.route('', methods=['POST'])
def create_lost_location(item_id):
    item = LostItem.query.get_or_404(item_id)
    data = request.get_json()

    # Create a new lost location for the item
    location = LostLocation(
        street_address=data['street_address'],
        cell=data['cell'],
        secto
