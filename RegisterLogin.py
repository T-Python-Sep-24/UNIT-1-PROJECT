from Customers import Customer
import os
import pickle

class RegisterLogin:
    def __init__(self, customer:Customer):
        self.customers = self.load_from_file()
        
    def register_customer(self, customer:Customer):
        if customer.username not in self.customers:
            self.customers[customer.username] = customer
            self.save_to_file(customer)
            return True
        else:
            return False
        
    def login_customer(self, username:str, password:str):
        if username in self.customers:
            if password == self.customers[username].get_password():
                return self.customers[username]
        return None
    
    def save_to_file(self, customers:dict):
        with open("customers_data", 'wb') as file:
            pickle.dump(customers, file)

    def load_from_file(self):
        if not os.path.exists("customers_data"):
            return {}  
        
        with open("customers_data", 'rb') as file:
            return pickle.load(file)