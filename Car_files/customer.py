from car import Car,CarStorage, car_storage

class customer:
    def __init__(self, name, id,):
        self.name = name
        self.id = id
        self.rented = []
    

    def rent_car(self, cname, year, car_storage):
        car = car_storage.search_car(cname, year)
        if car and car.available :
            car.available = False
            self.rented.append(car)
            print(f"customer {self.name} with id {self.id} has rented car {car.cname}: {car.year}")
        else:
            print(f"car not available try diffrenet car")


    def return_car(self, cname, year):
        for car in self.rented:

            if car.cname == cname and car.year == year:
                car.available = True
                self.rented.remove(car)
                print(f"customer {self.name} with id {self.id} has returned car {car.cname}: {car.year}")
                return
        print("car not rented")
        


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