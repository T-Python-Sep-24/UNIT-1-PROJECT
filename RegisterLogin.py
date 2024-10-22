from Customers import Customer
import os
import pickle

class RegisterLogin:
    def __init__(self):
        self.customers = self.load_from_file()
        # Ensure customers is a dictionary
        if not isinstance(self.customers, dict):
            print("Error: Loaded customers data is not a dictionary. Initializing empty dictionary.")
            self.customers = {}
        
    def register_customer(self, customer: Customer):
        if isinstance(customer, Customer):
            if customer.username not in self.customers:
                self.customers[customer.username] = customer
                print(f"Customer {customer.name} registered successfully.")
                self.save_to_file()
                return True
            else:
                print("Username already exists.")
                return False
        else:
            print("Provided object is not a valid Customer.")
            return False
        
    def login_customer(self, username: str, password: str):
        if username in self.customers:
            if password == self.customers[username].get_password():
                return self.customers[username]
        return None
    
    def get_customer(self, username: str):
        return self.customers.get(username)
    
    def save_to_file(self):
        with open("customers_data", 'wb') as file:
            pickle.dump(self.customers, file)

    def load_from_file(self):
        if not os.path.exists("customers_data"):
            return {}  # Return an empty dictionary if the file does not exist
        
        with open("customers_data", 'rb') as file:
            try:
                data = pickle.load(file)
                if not isinstance(data, dict):
                    print("Loaded data is not a dictionary. Initializing empty dictionary.")
                    return {}
                return data
            except Exception as e:
                print(f"Error loading customers data: {e}")
                return {}

