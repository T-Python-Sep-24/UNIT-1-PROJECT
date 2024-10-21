from generators import DataGenerators
from data_exporter import DataExporter
from data_manager import DataManager
from colorama import Fore , Style
import os
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """in this class we take inputs from the user and call the methods to do what he want """
    data_generator = DataGenerators()
    data_manager = DataManager()
    data_exporter = DataExporter()

    while True:
        clear_console()
        print(Fore.CYAN + "=" * 40)
        print(Fore.YELLOW + Style.BRIGHT + "  Sales and Marketing Management System  ".center(40))
        print(Fore.CYAN + "=" * 40 + "\n")

        print(Fore.GREEN + "Please choose an action:".center(40))
        print(Fore.MAGENTA + "1. " + Fore.WHITE + "Generate Employees".center(40))
        print(Fore.MAGENTA + "2. " + Fore.WHITE + "Generate Clients".center(40))
        print(Fore.MAGENTA + "3. " + Fore.WHITE + "Generate Products".center(40))
        print(Fore.MAGENTA + "4. " + Fore.WHITE + "Generate Transactions".center(40))
        print(Fore.MAGENTA + "5. " + Fore.WHITE + "View Employees".center(40))
        print(Fore.MAGENTA + "6. " + Fore.WHITE + "View Clients".center(40))
        print(Fore.MAGENTA + "7. " + Fore.WHITE + "View Products".center(40))
        print(Fore.MAGENTA + "8. " + Fore.WHITE + "View Transactions".center(40))
        print(Fore.MAGENTA + "9. " + Fore.WHITE + "Export Data".center(40))
        print(Fore.MAGENTA + "10. " + Fore.WHITE + "Delete Data".center(40))
        print(Fore.MAGENTA + "11. " + Fore.WHITE + "Exit".center(40))
        print(Fore.CYAN + "=" * 40)

        try:
            choice = int(input("> "))  # Capture the user's choice
        except ValueError:
            print("Please enter a valid number.")
            continue

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

            data_manager.view_employees()


        elif choice == 6:

            data_manager.view_clients()


        elif choice == 7:

            data_manager.view_products()


        elif choice == 8:

            data_manager.view_sales()


        elif choice == 9:

            data_exporter.export_to_csv(data_manager, 'employees.csv', 'employees')

            data_exporter.export_to_csv(data_manager, 'clients.csv', 'clients')

            data_exporter.export_to_csv(data_manager, 'products.csv', 'products')

            data_exporter.export_to_csv(data_manager, 'sales.csv', 'sales')

            print("Data exported successfully.")


        elif choice == 10:

            print("Exiting the sales management system. Goodbye!")

            break


        else:

            print("Invalid choice. Please select a valid option.")

main()
