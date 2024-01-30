#!/usr/bin/python3

from flask import Blueprint, jsonify, request
from models import db, Notification

notifications_bp = Blueprint('notifications', __name__)

@notifications_bp.route('/api/notifications', methods=['GET'])
def get_notifications():
    """
    Retrieve notifications for the authenticated user.

    Returns:
        jsonify: A JSON response containing the list of notifications.
    """
    user_id = current_user.id  # Assuming you're using Flask-Login for user authentication
    notifications = Notification.query.filter_by(user_id=user_id).all()

    notifications_list = [{
        'id': notification.id,
        'item_id': notification.item_id,
        'notification_type': notification.notification_type,
        'timestamp': notification.timestamp.strftime('%Y-%m-%d %H:%M:%S')
    } for notification in notifications]

    return jsonify({'notifications': notifications_list})

@notifications_bp.route('/api/notifications/<int:notification_id>', methods=['DELETE'])
def delete_notification(notification_id):
    """
    Delete a specific notification.

    Args:
        notification_id (int): The ID of the notification.

    Returns:
        jsonify: A JSON response indicating the status of the operation.
    """
    notification = Notification.query.get_or_404(notification_id)

    if notification:
        db.session.delete(notification)
        db.session.commit()
        return jsonify({'message': 'Notification deleted successfully'})
    else:
        return jsonify({'error': 'Notification not found'}), 404
