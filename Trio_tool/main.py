from user_manager import UserManager
from registration import Registration
from login import Login
from manager import Manager
from employee import Employee

def main():
    # Create necessary instances
    user_manager = UserManager()  # Handle users
    registration = Registration(user_manager)  # Manage registration
    login = Login(user_manager)  # Handle login

    print("--- Welcome to Trio Management Tool! ---")

    while True:
        print("\nChoose an option:")
        print("1. Registration")
        print("2. Login")
        print("3. Exit")
        option = input("Enter your choice (1-3): ").strip()

        if option == "1":
            registration.create_account()  # Handle registration
        elif option == "2":
            username = login.user_login()  # Perform login and get username
            if username:  # If login is successful
                user_data = user_manager.get_user(username)  
                if user_data:  # Ensure the data is retrieved
                    role = user_data["role"].capitalize()  # Check user role
                    print(f"Logged in as: {username} with role: {role}")

                    if role == 'Manager':
                        manager = Manager(user_manager)  # Create Manager instance
                        manager.manager_dashboard()  # Enter Manager Dashboard
                    elif role == 'Employee':
                        employee = Employee(username)
                        employee.employee_dashboard()  # Enter Employee Dashboard
                    else:
                        print("Invalid role type. Please contact your administrator.")
            else:
                print("Login failed. Please try again.")
        elif option == "3":
            print("Exiting from the Trio Management Tool.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
