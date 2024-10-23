from Storge import Storge

from Employees import Employee , RegisterLoginEmploee
from Products import Products

from RegisterLogin import RegisterLogin

import pyfiglet
from blessed import Terminal
from termcolor import colored

term = Terminal()

print(pyfiglet.figlet_format("Car Solutions", font='standard'))

print(term.bold('Welcome to'), end=' ')
print(colored("Car Solutions", 'green', attrs=['bold']), end=' ')
print(term.bold('program!\n'))

exit = True
while True:
    print(colored('Kindly write ("y" for Yes and "n" for No). If you want to exit write ("exit").\n', 'blue', attrs=['bold']))
    main_choice = input(colored("Do you have an account in Car Solutions program? ", 'green', attrs=['bold'])) 
    
    register = RegisterLogin()
    if main_choice.lower() == 'employee':
        storge = Storge()
        register = RegisterLoginEmploee()
        exit = False
        if input("Register new employee? ") == 'y':
            while True:
                print(colored('Write your information to Register please:\n', 'blue', attrs=['bold']))
                name = input(term.bold('\nWrite your name here: '))
                username = input(term.bold('Create a username: '))
                password = input(term.bold('Create a strong password: '))
                secretCode = input(term.bold('Inter the program secret Code: '))
                employee = Employee(name, username, password)
                if register.register_customer(employee, secretCode):
                    employee = register.login_employee(username, password)
                    print(pyfiglet.figlet_format("WELCOME!", font='standard'))
                if input('Type p to add product') == 'p':
                    storge.add_product(Products(input('Product name: '), input('Product price: '), input('Product quantity: ')))  
                    storge.display_products()
                
                if input(colored('\nType exit to exit ', 'green', attrs=['bold'])).lower() == 'exit':
                   break
        else:
            print(colored('Write your information to Login please:\n', 'blue', attrs=['bold']))
            username = input(term.bold('Write your username: '))
            password = input(term.bold('Write your password: '))
            secretCode = input(term.bold('Inter the program secret Code: '))
            employee = register.login_employee(username, password)
            if employee:
                print(pyfiglet.figlet_format("Welcome Again!", font='standard'))
                break
            if input(colored('\nAre you already registered? ', 'green', attrs=['bold'])).lower() == 'n':
                print(colored('\nWrite your information to Register please: ', 'blue', attrs=['bold']))
                name = input(term.bold('\nWrite your name here: '))
                username = input(term.bold('Create a username: '))
                password = input(term.bold('Create a strong password: '))
                if register.register_employee(name, username, password):
                    employee = register.login_employee(username, password)
                    print(pyfiglet.figlet_format("WELCOME !", font='standard'))
                    break
        break
          
    elif main_choice.lower() == 'n':
        while True:
            print(colored('Write your information to Register please:\n', 'blue', attrs=['bold']))
            name = input(term.bold('\nWrite your name here: '))
            username = input(term.bold('Create a username: '))
            password = input(term.bold('Create a strong password: '))
            if register.register_customer(name, username, password):
                customer = register.login_customer(username, password)
                print(pyfiglet.figlet_format("WELCOME!", font='standard'))
                break
            if input(colored('\nAre you already registered? ("y" for Yes and "n" for No.) ', 'green', attrs=['bold'])).lower() == 'y':
                username = input(term.bold('Write your username: '))
                password = input(term.bold('Write your password: '))
                customer = register.login_customer(username, password)
                if customer:
                    print(pyfiglet.figlet_format("Welcome Again!", font='standard'))
                    break
        break
    elif main_choice.lower() == 'y':
        while True:
            print(colored('Write your information to Login please:\n', 'blue', attrs=['bold']))
            username = input(term.bold('Write your username: '))
            password = input(term.bold('Write your password: '))
            customer = register.login_customer(username, password)
            if customer:
                print(pyfiglet.figlet_format("Welcome Again!", font='standard'))
                break
            if input(colored('\nAre you already registered? ', 'green', attrs=['bold'])).lower() == 'n':
                print(colored('\nWrite your information to Register please: ', 'blue', attrs=['bold']))
                name = input(term.bold('\nWrite your name here: '))
                username = input(term.bold('Create a username: '))
                password = input(term.bold('Create a strong password: '))
                if register.register_customer(name, username, password):
                    customer = register.login_customer(username, password)
                    print(pyfiglet.figlet_format("WELCOME !", font='standard'))
                    break
        break
    elif main_choice.lower() == 'exit':
        exit = False
        break
    else:
        print(colored("Invalid Input. Try Again Please!", 'red', attrs=['bold']))
    

if exit:  
    storge = Storge()
    print(colored("Here are the list of your scheduled services:", 'yellow', attrs=['bold']))
    storge.display_upcoming_services()
    
    if customer.previous_products_orders:
        print(colored("\nYou may want to see these PRODUCTs:", 'yellow', attrs=['bold']))
        for product in customer.previous_products_orders:
            product.display()
            
    while True:
        print(colored("\nHere are the list of our services:", 'blue', attrs=['bold']))
        
        print('\n1. Car Products and Accessories.')
        print('2. Car Services for Repairing in Workshops.')
        print('3. Car Services on your Site.')
        print('4. Car Regular Maintenance Service.\n')
        
        try:    
            service_choice = int(input(colored("Choose the Number of Service that you Want: To Exit Write ('0'). ", 'green', attrs=['bold'])))
        except TypeError:
            print(colored("Invalid Input. Try Again Please!", 'red', attrs=['bold']))
            continue
        if service_choice == 1:
            while True:
                print(colored("\nAvailable products in the stock:\n", 'blue', attrs=['bold']))
                storge.display_products()
                product_choice = int(input(colored("\nChoose Product Number that you want to ADD to your Shopping Cart: ", 'green', attrs=['bold'])))
                try:
                    product = storge.get_product(product_choice)
                except TypeError:
                    print(colored("Invalid Input. Please Choose Available Product Number!", 'red', attrs=['bold']))
                    continue
                
                while True:
                    try:
                        quantity = int(input(colored("\nHow many you want to ADD from this product to your Shopping Cart?: ", 'green', attrs=['bold'])))
                    except TypeError:
                        print(colored("Invalid Input. Please Write Only Ingers numbers", 'red', attrs=['bold']))
                        continue
                    if customer.product_cart.add_to_cart(product, quantity):
                        break
                
                if input(colored('\nDo you want to ADD more Products?. ("y" for Yes and "n" for No): ', 'green', attrs=['bold'])).lower() == 'n':
                    if customer.checkout_products_cart():
                        print(pyfiglet.figlet_format("Thanks for your purchase!", font='standard'))
                        break
                    
        elif service_choice == 2:
            while True:
                print(colored("\nAvailable services: ", 'blue', attrs=['bold']))
                storge.display_services()
                serviceChoice = int(input(colored("\nChoose the Number of Service that you want: ", 'green', attrs=['bold'])))
                service = storge.get_service(serviceChoice)
                
                while True:
                    if storge.display_dates():
                        try:
                            date_choice = int(input(colored("\nChoose the appropriate date for you: ", 'blue', attrs=['bold'])))
                        except TypeError:
                            print(colored("Please choose only avilable numbers from the list. Write Only Ingers numbers", 'red', attrs=['bold']))
                            continue
                        date = storge.get_date(date_choice)
                        
                        if storge.display_times(date_choice, date):
                            try:
                                time_choice = int(input(colored("\nChoose the appropriate time for you: ", 'blue', attrs=['bold'])))
                            except TypeError:
                                print(colored("Please choose only avilable numbers from the list. Please Write Only Ingers numbers", 'red', attrs=['bold']))
                                continue
                            time = storge.get_time(date_choice, time_choice)
                            if customer.service_cart.add_to_cart(service, date, time, storge):
                                break
                
                if input(colored('\nDo you want to edit date, time or cancel service?. ("y" for Yes and "n" for No): ', 'green', attrs=['bold'])).lower() == 'n':
                    if customer.checkout_service_cart(storge):
                        print('The Receipt well sent to you with the total price after performing all necessary repairs')
                        print(pyfiglet.figlet_format("Thanks for your purchase!", font='standard'))
                        break
                    else:
                        print(colored("There is an error in checkout!", 'red', attrs=['bold']))
                        customer.service_cart.delete_cart()
                else:
                    customer.service_cart.delete_cart()
                    
        elif service_choice == 3:
            while True:
                print(colored("\nAvailable services on your Site: ", 'blue', attrs=['bold']))
                
                storge.display_On_Site_Maintenance()
                
                try:
                    serviceChoice = int(input(colored("\nChoose the Number of Service that you want: ", 'green', attrs=['bold'])))
                except TypeError:
                            print(colored("Please choose only avilable numbers from the list. Write Only Intgers numbers", 'red', attrs=['bold']))
                            continue
                            
                service = storge.get_On_Site_Maintenance(serviceChoice)
                
                while True:
                    if storge.display_dates():
                        try:
                            date_choice = int(input(colored("\nChoose the appropriate date for you: ", 'blue', attrs=['bold'])))
                        except TypeError:
                            print(colored("Please choose only avilable numbers from the list. Write Only Intgers numbers", 'red', attrs=['bold']))
                            continue
                        date = storge.get_date(date_choice)
                        
                        if storge.display_times(date_choice, date):
                            try:
                                time_choice = int(input(colored("\nChoose the appropriate time for you: ", 'blue', attrs=['bold'])))
                            except TypeError:
                                print(colored("Please choose only avilable numbers from the list. Write Only Intgers numbers", 'red', attrs=['bold']))
                                continue
                            time = storge.get_time(date_choice, time_choice)
                            if customer.service_cart.add_to_cart(service, date, time, storge):
                                break
                
                if input(colored('\nDo you want to edit date, time or cancel service?. ("y" for Yes and "n" for No): ', 'green', attrs=['bold'])).lower() == 'n':
                    if customer.checkout_service_cart(storge):
                        print(pyfiglet.figlet_format("Thanks for your purchase!", font='standard'))
                        break
                else:
                    customer.service_cart.delete_cart()
                    
        elif service_choice == 4:
            while True:
                print(colored("\nAvailable Regular Maintenance Services: ", 'blue', attrs=['bold']))
                storge.display_RegularMaintenances()
                try:
                    serviceChoice = int(input(colored("\nChoose Maintenance Kelometer of your car: ", 'green', attrs=['bold'])))
                except TypeError:
                        print(colored("Please choose only avilable numbers from the list. Write Only Intgers numbers", 'red', attrs=['bold']))
                        continue
                
                service = storge.get_RegularMaintenance(serviceChoice)
                
                while True:
                    if storge.display_dates():
                        try:
                            date_choice = int(input(colored("\nChoose the appropriate date for you: ", 'blue', attrs=['bold'])))
                        except TypeError:
                            print(colored("Please choose only avilable numbers from the list. Write Only Intgers numbers", 'red', attrs=['bold']))
                            continue
                        date = storge.get_date(date_choice)
                        
                        if storge.display_times(date_choice, date):
                            try:
                                time_choice = int(input(colored("\nChoose the appropriate time for you: ", 'blue', attrs=['bold'])))
                            except TypeError:
                                print(colored("Please choose only avilable numbers from the list. Write Only Intgers numbers", 'red', attrs=['bold']))
                                continue
                            time = storge.get_time(date_choice, time_choice)
                            if customer.service_cart.add_to_cart(service, date, time, storge):
                                break
                
                if input(colored('\nDo you want to edit date, time or cancel service?. ("y" for Yes and "n" for No): ', 'green', attrs=['bold'])).lower() == 'n':
                    if customer.checkout_service_cart(storge):
                        print(pyfiglet.figlet_format("Thanks for your purchase!", font='standard'))
                        break
                else:
                    customer.service_cart.delete_cart()
        
        elif service_choice == 0:
            break
        else:
            print(colored("Invalid Input. Try Again Please!", 'red', attrs=['bold']))
        
                    
        if input('\nDo you want to see the other services?. ("y" for Yes and "n" for No): ').lower() == 'n':
            print(pyfiglet.figlet_format("VISIT Us Again!", font='standard'))
            break





