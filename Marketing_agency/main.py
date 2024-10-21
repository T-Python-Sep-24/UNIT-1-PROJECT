from generators import DataGenerators
from data_exporter import DataExporter
from data_manager import DataManager

def main():
    """in this class we take inputs from the user and call the methods to do what he want """
    print("Welcome to the Sales and Marketing Management System!")
    data_generator = DataGenerators()
    data_manager = DataManager()
    data_exporter = DataExporter()

    while True:
        print("\nPlease choose an action:")
        print("1. Generate Employees")
        print("2. Generate Clients")
        print("3. Generate Products")
        print("4. Generate Transactions")
        print("5. View Employees")
        print("6. View Clients")
        print("7. View Products")
        print("8. View Transactions")
        print("9. Export Data")
        print("10. Exit")

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
