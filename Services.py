import random
import json
import os

class Services:
    def __init__(self, name:str, price:float, availability:bool, dates, times):
        self.name = name
        self.price = price
        self.services_ids = self.__load_from_json()
        self.service_id = self.__auto_generate_id()
        
        self.availability = availability
        self.dates_and_times = {'dates': dates, 'times': times}
    
    def __auto_generate_id(self):
        while True:
            id = random.randint(51, 99)
            if id not in self.services_ids:
                self.services_ids.add(id)
                self.__save_to_file(self.services_ids)
                return id
            
    def __save_to_file(self, services_ids:dict):
        with open('services_ids.json', 'w') as file:
            json.dump(list(services_ids), file)
            
    def __load_from_json(self):
        if os.path.exists('services_ids.json'):
            with open('services_ids.json', 'r') as file:
                return set(json.load(file))
        else:
            return set()

    def display(self):
        print(f'Name: {self.name}, Service Id: {self.service_id}, Price: SAR {self.price}, Service Availability: {"Available" if self.availability else "Not Available"}')