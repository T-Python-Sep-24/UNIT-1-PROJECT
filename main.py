import pickle
from bakery.person import *
from bakery.order import *
import re

#Using Rich library to style the output on terminal
from rich import print
from rich.prompt import Prompt, IntPrompt, FloatPrompt, Confirm
from rich.text import Text

users: list[Person] = []

def loadUsers():
    '''This function gets a list of users from a pickle file'''
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
    '''This function saves users to a pickle file'''
    loadUsers()
    users.append(user)
    with open("bakeryData/users.pkl", "wb") as file:
            #Store list of bank accounts in a pickle file
            pickle.dump(users, file)

def updateCustomer(customer: Customer):
    '''
    This function updates a customer's details then saves the updated info to the list of users in a pickle file
    '''
    loadUsers()
    for user in users:
        if user.getPhone() == customer.getPhone():

            choiceList: str = "Choose what to update:\n1. Name.\n2. Age\n3. Gender.\n4. Phone number.\n5. Password.\n6. Back to main menu.\nYour choice"
            choice: str = Prompt.ask(Text(choiceList, style="#bdeeff"), choices=['1','2','3','4','5','6'], show_choices=False)
            if choice == '1':
                newName: str = Prompt.ask("[#43cfff]New name[/]")
                user.setName(newName)
                print(Text("Name was updated successfully.", style="#49ff88"))
                Prompt.ask(Text("Press Enter to continue..", style="white italic"))

            elif choice == '2':
                newAge: int =IntPrompt.ask("[#43cfff]New age[/]")
                user.setAge(newAge)
                print(Text("Age was updated successfully.", style="#49ff88"))
                Prompt.ask(Text("Press Enter to continue..", style="white italic"))

            elif choice == '3':
                #Keep asking user to enter a valid gender
                newGender: str = Prompt.ask("[#43cfff]New gender[/]", choices=['male','Male','female','Female'], show_choices=False)
                user.setGender(newGender)
                print(Text("Gender was updated successfully.", style="#49ff88"))
                Prompt.ask(Text("Press Enter to continue..", style="white italic"))

            elif choice == '4':
                #Keep asking for correct phone number format
                while True:
                    newPhone: str = Prompt.ask("[#43cfff]New phone number[/]")
                    if not phoneValid(newPhone):
                        print(Text("Phone number should be 10 digits starting with (05). Try again..", style="red"))
                        Prompt.ask(Text("Press Enter to continue..", style="white italic"))
                    else:
                        user.setPhone(newPhone)
                        print(Text("Phone was updated successfully.", style="#49ff88"))
                        break
                Prompt.ask(Text("Press Enter to continue..", style="white italic"))

            elif choice == '5':
                #Keep asking for correct password format
                while True:
                    newPassword: str = input("New password: ")
                    if not passwordValid(newPassword):
                        print("[red bold]Password too weak[/], [#f5cda4]your password should satisfy the following:[/]")
                        print(Text("• Be at least 8 characters long.\n• Contain 1 upper case and 1 lower case letters.\n• Contain a special character e.g(@#_)\n", style = "#fff2f2"), end =" ")
                        Prompt.ask("[#fff2f2]Try again[/]")
                    else:
                        user.setPassword(newPassword)
                        print("Password was updated successfully.")
                        Prompt.ask(Text("Press Enter to continue..", style="white italic"))
                        break
            elif choice == '6':
                break
            customer = user

    with open("bakeryData/users.pkl", "wb") as file:
            #Store list of bank accounts in a pickle file
            pickle.dump(users, file)

    return customer

def phoneValid(phone: str) -> bool:
    '''This method validates a phone number and return true if it's valid'''
    numberPattern = r'^05[0-9]{8}$'
    return re.match(numberPattern, phone)

def passwordValid(password: str) -> bool:
    '''This function validates a password and returns true if it's valid'''
    passwordPattern = r'[A-Za-z0-9@#_+$&-]{8,}'
    return re.fullmatch(passwordPattern, password)

def checkUserLogin(phone: str, password: str) -> Person:
    '''This function searches for a user with a phone number and password, if they exists it returns the user'''
    loadUsers()
    for user in users:
        if user.getPhone() == phone and user.getPassword() == password:
            print(Text(f"Welcome back {user.getName()}", style="red"))
            return user
        elif user.getPhone() == phone and user.getPassword() != password: 
            print(Text(f"Incorrect password for phone number {phone}", style="red"))
          
def checkUserRegister(phone: str, password: str) -> bool:
    '''This function checks if a user with the passed phone number exists. It returns True if they do and False if not'''
    loadUsers()
    for user in users:
        if user.getPhone() == phone and user.getPassword() == password:
            print(Text(f"You already have an account {user.getName()}!", style="red"))
            return True
        elif user.getPhone() == phone and user.getPassword() != password: 
            print(Text("An account with that number already exists", style="red"))
            return True
        else:
            return False            
     
def employeeMenu(employee: Employee):
    '''This function displays a menu of available actions to the employee'''
    print("-" * 30)
    print(Text(f"Welcome back {employee.getName()}..", style = "italic bold #aca2f5"))
    print(Text("What would you like to do?", style = "bold #d6d0ff"))

    #Display a list of options to the employee
    choicesList: str = "1. Add a product.\n2. Remove a product.\n3. Update a product.\n4. View the menu.\n5. Exit.\nYour choice"
    choice = Prompt.ask(Text(choicesList, style = "#d6d0ff"), choices=['1','2','3','4','5'], show_choices=False)
    if choice == '1':
        print(Text("------------------Adding Product------------------", style="bold #f5cda4"))
        prodName: str = Prompt.ask("[#fbff9b]Product name[/]")
        qty: int = IntPrompt.ask("[#fbff9b]Quantity: ")
        price: float = FloatPrompt.ask("[#fbff9b]Price: ")

        employee.addProduct(prodName, qty, price)
        print(Text(f"{prodName} was added successfully.", style="#baf5ce"))
        Prompt.ask(Text("Press Enter to continue..", style="white italic"))

    elif choice == '2':
        print(Text("------------------Removing Product------------------", style="bold #f5cda4"))
        prodName: str = Prompt.ask("[#fbff9b]Product name[/]")
        removeMsg: str = employee.removeProduct(prodName)
        print(Text(removeMsg, style="#feffde"))
        Prompt.ask(Text("Press Enter to continue..", style="white italic"))
            
    elif choice == '3':
        print("------------------Updating a Product------------------")
        prodName: str = Prompt.ask("[#fbff9b]Product name[/]")
        choicesList = "1. Update product name.\n2. Update product quantity\n3. Update product price.\n4. Back to main menu."
        updateChoice: str = Prompt.ask(Text(choicesList, style = "#fbff9b"), choices=['1','2','3','4'], show_choices=False)
        updateMsg: str = employee.updateProduct(prodName, updateChoice)
        print(Text(updateMsg, style="#feffde"))
        Prompt.ask(Text("Press Enter to continue..", style="white italic"))

    elif choice == '4':
        menu: str = employee.listAllProducts()
        print(menu)
        Prompt.ask(Text("Press Enter to continue..", style="white italic"))

    elif choice == '5':
        #Add progress bar here 
        print("Exiting program..")

def customerMenu(customer: Customer):
    '''
    This function displays a menu of available actions for the customer
    '''
    cart: Cart = Cart()
    print("-" * 30)
    print(Text(f"Welcome back {customer.getName()}..", style="italic bold #aca2f5"))
    print(Text("What would you like to do?", style = "bold #d6d0ff"))
    #Prompt customer for a choice and only accept one of the specified choices
    choicesList: str = "1. View bakery menu.\n2. View cart.\n3. Make New order.\n4. View my profile.\n5. Exit."    
    choice = Prompt.ask(Text(choicesList, style="#d6d0ff"), choices=['1','2','3','4','5'], show_choices=False)
    if choice == '1':
        menu: str = customer.listAllProducts()
        print(menu)
        input("")

    elif choice == '2':
        print(Text("------------------Your Cart------------------", style="bold #f5cda4"))
        cartInfo: str = cart.viewCart()
        #Display cart contents if they exist
        print(Text(cartInfo, style="#f5cda4"))
        
        #Display cart options to the user
        choicesList = "1. Add to cart.\n2. Remove from cart.\n3. Clear cart.\n4. Proceed to checkout.\n5. Back to previous menu.\nYour choice"
        cartChoice: str = Prompt.ask(Text(choicesList, style="#f5cda4"), choices=['1','2','3','4','5'], show_choices=False)
        if cartChoice == '1':
            while True:
                print(customer.listAllProducts())
                print(Text("Enter the name and quantity of the product you want.", style="bold #f5cda4"))
                prodName: str = Prompt.ask("[#fbff9b]Product name[/]")
                #Only accepts integers from the user
                prodQty: int = IntPrompt.ask("[#fbff9b]Quantity[/]")
                cart.addItem(prodName, prodQty)
                print(Text(f"{prodName} was successfully added to your cart.", style="#baf5ce"))
                addMore: str = Confirm.ask(Text("Add more products?", style="bold #fbff9b"))
                if addMore.lower() == 'y':
                    continue
                elif addMore.lower() == 'n':
                    break

        elif cartChoice == '2':
                prodName: str = Prompt.ask(Text("Enter the name of the product you want to remove", style="bold #f5cda4"))
                cart.removeItem(prodName)
        
        elif cartChoice == '3':
                cart.clearCart()
                print(Text("Cart has been cleared.", style="#baf5ce"))
                
        elif cartChoice == '4':
            pass
        elif cartChoice == '5':
            pass

        Prompt.ask(Text("Press Enter to continue..", style="white italic"))
            
    elif choice == '3':
        print(Text("------------------Make New Order------------------", style="bold #f5cda4"))
        #To make a new order contents of the cart will be cleared
        cart.clearCart()
        #Display menu to the user
        print(customer.listAllProducts())
        print(Text("Enter the name and quantity of the product you want.", style="bold #f5cda4"))
        prodName: str = Prompt.ask("[#fbff9b]Product name[/]")
        #Only accepts integers from the user
        prodQty: int = IntPrompt.ask("[#fbff9b]Quantity[/]")
        cart.addItem(prodName, prodQty)
        print(Text(f"{prodName} was successfully added to your cart.", style="#baf5ce"))

        Prompt.ask(Text("Press Enter to continue..", style="white italic"))

    elif choice == '4':
        print(Text("------------------My Profile------------------", style="bold #ffbfcb"))
        print(Text(customer.getInfo(), style="#ffd7f0"))

        profileChoice: str = Confirm.ask(Text("Would you like to update your profile?", style="bold #fff2f2"), choices=['yes', 'no'])
        if profileChoice.lower() == 'yes':
            print(Text("------------------Update Profile------------------", style="bold #ffbfcb"))
            customer = updateCustomer(customer)
        elif profileChoice.lower() == 'no':
            pass

        Prompt.ask(Text("Press Enter to continue..", style="white italic"))

    elif choice == '5':
        #Add progress bar here
        print("Exiting program..")

#Main program
def main():
    '''
    Function that contains all main operations
    '''
    print(Text("------- Welcome to Stellar Bakery -------", style="bold #aca2f5"))
    
    choice = Prompt.ask("[#bdeeff]1. Login.\n2. Register.\nYour choice[/]", choices=['1','2'], show_choices=False)
    if choice == '1':
        while True:
            print(Text("----------------- Login -----------------", style="bold #2baedb"))
            phone: str = Prompt.ask("[#bdeeff]Enter your phone number[/]")
            password: str = Prompt.ask("[#bdeeff]Enter your password[/]")
            
            #Check if phone number is valid
            if not phoneValid(phone):
                print(Text("Phone number should be 10 digits starting with (05). Try again..", style= "red"))
                continue

            #Check if the user exists in the system, returns None if the user don't
            user: Person = checkUserLogin(phone, password)
            if user != None:
                #Display the appropriate main menu for each of the employee and the customer
                if user.getRole() == "employee":
                    employeeMenu(user)
                    break
                elif user.getRole() == "customer":
                    customerMenu(user)
                    break

    elif choice == '2':
        while True:
            print(Text("-------------- Register --------------", style="bold #2baedb"))
            name: str = Prompt.ask("[#bdeeff]Enter your name[/]")
            #Only accepts integers from the user
            age: int = IntPrompt.ask("[#bdeeff]Enter your age[/]")
            #Keep asking user to enter a valid gender
            gender: str = Prompt.ask("[#bdeeff]Enter your gender[/]", choices=['male','Male','female','Female'])
            phone: str = Prompt.ask("[#bdeeff]Enter your phone number[/]")
            password: str = Prompt.ask("[#bdeeff]Enter your password[/]")

            #Validate phone and password formats
            if not phoneValid(phone):
                print(Text("Phone number should be 10 digits starting with (05).", style= "red"))
                Prompt.ask("[#fff2f2]Try again..[/]")
                continue
            if not passwordValid(password):
                print("[red bold]Password too weak[/], [#f5cda4]your password should satisfy the following:[/]")
                print(Text("• Be at least 8 characters long.\n• Contain 1 upper case and 1 lower case letters.\n• Contain a special character e.g(@#_)\n", style = "#fff2f2"), end =" ")
                Prompt.ask("[#fff2f2]Try again..[/]")
                continue
                
            #Check if the user exists in the system, returns False if they don't
            exist: bool = checkUserRegister(phone, password)
            if not exist:
                customer: Customer = Customer(name, age, gender, phone, password)
                #Store the created customer account in a pickle file with the rest of the users
                saveUsers(customer)
                print(Text("You have successfully registered, continue to login.", style="#49ff88"))
            Prompt.ask(Text("Press Enter to continue..", style="white italic"))
            break

#Executing main program
main()