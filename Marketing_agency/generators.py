import random
import faker


class DataGenerators:
    """
    This class generates fake data for employees, clients, and products.
    """

    def __init__(self):
        self.data = []  # Where we store the generated data
        self.fake_data = faker.Faker()  # This helps create fake names, addresses, etc.

    def generate_employees(self, number, data_manager):
        """Generate fake employee data and append to the data manager."""
        for _ in range(number):
            employee = {
                "name": self.fake_data.name(),
                "id": self.fake_data.uuid4(),
                "address": self.fake_data.address(),
                "email": self.fake_data.email(),
                "role": random.choice(
                    ["Project Manager", "Marketing Specialist", "Human Resources", "Product Manager"]),
                "salary": round(random.uniform(7000, 45000), 2)
            }
            data_manager.employees.append(employee)  # Correctly appending to employees
        print(f"Generated {number} employees profiles.")

    def generate_clients(self, number, data_manager):
        """this method take 2 prameters number : the number of Clients to generate
                  data_manager to pass and append to the list in data manager
               """

        # Generate a number of client profiles
        for _ in range(number):
            client = {
                "name": random.choice(
                    ["Minister in Education", "Minister in Culture", "Minister in Hajj and Umrah", "Minister of Health",
                     "Minister in Finance"]),
                "contact_number": self.fake_data.phone_number(),
                "email": self.fake_data.email(),
                "address": self.fake_data.address(),
            }
            data_manager.clients.append(client)  # Add to data_manager
        print(f"Generated {number} client profiles.")

    def generate_products(self, number, data_manager):
        """this method take 2 prameters number : the number of Products to generate
                  data_manager to pass and append to the list in data manager
               """
        # Generate a number of product profiles
        for _ in range(number):
            product = {
                "name": random.choice(["Rebranding", "Online Ads", "Marketing Operations", "Product Development"]),
                "id": self.fake_data.uuid4(),
                "price": round(random.uniform(30000, 700000), 2)
            }
            data_manager.products.append(product)  # Add to data_manager
        print(f"Generated {number} product profiles.")

    def generate_transactions(self, number, data_manager):
        """this method take 2 prameters number : the number of Transactions to generate
                  data_manager to pass and append to the list in data manager
               """
        # Check for employees and clients before generating transactions
        if not data_manager.employees:
            print("No employees available to generate transactions.")
            return
        if not data_manager.clients:
            print("No clients available to generate transactions.")
            return

        for _ in range(number):
            transaction = {
                "transaction_id": self.fake_data.uuid4(),
                "date": self.fake_data.date_between(start_date='-1y', end_date='today'),
                "employee": random.choice([emp['name'] for emp in data_manager.employees]),
                "client": random.choice([client['name'] for client in data_manager.clients]),
            }
            data_manager.sales.append(transaction)
        print(f"Generated {number} transaction records.")
