from Car_files.car import Car, CarStorage
import json

class Manager:
    def __init__(self, name, password, car_storage):
        self.name = name
        self.password = password
        self.car_storage = car_storage
        self.customers = []


    def login(self, name, password):
        if self.name == name and self.password == password:
            print("Login successful")
            return True
        else:
            print("Invalid user details")
            return False


    def add_car(self, cname, year, price):
        car = Car(cname, year, price)
        self.car_storage.add_car(car)
        print(f"Car {cname} ({year}) added successfully.")
        self.car_storage.save_file()


    def remove_car(self, cname, year):
        car = self.car_storage.search_car(cname, year)
        if car:
            self.car_storage.remove_car(car)
            print(f"Car {cname} ({year}) removed successfully.")
        else:
            print("Car not found, cannot remove.")
        self.car_storage.save_file()


    def list_all_cars(self):
        print("Listing all cars:")
        self.car_storage.list_car()


    def search_car(self, cname, year):
        car = self.car_storage.search_car(cname, year)
        if car:
            print(f"Car found: {car}")
        else:
            print("Car not found")


    def add_customer(self, customer):
        self.customers.append(customer)


    def rental_history(self):
        for customer in self.customers:
            print(f"Rental history for {customer.name} (ID: {customer.id}):")
            for record in customer.rental_history:
                action = record['action']
                car_name = record['car_name']
                car_year = record['car_year']
                date = record['date']
                print(f"  {action.capitalize()} car {car_name} ({car_year}) on {date}")