from generators import DataGenerators
from data_exporter import DataExporter
from data_manager import DataManager
from forcasting import run_sales_prediction
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
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
    Function to manage data for employees, clients, products, and sales.
    Allows the user to choose whether to view the data or directly update, delete, or search.
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

    # Ask if the user wants to view the data
    view_data = input("Would you like to view the data first? (y/n): ").lower()

    if view_data == 'y':
        # Based on the user's choice, view the corresponding data
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

    # After viewing (or skipping), ask what action the user wants to perform
    action = input("Would you like to update, delete, or search a record? (u/d/s/n): ").lower()

    if action == 's':
        if choice == 1:
            record_id = input("Enter the ID of the employee to search: ")
            data_manager.search_record(data_manager.employees, "id", record_id)
        elif choice == 2:
            email = input("Enter the email of the client to search: ")
            data_manager.search_record(data_manager.clients, "email", email)
        elif choice == 3:
            record_id = input("Enter the ID of the product to search: ")
            data_manager.search_record(data_manager.products, "id", record_id)
        elif choice == 4:
            record_id = input("Enter the ID of the sale to search: ")
            data_manager.search_record(data_manager.sales, "transaction_id", record_id)

    elif action == 'u':
        record_id = input("Enter the ID or email of the record you want to update: ")  # Adjust depending on the type
        if choice == 1:
            data_manager.update_record(data_manager.employees, record_id)
        elif choice == 2:
            data_manager.update_record(data_manager.clients, record_id)
        elif choice == 3:
            data_manager.update_record(data_manager.products, record_id)
        elif choice == 4:
            data_manager.update_record(data_manager.sales, record_id)

    elif action == 'd':
        record_id = input("Enter the ID or email of the record you want to delete: ")  # Adjust depending on the type
        if choice == 1:
            data_manager.delete_record(data_manager.employees, record_id)
        elif choice == 2:
            data_manager.delete_record(data_manager.clients, record_id)
        elif choice == 3:
            data_manager.delete_record(data_manager.products, record_id)
        elif choice == 4:
            data_manager.delete_record(data_manager.sales, record_id)

    elif action == 'n':
        print("No action selected. Returning to main menu.")


import pandas as pd

def visualize_client_preferences(data_manager):
    """
    Visualizes client preferences, showing the total amount spent on each product
    for every client in the system.
    """

    # Ensure there are sales data to analyze
    if not data_manager.sales:
        print("No sales data available to analyze.")
        return

    # Convert sales data to DataFrame
    df = pd.DataFrame(data_manager.sales)

    # Ensure there is product price data available to analyze
    if 'price' not in df.columns or 'product' not in df.columns:
        print("Sales data must include 'product' and 'price' fields.")
        return

    # Group by client and product to sum up prices
    client_data = df.groupby(['client', 'product'])['price'].sum().unstack().fillna(0)

    # Plot data for each client
    for client in client_data.index:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            plt.figure(figsize=(10, 6))
            sns.barplot(x=client_data.columns, y=client_data.loc[client], palette='viridis')
            plt.title(f'Total Spending by {client}')
            plt.ylabel('Total Spent')
            plt.xlabel('Products')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

    print("Client preferences visualization complete.")
def main():
    """in this class we take inputs from the user and call the methods to do what he want """
    data_generator = DataGenerators()
    data_manager = DataManager()
    data_exporter = DataExporter()
    data_manager.load_data_from_csv()

    clear_console()
    print(Fore.CYAN + "=" * 40)
    print(Fore.YELLOW + Style.BRIGHT + "  Data Management System  ".center(40))
    print(Fore.CYAN + "=" * 40 + "\n")

    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if User.authenticate(username, password):
            break  # Exit the loop when the correct credentials are provided
        else:
            print("Invalid credentials. Please try again.")
            z = input("")

    while True:

        print(Fore.GREEN + "Please choose an option:".center(40))
        print(Fore.MAGENTA + "1. " + Fore.WHITE + "Generate & Export Data".center(40))
        print(Fore.MAGENTA + "2. " + Fore.WHITE + "View & Manage Data".center(40))
        print(Fore.MAGENTA + "3. " + Fore.WHITE + "Run Sales Forecasting".center(40))
        print(Fore.MAGENTA + "4. " + Fore.WHITE + "show client preferences".center(40))
        print(Fore.MAGENTA + "5. " + Fore.WHITE + "Exit".center(40))
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
            visualize_client_preferences(data_manager)
        elif choice == 5:
            data_manager.save_data_to_csv()
            print("Exiting the data management system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")




if __name__ == '__main__':
    main()