#!/usr/bin/python3

import os

def create_uploads_directory(app):
    # Check if the 'uploads' directory exists, create it if not
    uploads_directory = os.path.join(app.root_path, 'static', 'uploads')
    if not os.path.exists(uploads_directory):
        os.makedirs(uploads_directory)

    return uploads_directory
