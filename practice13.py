
"""
login_attempts.py - Allow only 3 login attempts before denying access
"""

import getpass

# Hardcoded credentials (for demo)
USERNAME = "admin"
PASSWORD = "password123"

MAX_ATTEMPTS = 3

def login():
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        user = input("Enter username: ")
        passwd = getpass.getpass("Enter password: ")

        if user == USERNAME and passwd == PASSWORD:
            print("✅ Login successful. Welcome!")
            return True
        else:
            attempts += 1
            print(f"❌ Invalid credentials. Attempts left: {MAX_ATTEMPTS - attempts}")

    print("🚫 Too many failed attempts. Access denied!")
    return False

if __name__ == "__main__":
    login()
