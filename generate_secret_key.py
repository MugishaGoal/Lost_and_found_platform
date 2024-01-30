#!/usr/bin/python3
import os
import secrets

# Generate a random secret key
secret_key = secrets.token_hex(16)

# Path to config.py
config_file_path = 'config.py'

# Write the secret key to config.py
with open(config_file_path, 'w') as config_file:
    config_file.write(f"SECRET_KEY = '{secret_key}'\n")

print(f"Random secret key generated and saved to {config_file_path}")
