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
        command = input("> ").strip().lower()
        if command.startswith("generate employees "):
            _, _, number = command.split()
            data_generator.generate_employees(int(number), data_manager)

        elif command.startswith("generate clients"):
            _, _, number = command.split()
            data_generator.generate_clients(int(number), data_manager)

        elif command.startswith("generate products"):
            _, _, number = command.split()
            data_generator.generate_products(int(number), data_manager)

        elif command.startswith("generate transactions"):
            _, _, number = command.split()
            data_generator.generate_transactions(int(number), data_manager)

        elif command == "view employees":
            data_manager.view_employees()

        elif command == "view clients":
            data_manager.view_clients()

        elif command == "view products":
            data_manager.view_products()

        elif command == "view transactions":
            data_manager.view_sales()

        elif command == "export data":
            data_exporter.export_to_csv(data_manager, 'employees.csv', 'employees')
            data_exporter.export_to_csv(data_manager, 'clients.csv', 'clients')
            data_exporter.export_to_csv(data_manager, 'products.csv', 'products')
            data_exporter.export_to_csv(data_manager, 'sales.csv', 'sales')
            print("Data exported successfully.")

        elif command == "exit":
            print("Exiting the sales management system. Goodbye!")
            break

        else:
            print("Invalid input")

main()
