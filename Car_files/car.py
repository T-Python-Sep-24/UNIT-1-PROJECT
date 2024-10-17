class Car:
    def __init__(self, cname, year, price, available = True):
        self.cname = cname
        self.year = year
        self.price = price 
        self.available = available


    def __str__(self):
        availability = "Available" if self.available else "Not Available"
        return f"{self.cname} ({self.year}) - ${self.price}/day ({availability})"

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
car_storage = CarStorage()