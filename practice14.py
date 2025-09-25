#!/usr/bin/env python3
"""
login_system.py - Simple login system with user dictionary and functions
"""

import getpass

# Dictionary to store users
# Format: "username": {"password": "...", "role": "..."}
users = {
    "admin": {"password": "admin123", "role": "Administrator"},
    "john": {"password": "john123", "role": "Editor"},
    "mary": {"password": "mary123", "role": "Viewer"}
}

MAX_ATTEMPTS = 3

def authenticate(username, password):
    """Check if username exists and password matches"""
    if username in users and users[username]["password"] == password:
        return True
    return False

def get_role(username):
    """Return role of the user"""
    return users[username]["role"]

def login():
    """Handle login attempts"""
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        user = input("Enter username: ")
        passwd = getpass.getpass("Enter password: ")

        if authenticate(user, passwd):
            print(f"✅ Login successful. Welcome, {user}!")
            print(f"Your role is: {get_role(user)}")
            return True
        else:
            attempts += 1
            print(f"❌ Invalid credentials. Attempts left: {MAX_ATTEMPTS - attempts}")

    print("🚫 Too many failed attempts. Access denied!")
    return False

if __name__ == "__main__":
    login()
