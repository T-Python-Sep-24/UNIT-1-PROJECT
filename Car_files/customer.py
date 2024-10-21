from Car_files.car import Car, CarStorage
from Car_files.manager import Manager
import json
import os
from datetime import datetime, timedelta



class Customer:
    def __init__(self, name, id, car_storage, manager):
        self.name = name
        self.id = id
        self.rented = []
        self.car_storage = car_storage
        self.rental_history = []
        self.manager = manager
    
    
    
    def rent_car(self, cname, year):
        car = self.car_storage.search_car(cname, year)
        if car and car.available:
            car.available = False
            car.rented_by = self.id  
            self.rented.append(car)
            rent_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"Customer {self.name} (ID: {self.id}) has rented car {car.cname} ({car.year})")
            self.rental_history.append({
             "action": "rented",
                "car_name": car.cname,
                "car_year": car.year,
                "date": rent_date
            })
            self.manager.add_customer(self)
            self.save_customer_file()

        else:
            print(f"Car not available.")

    
    def return_car(self, cname, year):
        for car in self.rented:
            if car.cname == cname and car.year == year:
                car.available = True
                car.rented_by = None  
                self.rented.remove(car)
                return_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(f"Customer {self.name} (ID: {self.id}) has returned car {car.cname} ({car.year})")
                self.rental_history.append({
                    "action": "returned",
                    "car_name": car.cname,
                    "car_year": car.year,
                    "date": return_date
                })
                self.manager.add_customer(self)
                self.save_customer_file()
                return
        print("Car not rented.")
        


    def search_for_car(self, cname, year, car_storage):
        for car in car_storage.cars:
            if car.name == cname and car.year == year:
                print(car)
                return
        print("car not found")

    


    def my_rented_cars(self):
        for car in self.rented:
            print(f"rented cars are: {car}")
    

    def list_available_cars(self, car_storage):
        for car in car_storage.cars:
            if car.available:
                print(car)
    

    def save_customer_file(self):
        filename = os.path.join(os.path.dirname(__file__), '..', 'data_file', 'customer_data.json')
        if not os.path.exists(filename):
            customers_data = []
        else:
            with open(filename, "r") as f:
                customers_data = json.load(f)

        # Find if the customer already exists based on ID
        existing_customer = None
        for customer in customers_data:
            if customer['id'] == self.id:
                existing_customer = customer
                break
            
        customer_data = {
            "name": self.name,
            "id": self.id,
            "rented": [car.to_dict() for car in self.rented],  
            "rental_history": self.rental_history  
        }

        if existing_customer:
            existing_customer.update(customer_data)
        else:
            customers_data.append(customer_data)

        with open(filename, "w") as f:
            json.dump(customers_data, f, indent=4)
        


    def load_customer_file(self):
        filename = os.path.join(os.path.dirname(__file__), '..', 'data_file', 'customer_data.json')
        
        try:
            with open(filename, "r") as f:
                try:
                    content = f.read().strip()  
                    if content:
                        customers_data = json.loads(content)
                    else:
                        print("Customer data registered")
                        customers_data = []
                except json.JSONDecodeError:
                    print("Error decoding JSON data. Initializing with an empty list.")
                    customers_data = []
            
            for customer in customers_data:
                if customer['id'] == self.id:
                    self.name = customer["name"]
                    self.rented = [Car.from_dict(car_data) for car_data in customer["rented"]]
                    self.rental_history = customer.get("rental_history", [])
                    break
        except FileNotFoundError:
            print("Customer data file not found. Creating a new one.")
            with open(filename, "w") as f:
                json.dump([], f)  
