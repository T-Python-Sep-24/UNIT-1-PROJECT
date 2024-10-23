from Car_files.car import Car, CarStorage
import pandas as pd
from datetime import datetime

class Manager:
    def __init__(self, name, password, car_storage):
        self.name = name
        self._password = password
        self.car_storage = car_storage
        self.customers = []


    def _validate_password(self, password):
        return self._password == password
    

    def login(self, name, password):
        if self.name == name and self._validate_password(password):
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
        for existing_customer in self.customers:
            if existing_customer.id == customer.id:
                return  
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

    
    def rented_cars(self):
        print("Rented Cars and their Renters:")
        any_rented = False 
    
        for customer in self.customers:
            rented_cars = customer.get_rented_cars()
            if rented_cars:
                any_rented = True  
                print(f"Customer {customer.name} (ID: {customer.id}) has rented the following cars:")
                for car in rented_cars:
                    print(f"  - {car.cname} ({car.year})")

        if not any_rented:
            print("No rented cars.")
    

    

    def rental_stats(self):
        rental_data = []

        # Collect rental history data for analysis
        for customer in self.customers:
            for record in customer.get_rental_history():  # Call the method to get rental history
                if record['action'] == 'rented':
                    rental_data.append({
                        'car_name': record['car_name'],
                        'date': datetime.strptime(record['date'], "%Y-%m-%d %H:%M:%S")
                    })
        
        # Convert the list of rental data into a DataFrame
        df = pd.DataFrame(rental_data)

        if df.empty:
            print("No rental history available.")
            return

        # Calculate the most rented car
        most_rented_car = df['car_name'].value_counts().idxmax()
        most_rented_count = df['car_name'].value_counts().max()

        # Calculate average renting days
        df['next_date'] = df['date'].shift(-1)  # Shift dates to find the next rental
        df['rental_days'] = (df['next_date'] - df['date']).dt.days
        average_renting_days = df['rental_days'].mean()

        print(f"Most rented car: {most_rented_car} (Rented {most_rented_count} times)")
        print(f"Average renting days: {average_renting_days:.2f} days")


