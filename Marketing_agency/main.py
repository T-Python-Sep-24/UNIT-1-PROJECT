from generators import DataGenerators
from data_exporter import DataExporter
from data_manager import DataManager
from forcasting import run_sales_prediction
import pandas as pd
from colorama import Fore, Style
import os
from user_auth import User

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_export_data(data_generator, data_exporter, data_manager):
    """
    Function to generate and export data.
    """
    print(Fore.GREEN + "Choose an action:".center(40))
    print(Fore.MAGENTA + "1. " + Fore.WHITE + "Generate Employees".center(40))
    print(Fore.MAGENTA + "2. " + Fore.WHITE + "Generate Clients".center(40))
    print(Fore.MAGENTA + "3. " + Fore.WHITE + "Generate Products".center(40))
    print(Fore.MAGENTA + "4. " + Fore.WHITE + "Generate Transactions".center(40))
    print(Fore.MAGENTA + "5. " + Fore.WHITE + "Export Data".center(40))
    print(Fore.MAGENTA + "6. " + Fore.WHITE + "Return to Main Menu".center(40))
    print(Fore.CYAN + "=" * 40)

    try:
        choice = int(input("> "))  # Capture the user's choice
    except ValueError:
        print("Please enter a valid number.")
        return

    if choice == 1:
        number = int(input("Enter number of employees to generate: "))
        data_generator.generate_employees(number, data_manager)

    elif choice == 2:
        number = int(input("Enter number of clients to generate: "))
        data_generator.generate_clients(number, data_manager)

    elif choice == 3:
        number = int(input("Enter number of products to generate: "))
        data_generator.generate_products(number, data_manager)

    elif choice == 4:
        number = int(input("Enter number of transactions to generate: "))
        data_generator.generate_transactions(number, data_manager)

    elif choice == 5:
        data_exporter.export_to_csv(data_manager, 'employees.csv', 'employees')
        data_exporter.export_to_csv(data_manager, 'clients.csv', 'clients')
        data_exporter.export_to_csv(data_manager, 'products.csv', 'products')
        data_exporter.export_to_csv(data_manager, 'sales.csv', 'sales')
        print("Data exported successfully.")
def view_manage_data(data_manager):
    """
    Function to view and manage data for employees, clients, products, and sales.
    """
    print(Fore.GREEN + "Choose data to manage:".center(40))
    print(Fore.MAGENTA + "1. " + Fore.WHITE + "Employees".center(40))
    print(Fore.MAGENTA + "2. " + Fore.WHITE + "Clients".center(40))
    print(Fore.MAGENTA + "3. " + Fore.WHITE + "Products".center(40))
    print(Fore.MAGENTA + "4. " + Fore.WHITE + "Sales".center(40))
    print(Fore.MAGENTA + "5. " + Fore.WHITE + "Return to Main Menu".center(40))
    print(Fore.CYAN + "=" * 40)

    try:
        choice = int(input("> "))  # Capture the user's choice
    except ValueError:
        print("Please enter a valid number.")
        return

    if choice == 1:
        data_manager.view_employees()
    elif choice == 2:
        data_manager.view_clients()
    elif choice == 3:
        data_manager.view_products()
    elif choice == 4:
        data_manager.view_sales()
    elif choice == 5:
        return
    else:
        print("Invalid choice. Returning to main menu.")

    # Ask if the user wants to update or delete after viewing
    action = input("Would you like to update or delete a record? (u/d/n): ").lower()
    if action == 'u':
        record_id = int(input("Enter the ID of the record you want to update: "))
        if choice == 1:
            data_manager.update_record(data_manager.employees, record_id)
        elif choice == 2:
            data_manager.update_record(data_manager.clients, record_id)
        elif choice == 3:
            data_manager.update_record(data_manager.products, record_id)
        elif choice == 4:
            data_manager.update_record(data_manager.sales, record_id)
    elif action == 'd':
        record_id = int(input("Enter the ID of the record you want to delete: "))
        if choice == 1:
            data_manager.delete_record(data_manager.employees, record_id)
        elif choice == 2:
            data_manager.delete_record(data_manager.clients, record_id)
        elif choice == 3:
            data_manager.delete_record(data_manager.products, record_id)
        elif choice == 4:
            data_manager.delete_record(data_manager.sales, record_id)


def main():
    """in this class we take inputs from the user and call the methods to do what he want """
    data_generator = DataGenerators()
    data_manager = DataManager()
    data_exporter = DataExporter()

    clear_console()
    print(Fore.CYAN + "=" * 40)
    print(Fore.YELLOW + Style.BRIGHT + "  Data Management System  ".center(40))
    print(Fore.CYAN + "=" * 40 + "\n")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if not User.authenticate(username, password):
        print("Invalid credentials. Exiting.")
        return

    while True:

        print(Fore.GREEN + "Please choose an option:".center(40))
        print(Fore.MAGENTA + "1. " + Fore.WHITE + "Generate & Export Data".center(40))
        print(Fore.MAGENTA + "2. " + Fore.WHITE + "View & Manage Data".center(40))
        print(Fore.MAGENTA + "3. " + Fore.WHITE + "Run Sales Forecasting".center(40))
        print(Fore.MAGENTA + "4. " + Fore.WHITE + "Exit".center(40))
        print(Fore.CYAN + "=" * 40)

        try:
            choice = int(input("> "))  # Capture the user's choice
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            generate_export_data(data_generator, data_exporter, data_manager)
        elif choice == 2:
            view_manage_data(data_manager)
        elif choice == 3:  # Sales Forecasting
            df = pd.read_csv("Stores.csv")
            run_sales_prediction(df)
        elif choice == 4:
            print("Exiting the data management system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

main()
