from Customers import Customer
import os
import pickle

class RegisterLogin:
    def __init__(self):
        self.customers = self.load_from_file()
        if not isinstance(self.customers, dict):
            self.customers = {}
        
    def register_customer(self, name, username, password):
        customer = Customer(name, username, password)
        if isinstance(customer, Customer):
            if customer.username not in self.customers:
                self.customers[customer.username] = customer
                print(f"\n{customer.name} your registered successfully!")
                self.save_to_file()
                return True
            else:
                print("\nUsername already exists!. Try another one please. Or login if you already registered")
                return False
        print('Your data has some mistake!')
        return False
        
    def login_customer(self, username: str, password: str):
        if username in self.customers:
            if password == self.customers[username].get_password():
                return self.customers[username]
        print('The Username is not exists!. Try another one please. Or register if you haven\'t')
        return None
    
    def get_customer(self, username: str):
        return self.customers.get(username)
    
    def save_to_file(self):
        with open("customers_data", 'wb') as file:
            pickle.dump(self.customers, file)

    def load_from_file(self):
        if not os.path.exists("customers_data"):
            return {}  
        
        with open("customers_data", 'rb') as file:
            try:
                data = pickle.load(file)
                if not isinstance(data, dict):
                    return {}
                return data
            except Exception as e:
                print(f"Error loading customers data: {e.__cause__}")
                return {}

