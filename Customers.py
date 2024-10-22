from ProductsCart import ProductsCart
from ProductsOrder import ProductsOrder
import os
import pickle
import json
from ServiceCart import ServiceCart
from ServiceOrder import ServiceOrder

class Customer:
    def __init__(self, name:str, username:str, password:str):
        self.name = name
        self.username = username
        self.__password = password
        
        self.product_cart = ProductsCart()
        self.previous_products_orders = self.__load_products_orders_from_json()
        
        self.service_cart = ServiceCart()
        self.previous_products_orders = self.__load_products_services_from_json()
        
    def get_password(self):
        return self.__password
    
    def checkout_products_cart(self):    
        products_order = ProductsOrder(self, self.product_cart)
        products_order.order_summary()
        
        checkout = input('\nDo you want to add more items to your shopping cart? ("y" for Yes and "n" for No)')
        if checkout.lower() == 'y':
            products_order.checkout_cart()
            self.__Reset_ProductsCart()
            return True
        
        return False
    
    def __Reset_ProductsCart(self):
        self.product_cart = ProductsCart()
        
    def checkout_service_cart(self):    
        products_order = ServiceOrder(self, self.service_cart)
        products_order.order_summary()
        products_order.checkout_cart()
        self.__Reset_servicesCart()
                
    def __Reset_servicesCart(self):
        self.cart = ServiceCart()
            
    def __load_products_orders_from_json(self):
        if os.path.exists('previous_products_orders.json'):
            with open('previous_products_orders.json', 'r') as file:
                return json.load(file)
        else:
            return {}
        
    def __load_products_services_from_json(self):
        if os.path.exists('previous_services_orders.json'):
            with open('previous_services_orders.json', 'r') as file:
                return json.load(file)
        else:
            return {}
            
    # def load_from_file(self):
    #     if not os.path.exists("previous_products_orders"):
    #         return {}  
        
    #     with open("previous_products_orders", 'rb') as file:
    #         return pickle.load(file)
    