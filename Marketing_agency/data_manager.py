import datetime
class DataManager:
    def __init__(self):
        # Lists to hold our data
        self.employees = []
        self.clients = []
        self.products = []
        self.sales = []

    def process_sale(self, employee_id, client_id):
        # Creating a sale record
        sale = {
            "sale_id": len(self.sales) + 1,
            "employee_id": employee_id,
            "client_id": client_id,
            "timestamp": datetime.datetime.now().isoformat(),
        }
        self.sales.append(sale)  # Adding sale to the list
        print(f"Processed sale: {sale}")

    def view_employees(self):
        # Check if there are any employees to show
        if not self.employees:
            print("No employees to display.")
            return
        for employee in self.employees:
            print(employee)

    def view_clients(self):
        # Print each client
        for client in self.clients:
            print(client)

    def view_products(self):
        # Print each product
        for product in self.products:
            print(product)

    def view_sales(self):
        # Print each sale
        for sale in self.sales:
            print(sale)

