from Car_files.car import Car, CarStorage
import json
import os


class Customer:
    def __init__(self, name, id, car_storage):
        self.name = name
        self.id = id
        self.rented = []
        self.car_storage = car_storage
    
    

    def rent_car(self, cname, year):
        car = self.car_storage.search_car(cname, year)
        if car and car.available:
            car.available = False
            car.rented_by = self.id  
            self.rented.append(car)
            print(f"Customer {self.name} (ID: {self.id}) has rented car {car.cname} ({car.year})")
            self.save_customer_file()

        else:
            print(f"Car not available.")


    def return_car(self, cname, year):
        for car in self.rented:
            if car.cname == cname and car.year == year:
                car.available = True
                car.rented_by = None  
                self.rented.remove(car)
                print(f"Customer {self.name} (ID: {self.id}) has returned car {car.cname} ({car.year})")
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
        with open(filename, "w") as f:
            json.dump({
                "name": self.name,
                "id": self.id,
                "rented": [car.to_dict() for car in self.rented]
            }, f)
        


    def load_customer_file(self):
        filename = os.path.join(os.path.dirname(__file__), '..', 'data_file', 'customer_data.json')
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.name = data["name"]
                self.id = data["id"]
                self.rented = [Car.from_dict(car_data) for car_data in data["rented"]]
        except FileNotFoundError:
            print("No customer data found.")


def rental_fee_decorator():
    pass