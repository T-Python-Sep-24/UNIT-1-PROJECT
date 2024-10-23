import bcrypt
from user_manager import UserManager
from manager import Manager
from employee import Employee

class Login:
    def __init__(self, user_manager):
        self.user_manager = user_manager

    def user_login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if self.user_manager.verify_user(username, password):
            user_info = self.user_manager.get_user(username)
            if user_info:  # Ensure user_info is not None
                role = user_info.get('role')

                # Check the role after successful login
                if role == 'Manager':
                    print(f"Welcome back, {username}! You have logged in as a Manager.")
                    manager = Manager(self.user_manager)  # Create Manager instance
                    manager.manager_dashboard()  # Redirect to Manager dashboard
                elif role == 'Employee':
                    print(f"Welcome back, {username}! You have logged in as an Employee.")
                    employee = Employee(username)  # Create Employee instance
                    employee.employee_dashboard()  # Redirect to Employee dashboard
                else:
                    print("Invalid role type. Please contact your administrator.")
            else:
                print("User information could not be retrieved.")
        else:
            print("Invalid username or password.")

if __name__ == "__main__":
    user_manager = UserManager()
    login = Login(user_manager)

    while True:
        choice = input("Choose an option:\n1. Login\n2. Exit\nEnter your choice (1-2): ")
        if choice == '1':
            login.user_login()
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
