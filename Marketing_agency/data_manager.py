import datetime
import csv
import os
import pandas as pd

class DataManager:
    """
    The DataManager class is responsible for managing and processing the data
    """

    def __init__(self):
        """
        Initializes the DataManager with empty lists for employees, clients,
        products, and sales
        """
        self.employees = []  # List to hold employee information
        self.clients = []  # List to hold client information
        self.products = []  # List to hold product information
        self.sales = []  # List to hold sales records

    def load_data_from_csv(self):
        """
        Loads data from CSV files into the respective lists.
        """
        if os.path.exists('employees.csv'):
            self.employees = pd.read_csv('employees.csv').to_dict(orient='records')
        if os.path.exists('clients.csv'):
            self.clients = pd.read_csv('clients.csv').to_dict(orient='records')
        if os.path.exists('products.csv'):
            self.products = pd.read_csv('products.csv').to_dict(orient='records')
        if os.path.exists('sales.csv'):
            self.sales = pd.read_csv('sales.csv').to_dict(orient='records')
        print("Data loaded successfully from CSV files.")

    def save_data_to_csv(self):
        """
        Saves current data to CSV files.
        """
        pd.DataFrame(self.employees).to_csv('employees.csv', index=False)
        pd.DataFrame(self.clients).to_csv('clients.csv', index=False)
        pd.DataFrame(self.products).to_csv('products.csv', index=False)
        pd.DataFrame(self.sales).to_csv('sales.csv', index=False)
        print("Data saved successfully to CSV files.")

    def process_sale(self, employee_id, client_id):
        """
        Creates a new sale record.

        Parameters:
        - employee_id: The ID of the employee making the sale.
        - client_id: The ID of the client making the purchase.

        A sale record is created and added to the sales list, along with
        a timestamp.
        """
        # Create a sale dictionary to hold sale details
        sale = {
            "sale_id": len(self.sales) + 1,  # Unique ID for the sale
            "employee_id": employee_id,  # ID of the employee making the sale
            "client_id": client_id,  # ID of the client buying the product
            "timestamp": datetime.datetime.now().isoformat(),# Current date and time of the sale

        }

        self.sales.append(sale)  # Add the new sale to the list of sales
        print(f"Processed sale: {sale}")  # Print confirmation of the sale

    def view_employees(self):
        """
        Displays all employees.

        If there are no employees, it prints a message indicating that.
        """
        if not self.employees:  # Check if the employee list is empty
            print("No employees to display.")  # Message if no employees are found
            return

        for employee in self.employees:  # Loop through each employee and print their info
            print(employee)

    def view_clients(self):
        """
        Displays all clients.
        """
        for client in self.clients:  # Loop through each client and print their info
            print(client)

    def view_products(self):
        """
        Displays all products.
        """
        for product in self.products:  # each product and print its info
            print(product)

    def view_sales(self):
        """
        Displays all sales .
        """
        for sale in self.sales:  # each sale and print its info
            print(sale)

    def update_record(self, data_list, record_id):
        """
        Updates a record in the specified data list.

        Parameters:
        - data_list: List of records (employees, clients, products, or sales).
        - record_id: ID of the record to update.
        """
        for record in data_list:
            if record.get("id") == record_id:
                print(f"Found record: {record}")
                for key in record:
                    new_value = input(f"Enter new value for {key} (leave blank to keep current value): ")
                    if new_value:
                        record[key] = new_value
                print(f"Updated record: {record}")
                return
        print("Record not found.")

    def delete_record(self, data_list, record_id):
        """
        Deletes a record in the specified data list.
        """
        for record in data_list:
            if record.get("id") == record_id:
                data_list.remove(record)
                print(f"Record {record_id} deleted successfully.")
                return
        print("Record not found.")

    def search_record(self, data_list, search_key, search_value):
        """
        Searches for a record in the given data list by a specific search key (e.g., 'id' or 'email').
        Parameters:
        - data_list: List of records (employees, clients, products, or sales).
        - search_key: The key in the record to search by (e.g., 'id', 'email').
        - search_value: The value to search for (e.g., specific ID or email).
        """
        for record in data_list:
            if record.get(search_key) == search_value:
                print(f"Record found: {record}")
                return
        print("Record not found.")