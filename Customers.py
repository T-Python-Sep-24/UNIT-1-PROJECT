from ProductsCart import ProductsCart
from ProductsOrder import ProductsOrder
import os
import pickle
from ServiceCart import ServiceCart
from ServiceOrder import ServiceOrder
from termcolor import colored

class Customer:
    def __init__(self, name:str, username:str, password:str):
        self.name = name
        self.username = username
        self.__password = password
        
        self.product_cart = ProductsCart()
        self.previous_products_orders = self.__load_products_orders()
        if self.username not in self.previous_products_orders:
                self.previous_products_orders[self.username] = []
        
        self.service_cart = ServiceCart()
        self.upcoming_services = []
        
    def get_password(self):
        return self.__password
    
    def checkout_products_cart(self):  
        try:  
            products_order = ProductsOrder(self, self.product_cart)
            products_order.order_summary()
            
            if input(colored('\nDo you want to checkout to payment? ("y" for Yes and "n" for No) ', 'green', attrs=['bold'])).lower() == 'y':
                products_order.checkout_cart()
                self.product_cart = ProductsCart()
                return True
            
            return False
        except Exception:
            print("Try again!")
            return False
        
    def checkout_service_cart(self, storge):    
        service_order = ServiceOrder(self, self.service_cart)
        service_order.order_summary()
        
        checkout = input('\nDo you want to checkout to payment? ("y" for Yes and "n" for No) ')
        if checkout.lower() == 'y':
            service_order.checkout_cart(storge)
            self.cart = ServiceCart()
            return True
        
        return False
      
    def add_upcoming_service(self, service):
        self.upcoming_services.append(service)

    def display_upcoming_services(self):
        if not self.upcoming_services:
            return
        
        print(colored("\nUpcoming services:", 'green', attrs=['bold']))
        for service in self.upcoming_services:
            print(f'Service name: {service.name}, Date: {service.date.strftime("%m/%d/%Y")}, Time: {service.time}')
            print(f'Service description: {service.description}')
        print()
            
    def __load_products_orders(self):
        if not os.path.exists("previous_products_orders"):
            return {}  
        
        with open("previous_products_orders", 'rb') as file:
            return pickle.load(file)

        
        