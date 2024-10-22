import pickle
from bakery.person import *
from bakery.order import *
from bakery.cart import Cart
import re
import time

#Using Rich library to style the output on terminal
from rich import print
from rich.prompt import Prompt, IntPrompt, FloatPrompt, Confirm
from rich.text import Text
from rich.rule import Rule
from rich.progress import track

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
            choice: str = Prompt.ask(Text(choiceList, style="#fff2f2"), choices=['1','2','3','4','5','6'], show_choices=False)
            if choice == '1':
                newName: str = Prompt.ask("[#ffd7f0]New name[/]")
                user.setName(newName)
                print(Text("Name was updated successfully.", style="#baf5ce"))

            elif choice == '2':
                newAge: int =IntPrompt.ask("[#ffd7f0]New age[/]")
                user.setAge(newAge)
                print(Text("Age was updated successfully.", style="#baf5ce"))

            elif choice == '3':
                #Keep asking user to enter a valid gender
                newGender: str = Prompt.ask("[#ffd7f0]New gender[/]", choices=['male','Male','female','Female'], show_choices=False)
                user.setGender(newGender)
                print(Text("Gender was updated successfully.", style="#baf5ce"))

            elif choice == '4':
                #Keep asking for correct phone number format
                while True:
                    newPhone: str = Prompt.ask("[#ffd7f0]New phone number[/]")
                    if not phoneValid(newPhone):
                        print(Text("Phone number should be 10 digits starting with (05).", style= "red"), end=" ")
                        Prompt.ask("[#fff2f2]Try again..[/]")
                    else:
                        user.setPhone(newPhone)
                        print(Text("Phone was updated successfully.", style="#baf5ce"))
                        break

                Prompt.ask(Text("Press Enter to continue..", style="white italic"))

            elif choice == '5':
                #Keep asking for correct password format
                while True:
                    newPassword: str = Prompt.ask("[#ffd7f0]New password[/]")
                    if not passwordValid(newPassword):
                        print("[red bold]Password too weak[/], [#fff2f2]your password should satisfy the following:[/]")
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

    #Keep showing the list of choices until the user enters 5
    while True:
        print(Rule(Text(f"Welcome, {employee.getName()}.. What would you like to do?", style="bold italic #e2deff"), characters="-  ", style="bold #aca2f5"))
        #Display a list of options to the employee
        choicesList: str = "1. Add a product.\n2. Remove a product.\n3. Update a product.\n4. View the menu.\n5. Exit.\nYour choice"
        choice = Prompt.ask(Text(choicesList, style = "#e7e4ff"), choices=['1','2','3','4','5'], show_choices=False)
        
        #Add product to the menu of available products
        if choice == '1':
            print(Rule(Text("Add Product", style="bold #fdffc3"), characters="- ", style="bold #fdffb0"))
            prodName: str = Prompt.ask("[bold #fbfbe2]Product name[/]")
            qty: int = IntPrompt.ask("[bold #fbfbe2]Quantity: ")
            price: float = FloatPrompt.ask("[bold #fbfbe2]Price: ")

            employee.addProduct(prodName, qty, price)
            print(Text(f"{prodName} was added successfully.", style="#baf5ce"))

        #Remove product from the menu of available products
        elif choice == '2':
            print(Rule(Text("Remove Product", style="bold #fdffc3"), characters="- ", style="bold #fdffb0"))
            prodName: str = Prompt.ask("[bold #feffde]Product name[/]")
            removeMsg: str = employee.removeProduct(prodName)
            print(removeMsg)
                
        #Update product on the menu of available products
        elif choice == '3':
            print(Rule(Text("Update Product", style="bold #fdffc3"), characters="- ", style="bold #fdffb0"))
            prodName: str = Prompt.ask("[bold #feffde]Product name[/]")
            choicesList = "1. Update product name.\n2. Update product quantity\n3. Update product price.\n4. Back to main menu.\nYour choice"
            updateChoice: str = Prompt.ask(Text(choicesList, style = "#fbfbe2"), choices=['1','2','3','4'], show_choices=False)
            updateMsg: str = employee.updateProduct(prodName, updateChoice)
            print(updateMsg)
        
        #Display menu of available products
        elif choice == '4':
            menu: Table = employee.listAllProducts()
            print(menu)
        
        #Exit program
        elif choice == '5':
            for i in track(range(10), description="Exiting program.."):
                time.sleep(0.05)  # Simulate work being done
            break

        Prompt.ask(Text("Press Enter to continue..", style="white italic"))

def customerMenu(customer: Customer):
    '''This function displays a menu of available actions for the customer'''

    cart: Cart = Cart()    
    #Keep showing the list of choices until the user enters 5
    while True:
        print(Rule(Text(f"Welcome, {customer.getName()}.. What would you like to do?", style="italic bold #e2deff"),characters="-  ", style="bold #aca2f5"))
        #Prompt customer for a choice and only accept one of the specified choices
        choicesList: str = "1. View bakery menu.\n2. View cart.\n3. Make New order.\n4. View my profile.\n5. Exit.\nYour choice"    
        choice = Prompt.ask(Text(choicesList, style="#e7e4ff"), choices=['1','2','3','4','5'], show_choices=False)
        #Display menu
        if choice == '1':
            menu: str = customer.listAllProducts()
            print(menu)

        #Show cart
        elif choice == '2':
            print(Rule(Text("Your Cart", style="bold #fbfbe2"), characters="- ", style="bold #fdffb0"))
            #Keep displaying cart options to the customer until they enter 5
            while True:
                cartInfo = cart.viewCart()
                #Display cart contents if they exist
                print(cartInfo)
                choicesList = "1. Add to cart.\n2. Remove from cart.\n3. Update product quantity.\n4. Clear cart.\n5. Proceed to checkout.\n6. Back to previous menu.\nYour choice"
                cartChoice: str = Prompt.ask(Text(choicesList, style="#fbfbe2"), choices=['1','2','3','4','5','6'], show_choices=False)
                
                #Add procust to cart
                if cartChoice == '1':
                    print(Rule(Text("Add to Cart", style="bold #fbfbe2"), characters="- ", style="bold #fdffb0"))
                    while True:
                        print(customer.listAllProducts())
                        print(Text("Enter the name and quantity of the product you want.", style="bold #fdffc3"))
                        prodName: str = Prompt.ask("[#fbfbe2]Product name[/]")
                        #Only accepts integers from the customer
                        prodQty: int = IntPrompt.ask("[#fbfbe2]Quantity[/]")
                        #Add the new product to the cart
                        cart.addToCart(prodName, prodQty)
                        print(Text(f"{prodName} was successfully added to your cart.", style="#baf5ce"))
                        
                        #Keep asking customer if they want to add more items to their cart until they enter n
                        addMore: str = Confirm.ask(Text("Add more products?", style="bold #feffde"))
                        if addMore:
                            continue
                        elif not addMore:
                            break

                #Remove product from cart            
                elif cartChoice == '2':
                    print(Rule(Text("Remove from Cart", style="bold #fbfbe2"), characters="- ", style="bold #fdffb0"))
                    prodName: str = Prompt.ask(Text("Enter the name of the product you want to remove", style="bold #fbfbe2"))
                    isRemoved: bool = cart.removeFromCart(prodName)
                    if isRemoved:
                        print(Text(f"{prodName} has been successfully removed from cart.", style="#baf5ce"))
                    else: 
                        print(Text(f"{prodName} is not in your cart.", style="red"))
                
                #Update cart contents
                elif cartChoice == '3':
                    print(Rule(Text("Update Cart", style="bold #fbfbe2"), characters="- ", style="bold #fdffb0"))
                    prodName: str = Prompt.ask(Text("Enter the name of the product you want to update", style="bold #fbfbe2"))
                    #Only accepts integers from the customer
                    newQty: int = IntPrompt.ask(Text("New quantity", style="bold #fbfbe2"))
                    isUpdated: bool = cart.updateCart(prodName, newQty)
                    if isUpdated:
                        print(Text(f"{prodName}'s quantity has been successfully updated.", style="#baf5ce"))
                    else:
                        print(Text(f"{prodName} is not in your cart.", style="red"))
                
                #Clear cart
                elif cartChoice == '4':
                    isCleared: bool = cart.clearCart()
                    if isCleared:
                        print(Text("Your cart has been cleared.", style="#baf5ce"))
                    else:
                        print(Text("Your cart is already empty.", style="red"))
                    break
                
                #Checkout 
                elif cartChoice == '5':
                    print(Rule(Text("Checkout", style="bold #feffde"), characters="- ", style="bold #fdffb0"))

                #Back to previous menu
                elif cartChoice == '6':
                    break

                Prompt.ask(Text("Press Enter to continue..", style="white italic"))
        
        #Create a new order       
        elif choice == '3':
            print(Rule(Text("Make New Order", style="bold #feffde"), characters="-", style="bold #fdffc3"))

            #To make a new order contents of the cart will be cleared
            cart.clearCart()
            #Display menu to the user
            print(customer.listAllProducts())
            print(Text("Enter the name and quantity of the product you want.", style="bold #fdffc3"))
            prodName: str = Prompt.ask("[#feffde]Product name[/]")
            #Only accepts integers from the user
            prodQty: int = IntPrompt.ask("[#feffde]Quantity[/]")
            cart.addToCart(prodName, prodQty)
            print(Text(f"{prodName} was successfully added to your cart.", style="#baf5ce"))

        #View and Update profile 
        elif choice == '4':
            print(Rule(Text("My Profile", style="bold #ffd7f0"), characters="-", style="bold #ffbfcb"))
            print(Text(customer.getInfo(), style="#ffd7f0"))

            updateProfile: str = Confirm.ask(Text("Would you like to update your profile?", style="bold #fff2f2"))
            if updateProfile:
                print(Rule(Text("Update Profile", style="bold #ffd7f0"), characters="-", style="bold #ffbfcb"))
                customer = updateCustomer(customer)
            elif not updateProfile:
                pass
        
        #Exit program
        elif choice == '5':
            for i in track(range(10), description="Exiting program.."):
                time.sleep(0.05)  # Simulate work being done
            break
        
        Prompt.ask(Text("Press Enter to continue..", style="white italic"))

#Main program
def main():
    '''
    Function that contains all main operations
    '''
    print(Rule(Text("Welcome to Stellar Bakery", style="bold italic #f0cfff"), characters="-", style="bold #e09eff"))
    
    choice = Prompt.ask("[#f5e6fc]1. Login.\n2. Register.\nYour choice[/]", choices=['1','2'], show_choices=False)
    #Login
    if choice == '1':
        while True:
            print(Rule(Text("Login", style="bold #bdeeff"), characters="-", style="bold #5dd6ff"))
            phone: str = Prompt.ask("[#daf5ff]Enter your phone number[/]")
            password: str = Prompt.ask("[#daf5ff]Enter your password[/]")
            
            #Check if phone number is valid
            if not phoneValid(phone):
                print(Text("Phone number should be 10 digits starting with (05).", style= "red"), end=" ")
                Prompt.ask("[#fff2f2]Try again..[/]")
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
    #Register
    elif choice == '2':
        while True:
            print(Rule(Text("Register", style="bold #bdeeff"), characters="-", style="bold #5dd6ff"))
            name: str = Prompt.ask("[#daf5ff]Enter your name[/]")
            #Only accepts integers from the user
            age: int = IntPrompt.ask("[#daf5ff]Enter your age[/]")
            #Keep asking user to enter a valid gender
            gender: str = Prompt.ask("[#daf5ff]Enter your gender[/]", choices=['male','Male','female','Female'], show_choices=False)
            phone: str = Prompt.ask("[#daf5ff]Enter your phone number[/]")
            password: str = Prompt.ask("[#daf5ff]Enter your password[/]")

            #Validate phone and password formats
            if not phoneValid(phone):
                print(Text("Phone number should be 10 digits starting with (05).", style= "red"), end=" ")
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
                print(Text("You have successfully registered, continue to login.", style="#baf5ce"))
            Prompt.ask(Text("Press Enter to continue..", style="white italic"))
            break

#Executing main program
main()