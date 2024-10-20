import pickle
from bakery.person import *
from bakery.order import *

users: list[Person] = []

def loadUsers():
    '''
    This function gets a list of users from a pickle file
    '''
    global users
    try:
        with open("bakeryData/users.pkl", "rb") as file:
            #Read the list of bank accounts from a pickle file and store it in bankAccounts list
            users = list(pickle.load(file))
    except FileNotFoundError:
        print("File doesn't exist.")
    except Exception as e:
        print(e)

def saveUsers(user: Person):
    '''
    This function saves users to a pickle file
    '''
    loadUsers()

    users.append(user)
    with open("bakeryData/users.pkl", "wb") as file:
            #Store list of bank accounts in a pickle file
            pickle.dump(users, file)

def checkUserLogin(phone: str, password: str) -> Person:
    '''
    This function searches for a user with a phone number and password, if they exists it returns the user
    '''
    loadUsers()
    for user in users:
        if user.getPhone() == phone and user.getPassword() == password:
            print(f"Welcome back {user.getName()}")
            return user
        
def checkUserRegister(phone: str, password: str) -> bool:
    '''
    This function checks if a user with the passed phone number exists. It returns True if they do and False if not
    '''
    loadUsers()
    for user in users:
        if user.getPhone() == phone and user.getPassword() == password:
            print(f"You already have an account {user.getName()}!")
            return True
        elif user.getPhone() == phone and user.getPassword() != password: 
            print("An account with that number already exists")
            return True
        else:
            return False            
     
def employeeMenu(employee: Employee):
    '''
    This function displays a menu of available actions for the employee
    '''
    print("-" * 30)
    while True:
        print("What would you like to do?")
        print("1. Add a product.\n2. Remove a product.\n3. Update a product.\n4. View the menu.\n5. Exit.")
        choice: str = input("Your choice: ")
        if choice == '1':
            print("------------------Adding Product------------------")
            prodName: str = input("Product name: ")
            while True:
                try:
                    qty: int = int(input("Quantity: "))
                    if not isinstance(qty, int):
                        raise ValueError
                    price: float = float(input("Price: "))
                    if not isinstance(qty, int):
                        raise ValueError
                except ValueError:
                    print("Please enter numbers only.")
                else:
                    employee.addProduct(prodName, qty, price)
                    print(f"{prodName} was added successfully.")
                    break
            input("")

        elif choice == '2':
            print("------------------Removing Product------------------")
            prodName: str = input("Product name: ")
            removeMsg: str = employee.removeProduct(prodName)
            print(removeMsg)
            input("")
            
        elif choice == '3':
            print("------------------Updating a Product------------------")
            prodName: str = input("Product name: ")
            print("1. Update product name.\n2. Update product quantity\n3. Update product price.\n4. Back to main menu.")
            updateChoice: str = input("Your choice: ")
            updateMsg: str = employee.updateProduct(prodName, updateChoice)
            print(updateMsg)
            input("")

        elif choice == '4':
            print("------------------Stellar Bakery Menu------------------")
            menu: str = employee.listAllProducts()
            print(menu)
            input("")

        elif choice == '5':
            print("Exiting program..")
            break
        
        else:
            print("Invalid choice, try again..")

def customerMenu(customer: Customer):
    '''
    This function displays a menu of available actions for the customer
    '''
    cart: Cart = Cart()
    print("-" * 30)
    while True:
        print("What would you like to do?")
        print("1. View bakery menu.\n2. View cart.\n3. New order.\n4. View my profile.\n5. Exit.")
        choice: str = input("Your choice: ")
        if choice == '1':
            print("------------------Stellar Bakery Menu------------------")
            menu: str = customer.listAllProducts()
            print(menu)
            input("")

        elif choice == '2':
            print("------------------Your Cart------------------")
            cartInfo: str = cart.viewCart()
            print(cartInfo)
            input("")
            
        elif choice == '3':
            
            input("")

        elif choice == '4':
            
            input("")

        elif choice == '5':
            print("Exiting program..")
            break
        
        else:
            print("Invalid choice, try again..")

#Main program
def main():
    '''
    Function that contains all main operations
    '''
    print("-------Welcome to Stellar Bakery-------")

    while True:
        print("1. Login.\n2. Register.")
        choice: str = input("Your choice: ")
        if choice == '1':
            print("--------------Login--------------")
            phone: str = input("Enter your phone number: ")
            password: str = input("Enter your password: ")

            #Check if the user exists in the system, returns None if the user don't
            user: Person = checkUserLogin(phone, password)

            if user != None:
                if user.getRole() == "employee":
                    employeeMenu(user)
                    break
                elif user.getRole() == "customer":
                    customerMenu(user)
                    break
            else:
                print("There is no account with that phone number.")

        elif choice == '2':
            print("--------------Register--------------")
            name: str = input("Enter your name: ")
            age: int = int(input("Enter your age: "))
            gender: str = input("Enter your gender: ")
            phone: str = input("Enter your phone number: ")
            password: str = input("Enter your password: ")

            #Check if the user exists in the system, returns False if they don't
            exist: bool = checkUserRegister(phone, password)
            if not exist:
                customer: Customer = Customer(name, age, gender, phone, password)
                saveUsers(customer)
                print("You have successfully registered.")

        else:
            print("Invalid choice, try again..", end=" ")
            input("")

#Executing main
main()