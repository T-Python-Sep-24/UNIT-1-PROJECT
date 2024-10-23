from ServiceCart import ServiceCart
from Storge import Storge
import os
import pickle
from datetime import datetime
import json

class ServiceOrder:
    def __init__(self, customer, cart:ServiceCart):
        self.cart = cart
        self.customer = customer
        self.previous_services_orders = self.__load_from_pickle()
        
    def order_summary(self):
        print(f"\nService summary for {self.customer.name}:")
        self.cart.display()
        print(f"Cost: SAR {self.cart.total_cost()}")
    
    def checkout_cart(self, storge: Storge):
        self.previous_services_orders[self.customer.username] = {}
        self.previous_services_orders[self.customer.username][len(self.previous_services_orders) + 1] = self.cart
        self.__save_to_file(self.previous_services_orders)

        self.save_upcoming_service(storge)
        
        date = self.cart.cart['date']
        storge.delete_date(date)

        print(f"Checkout successful! Your service has been scheduled.")
        self.cart.display()

    def save_upcoming_service(self, storge: Storge):
        upcoming_services = storge.load_upcoming_services()
        upcoming_services.append(self.cart.cart)

        with open("upcoming_services.pkl", 'wb') as file: 
            pickle.dump(upcoming_services, file)
           
    def get_all_previous_services_orders(self):
        return self.__load_from_pickle()
    
    def __save_to_file(self, customers: dict):
        with open("previous_services_orders", 'wb') as file:
            pickle.dump(customers, file)
            
    def __load_from_pickle(self):
        if not os.path.exists("previous_services_orders"):
            return {}  
        
        with open("previous_services_orders", 'rb') as file:
            return pickle.load(file)
    