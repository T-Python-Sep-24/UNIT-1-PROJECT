from Storge import Storge

from Employees import Employee
from Customers import Customer

from RegisterLogin import RegisterLogin

from Products import Products
from ProductsCart import ProductsCart
from ProductsOrder import ProductsOrder

from Services import Services
from ServiceCart import ServiceCart
from ServiceOrder import ServiceOrder

import pyfiglet
from blessed import Terminal
from termcolor import colored

term = Terminal()

print(pyfiglet.figlet_format("Car Solutions", font='standard'))

print(term.bold('Welcome to'), end=' ')
print(colored("Car Solutions", 'green', attrs=['bold']), end=' ')
print(term.bold('program!\n'))


print('Kindly write "y" for Yes and "n" for No. Thanks.\n')
main_choice = input('Do you have an account in Car Solutions program? ')

register = RegisterLogin()
if main_choice.lower() == 'n':
    while True:
        print(term.bold('Write your information to register please:'))
        name = input('\nWrite your name here: ')
        username = input('Create a username: ')
        password = input('Create a strong password: ')
        if register.register_customer(name, username, password):
            customer = register.login_customer(username, password)
            print(pyfiglet.figlet_format("WELCOME!", font='standard'))
            break
        if input('\nAre you already registered? ').lower() == 'y':
            username = input('Write your username: ')
            password = input('Write your password: ')
            customer = register.login_customer(username, password)
            if customer:
                print(pyfiglet.figlet_format("Welcome Again!", font='standard'))
                break
else:
    while True:
        print(term.bold('\nWrite your information to login please:'))
        username = input('Write your username: ')
        password = input('Write your password: ')
        customer = register.login_customer(username, password)
        if customer:
            print(pyfiglet.figlet_format("Welcome Again!", font='standard'))
            break
        if input('\nYou have not registered yet? ').lower() == 'y':
            print(term.bold('Write your information to register please:'))
            name = input('\nWrite your name here: ')
            username = input('Create a username: ')
            password = input('Create a strong password: ')
            if register.register_customer(name, username, password):
                customer = register.login_customer(username, password)
                print(pyfiglet.figlet_format("WELCOME!", font='standard'))
                break

    
storge = Storge()
while True:
    print(colored("Here are the list of our services:", 'green', attrs=['bold']))
    
    print('\n1. Car Products and Accessories.')
    print('2. Car Services for Repairing in Workshops.')
    print('3. Car Services on your Site.')
    print('4. Car Regular Maintenance Service.\n')
    
    storge.display_upcoming_services()
        
    service_choice = int(input(colored("Choose the Number of Service that you Want: ", 'green', attrs=['bold'])))
    if service_choice == 1:
        while True:
            print(colored("\nAvailable products in the stock:\n", 'blue', attrs=['bold']))
            print(f'{"Id":<5} {"Name":<24} {"Product Id":<10} {"Price":<13} {"Stock Qty":<12}')
            storge.display_products()
            product_choice = int(input(colored("\nChoose the Number of Product that you want to ADD to your Shopping Cart: ", 'green', attrs=['bold'])))
            product = storge.get_product(product_choice)
            
            customer = Customer('init', 'init', 'init') # temp
            while True:
                quantity = int(input(colored("\nHow many you want to ADD from this product to your Shopping Cart?: ", 'blue', attrs=['bold'])))
                if customer.product_cart.add_to_cart(product, quantity):
                    break
            
            if input('\nDo you want to ADD more Products?. ("y" for Yes and "n" for No): ').lower() == 'n':
                if customer.checkout_products_cart():
                    print(pyfiglet.figlet_format("Thanks for your purchase!", font='standard'))
                    break
                
    elif service_choice == 2:
        while True:
            print("Available services:")
            storge.display_services()
            serviceChoice = int(input(colored("\nChoose the Number of Service that you want: ", 'green', attrs=['bold'])))
            service = storge.get_service(serviceChoice)
            
            while True:
                if storge.display_dates():
                    date_choice = int(input(colored("\nChoose the appropriate date for you: ", 'blue', attrs=['bold'])))
                    date = storge.get_date(date_choice)
                    
                    if storge.display_times(date_choice, date):
                        time_choice = int(input(colored("\nChoose the appropriate time for you: ", 'blue', attrs=['bold'])))
                        time = storge.get_time(date_choice, time_choice)
                        if customer.service_cart.add_to_cart(service, date, time, storge):
                            break
            
            if input('\nDo you want to edit date, time or cancel service?. ("y" for Yes and "n" for No): ').lower() == 'n':
                if customer.checkout_service_cart(storge):
                    print(pyfiglet.figlet_format("Thanks for your purchase!", font='standard'))
                    break
            else:
                customer.service_cart.delete_cart()
                
    if input('\nDo you want to see the other services?. ("y" for Yes and "n" for No): ').lower() == 'n':
        print(pyfiglet.figlet_format("VISIT Us Again!", font='standard'))
        break





