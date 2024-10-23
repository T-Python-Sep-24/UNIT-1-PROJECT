import random
import json
import os

class Services:
    def __init__(self, name:str, price:float, description:str):
        self.name = name
        self.price = price
        self.description = description
        
        self.services_ids = self.__load_from_json()
        self.service_id = self.__auto_generate_id()
            
    def __auto_generate_id(self):
        while True:
            if self.name not in self.services_ids:
                id = random.randint(1000, 9999)
                if id not in self.services_ids.values():
                    self.services_ids[self.name] = id
                    self.__save_to_file(self.services_ids)
                    return id
            else:
                return self.__load_from_json()[self.name]
            
    def __save_to_file(self, services_ids:dict):
        with open('services_ids.json', 'w') as file:
            json.dump(services_ids, file)
            
    def __load_from_json(self):
        if os.path.exists('services_ids.json'):
            with open('services_ids.json', 'r') as file:
                return json.load(file)
        else:
            return {}

    def display(self):
        print(f'Name: {self.name}, Service Id: {self.service_id}, Price: SAR {self.price}')
        print(f'Service Description: {self.description}\n')
        
