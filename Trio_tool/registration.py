import re
import json
import os
import bcrypt

class UserManager:
    def __init__(self, filename='users.json'):
        self.filename = filename
        self.users = self.load_users()

    def load_users(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}

    def save_users(self):
        with open(self.filename, 'w') as file:
            json.dump(self.users, file)

    def add_user(self, username, email, password, role, department):
        if username not in self.users:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            self.users[username] = {
                'email': email,
                'password': hashed_password,
                'role': role,
                'department': department
            }
            self.save_users()
            print("User registered successfully!")
        else:
            print("Username already exists.")

class Registration:
    def __init__(self, user_manager):
        self.user_manager = user_manager

    def create_account(self):
        # Get username input and validate
        username = input("Enter your username: ")
        if len(username) <= 2:
            print("The username length must be more than 2 characters, please provide a valid username.")
            return  # Exit the function if validation fails
        
        # Get role input and validate
        role = input("Enter your role (Manager/Employee): ")
        if len(role) <= 2:
            print("The role length must be more than 2 characters, please provide a valid role.")
            return  # Exit the function if validation fails
        
        # Get department input and validate
        department = input("Enter Department: ")
        if len(department) <= 2:
            print("The department length must be more than 2 characters, please provide a valid department.")
            return  # Exit the function if validation fails
        
        # Get email input and validate
        email = input("Enter your email address: ")
        if not self.validate_email(email):
            print("The email is not valid, please provide a valid email.")
            return  # Exit the function if validation fails
        
        # Get password input and validate
        password = input("Enter your password: ")
        while not self.validate_password(password):
            print("Invalid password. It must be at least 8 characters long, with at least one uppercase letter, one lowercase letter, one digit, and one special character.")
            password = input("Enter your password: ")

        # Store user information
        self.user_manager.add_user(username, email, password, role, department)

        print(f"Welcome {username}, you registered with the email {email}!")

    def validate_email(self, email):
        # Email validation logic
        if email.count('@') != 1:
            return False
        elif not email.endswith('@gmail.com'):
            return False
        elif email.index('@') == 0:
            return False
        elif email.index('@') + 1 == len(email):
            return False
        return True

    def validate_password(self, password):
        # Check if the password meets the criteria
        if (len(password) < 8 or  # Minimum length
            not re.search(r"[a-z]", password) or  # At least one lowercase letter
            not re.search(r"[A-Z]", password) or  # At least one uppercase letter
            not re.search(r"[0-9]", password) or  # At least one digit
            not re.search(r"[!@#$%^&*()_+=-]", password)):  # At least one special character
            return False
        return True
