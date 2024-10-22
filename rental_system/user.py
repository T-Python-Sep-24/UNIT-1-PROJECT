import json
from colorama import Fore,Style



class UserManager:
    def __init__(self):
       
        self.users = []

    def load_users(self):
       
        try:
            with open('users.json', 'r', encoding="UTF-8") as file:
                self.users = json.load(file)
        except FileNotFoundError:
            self.users = []

    def save_users(self):
      
        with open('users.json', 'w') as file:
            json.dump(self.users, file, indent=6)

    def add_user(self, username, password, role="Customer"):
        new_user = {
            "username": username,
            "password": password,
            "role": role
        }
        self.users.append(new_user)
        self.save_users()
        print(f"User {username} added successfully with role {role}.")

    def authenticate_user(self, username, password):
       
        for user in self.users:
            if user['username'] == username and user['password'] == password:
                print(f"Welcome back, {username}!")
                return user['role']  
        print(Fore.RED + "Invalid credentials!" + Style.RESET_ALL)
        return None
    def delete_user(self, username):
        for user in self.users:
            if user['username'] == username:
                self.users.remove(user)
                self.save_users() 
                print(f"User {username} deleted successfully.")
                return
        print(Fore.RED + f"User {username} not found." + Style.RESET_ALL)
