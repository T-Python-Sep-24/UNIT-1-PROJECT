import json
import os
import bcrypt

class UserManager:
    def __init__(self, filename='users.json'):
        self.filename = filename
        self.users = self.load_users()  

    def load_users(self):
        """Load users from a JSON file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Error decoding JSON. Creating a new user database.")
                return {}
        return {}

    def save_users(self):
        """Save users to a JSON file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.users, file, indent=4)
        except IOError as e:
            print(f"Error saving users: {e}")

    def add_user(self, username, email, password, role, department):
        valid_roles = ['Manager', 'Team Member']
        if role not in valid_roles:
            print("Invalid role type. Please contact your administrator.")
            return

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

    def verify_user(self, username, password):
        """Verify user credentials."""
        if username in self.users:
            stored_password = self.users[username]['password']
            return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))
        return False

    def get_user(self, username):
        """Get user details by username."""
        return self.users.get(username)
