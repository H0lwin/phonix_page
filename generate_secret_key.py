#!/usr/bin/env python3
"""
Script to generate a secure Django secret key
"""

import secrets
import string

def generate_secret_key(length=50):
    """Generate a secure Django secret key"""
    chars = string.ascii_letters + string.digits + string.punctuation
    # Remove quotes and backslashes to avoid issues in .env files
    chars = chars.replace('"', '').replace("'", '').replace('\\', '')
    return ''.join(secrets.choice(chars) for _ in range(length))

if __name__ == "__main__":
    secret_key = generate_secret_key()
    print(f"SECRET_KEY={secret_key}")