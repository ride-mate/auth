import secrets
import string
import hashlib
from getpass import getpass

USER_DETAILS_FILEPATH = "users.txt"
PUNCTUATIONS = "@#$%&"
DEFAULT_PASSWORD_LENGTH = 12
INVALID_LENGTH_MESSAGE = f'''
Password length must be between 8 and 16.
Password length must be a number.
Generating password with default length of {DEFAULT_PASSWORD_LENGTH} characters.
'''


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + PUNCTUATIONS
    pwd = ''.join(secrets.choice(characters) for _ in range(length))
    return pwd


def hash_password(pwd):
    """Hash a password using SHA-256 algorithm"""
    pwd_bytes = pwd.encode('utf-8')
    hashed_pwd = hashlib.sha256(pwd_bytes).hexdigest()
    return hashed_pwd


def save_user(username, hashed_pwd):
    """Save user-details to the user detail file"""
    with open(USER_DETAILS_FILEPATH, 'a') as f:
        f.write(f"{username} {hashed_pwd}\n")


def user_exists(username):
    try:
        with open(USER_DETAILS_FILEPATH, 'r') as f:
            for line in f:
                parts = line.split()
                if parts[0] == username:
                    return True
    except FileNotFoundError as fl_err:
        print(f"{fl_err.args[-1]}: {USER_DETAILS_FILEPATH}")
        print(f"System will create file: {USER_DETAILS_FILEPATH}")
    return False


def authenticate_user(username, password):
    try:
        with open(USER_DETAILS_FILEPATH, 'r') as f:
            for line in f:
                parts = line.split()
                if parts[0] == username:
                    if parts[1] == hash_password(password):
                        return True
                    else:
                        return False
    except FileNotFoundError as fl_err:
        print(f"{fl_err.args[-1]}: {USER_DETAILS_FILEPATH}")
        print(f"System will create file: {USER_DETAILS_FILEPATH}")
    return False
