import pickle
from bakery.person import Person, Employee, Customer

users: list[Person] = []

def loadUsers():
    '''
    This function gets a list of users from a file
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


def checkUser(phone: str, password: str):
    '''
    This function checks if a user is registered in the system
    '''
    loadUsers()
    for user in users:
        if user.getPhone() == phone and user.getPassword() == password:
            print(f"Welcome back {user.getName()}")
            return user
    print("User isn't registered.")
     
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
                        raise ValueError("Please enter qunatity in numbers only.")
                    price: float = float(input("Price: "))
                    if not isinstance(qty, int):
                        raise ValueError("Please enter price in numbers only.")
                except ValueError as e:
                    print(e)
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

def customerMenu(user: Customer):
    '''
    This function displays a menu of available actions for the customer
    '''
    print("This is Customer")

#Main program
def main():
    '''
    Function that contains all main operations
    '''
    print("-------Welcome to Stellar Bakery-------")

    while True:
        print("Enter '1' to Login and '2' to Register")
        choice: str = input("Your choice: ")
        if choice == '1':
            
            usrPhone: str = input("Enter your phone number: ")
            password: str = input("Enter your password: ")
            
            user: Person = checkUser(usrPhone, password)
            if user.getRole() == "employee":
                employeeMenu(user)
                break
            elif user.getRole() == "customer":
                customerMenu(user)
                break
        elif choice == '2':
            
            break
        else:
            print("Invalid choice, try again..", end=" ")
            input("")

#Executing main
main()