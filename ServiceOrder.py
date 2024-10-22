from ServiceCart import ServiceCart
# from Customers import Customer
import os
import json
import pickle

class ServiceOrder:
    def __init__(self, customer, cart:ServiceCart):
        self.cart = cart
        self.customer = customer
        self.__previous_services_orders = self.__load_from_json()
        
    def order_summary(self):
        print(f"Service summary for {self.customer.name}:")
        self.cart.display()
        print(f"\nCost: SAR {self.cart.total_cost()}")
    
    def checkout_cart(self):   
        self.__previous_services_orders[self.customer.username] = {} 
        self.__previous_services_orders[self.customer.username][len(self.__previous_services_orders) + 1] = self.cart
        self.__save_to_file(self.__previous_services_orders)
        
    def get_all_services_orders(self):
        return self.__load_from_json()
           
    # def __save_to_file(self, previous_services_orders: dict):
    #     with open('previous_services_orders.json', 'w') as file:
    #         json.dump(previous_services_orders, file)
            
    # def __load_from_json(self):
    #     if os.path.exists('previous_services_orders.json'):
    #         with open('previous_services_orders.json', 'r') as file:
    #             return json.load(file)
    #     else:
    #         return {}
        
    def __save_to_file(self, customers: dict):
        with open("previous_services_orders", 'wb') as file:
            pickle.dump(customers, file)
            
    def __load_from_json(self):
        if not os.path.exists("previous_services_orders"):
            return {}  
        
        with open("previous_services_orders", 'rb') as file:
            return pickle.load(file)
     