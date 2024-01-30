#!/usr/bin/python3

# routes.py

from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename
import os

from .models import db, LostItem

items_bp = Blueprint('items', __name__)

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
