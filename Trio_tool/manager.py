class Manager:
    
    def __init__(self):
        self.dashboard = []
    
    def create_account(self):
        # Get username input and validate
        username = input("Enter your username: ")
        if len(username) <= 2:
            print("The username length must be more than 2 characters, please provide a valid username.")
            return  # Exit the function if validation fails
        
        # Get roll input and validate
        roll = input("Enter your roll:")
        if len(roll)<=2:
            print("The roll length must be more than 2 characters, please provide a valid roll")
            return # Exit the function if validation fails
        
        # Get email input and validate
        email = input("Enter your email address: ")
        if email.count('@') != 1:
            print("The email is not valid, please provide a valid email.")
            return  # Exit the function if validation fails
        elif not email.endswith('@gmail.com'):
            print("The email is not valid, please provide a valid email.")
            return  # Exit the function if validation fails
        elif email.index('@') == 0:
            print("The email is not valid, please provide a valid email.")
            return  # Exit the function if validation fails
        elif email.index('@') + 1 == len(email):
            print("The email is not valid, please provide a valid email.")
            return  # Exit the function if validation fails
        
        # Get password input and validate
        password = input("Enter your password: ")
        while not self.validate_password(password):
            print("Invalid password. It must be at least 6 characters long.")
            password = input("Enter your password: ")

        print(f"Welcome {username}, you registered with the email {email}!")
        
        
        def validate_password(self, password: str) -> bool:
            return len(password) >= 6
        