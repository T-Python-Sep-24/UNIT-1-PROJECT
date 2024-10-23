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
        self.upcoming_services_dict = self.__load_upcoming_services_dict()
        
    def order_summary(self):
        print(f"\nService summary for {self.customer.name}:")
        self.cart.display()
        print(f"Cost: SAR {self.cart.total_cost()}")
    
    def checkout_cart(self, storge: Storge):
        upcoming_service = {
            "service": self.cart.cart['service'],
            "date": self.cart.cart['date'],
            "time": self.cart.cart['time']
        }
        self.add_service_to_dict(self.customer.username, upcoming_service)
        
        self.previous_services_orders[self.customer.username] = {}
        self.previous_services_orders[self.customer.username][len(self.previous_services_orders) + 1] = self.cart
        self.__save_to_file(self.previous_services_orders)
        
        date = self.cart.cart['date']
        storge.delete_date(date)

        print(f"Checkout successful! Your service has been scheduled.")
        self.cart.display()

    def add_service_to_dict(self, username, service):
        upcoming_services = self.__load_upcoming_services_dict()
        if username not in upcoming_services:
            upcoming_services[username] = []
        upcoming_services[username].append(service)
        self.__save_upcoming_services_dict(upcoming_services)
    
    def __load_upcoming_services_dict(self):
        if not os.path.exists("upcoming_services_dict.pkl"):
            return {}
        
        with open("upcoming_services_dict.pkl", 'rb') as file:
            return pickle.load(file)
          
    def __save_upcoming_services_dict(self, upcoming_services):
        with open("upcoming_services_dict.pkl", 'wb') as file:
            pickle.dump(upcoming_services, file)
           
    