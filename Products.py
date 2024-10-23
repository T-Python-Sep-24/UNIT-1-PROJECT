import random
import json
import os

class Products:
    def __init__(self, name, price, quantity):
        self.name = name
        self.products_ids = self.__load_from_json()
        self.product_id = self.__auto_generate_id()
        self.price = price
        self.quantity = quantity
    
    def __auto_generate_id(self):
        while True:
            if self.name not in self.products_ids:
                id = random.randint(100, 999)
                if id not in self.products_ids.values():
                    self.products_ids[self.name] = id
                    self.__save_to_file(self.products_ids)
                    return id
            else:
                return self.__load_from_json()[self.name]
            
    def __save_to_file(self, products_ids: dict):
        with open('products_ids.json', 'w') as file:
            json.dump(products_ids, file)
            
    def __load_from_json(self):
        if os.path.exists('products_ids.json'):
            with open('products_ids.json', 'r') as file:
                return json.load(file)
        else:
            return {}

    def display(self):
        print(f'{'':<5}{self.name:<25}{self.product_id:<12}SAR {self.price:<10}{self.quantity:<12}')
        # print(f'Name: {self.name}, Product Id: {self.product_id}, Price: SAR {self.price}, Stock Quantity: {self.quantity}')