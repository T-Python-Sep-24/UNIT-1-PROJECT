import json
import os

class Car:
    def __init__(self, cname, year, price, available = True):
        self.cname = cname
        self.year = year
        self.price = price 
        self.available = available


    def __str__(self):
        availability = "Available" if self.available else "Not Available"
        return f"{self.cname} ({self.year}) - ${self.price}/day ({availability})"
    

    def to_dict(self):
        return {
            "cname": self.cname,
            "year": self.year,
            "price": self.price,
            "available": self.available
        }

    @classmethod
    def from_dict(self, data):
        return self(data['cname'], data['year'], data['price'], data['available'])

class CarStorage():
    def __init__(self):
        self.cars = []


    def add_car(self, car):
        self.cars.append(car)
        


    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
        else:
            print("car not found")
        

    
    def search_car(self, cname, year):
        for car in self.cars:
            if car.cname == cname and car.year == year and car.available :
                return car
            
        print("car not found")
        return None


    def list_car(self):
        if not self.cars:
            print("no cars found")
        else:
            for car in self.cars:
                print(car)


    def save_file(self):
        file_path = os.path.join(os.path.dirname(__file__), '..', 'data_file', 'cars.json')
        with open(file_path, 'w') as f:
            cars_data = [{'cname': car.cname, 'year': car.year, 'price': car.price, 'available': car.available} for car in self.cars]
            json.dump(cars_data, f)


    def load_file(self):
        file_path = os.path.join(os.path.dirname(__file__), '..', 'data_file', 'cars.json')
        with open(file_path, 'r') as f:
            cars_data = json.load(f)
            self.cars = [Car(car['cname'], car['year'], car['price'], car['available']) for car in cars_data]
            
