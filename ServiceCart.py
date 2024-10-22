from Services import Services
from Storge import Storge
from datetime import datetime

class ServiceCart:
    def __init__(self):
        self.cart = {}
        self.storge = Storge()
        
    def add_to_cart(self, service: Services, date, time):
        if date in self.storge.get_dates_and_times() and time in self.storge.get_dates_and_times()[date]:
            self.cart = {'service': service, 'date': date, 'time': time}
            return True
            
        return False
    
    def display_upcoming_services(self):
        current_datetime = datetime.now()
        upcoming_services = []

        for service in self.cart.values():
            service_date = datetime.strptime(service['date'], '%Y-%m-%d')
            service_time = datetime.strptime(service['time'], '%I:%M %p')
            service_datetime = datetime.combine(service_date.date(), service_time.time())

            if service_datetime > current_datetime:
                upcoming_services.append(service)

        if not upcoming_services:
            print("There are no upcoming services right now.")
        else:
            print("Upcoming services:")
            for service in upcoming_services:
                print(f'Service: {service["service"].name}, Date: {service["date"]}, Time: {service["time"]}')
        
    def display(self):
        if not self.cart:
            return False
        else:
            print(f'Service: Name: {self.cart['service'].name}, Price: {self.cart['service'].price}, Will be on Date: {self.cart['date']}, At {self.cart['time']}')
            print(f'Service Description: {self.cart['service'].description}')
            return True
    
    def delete_from_cart(self, service:Services):
        if service.service_id == self.cart['service'].service_id:
            del self.cart[service.service_id]
            return True
        
        return False
    
    def change_date(self, service:Services, date):
        if service.service_id == self.cart['service'].service_id:
            self.cart[service.service_id]['date'] = date
            return True
        
        return False
    
    def change_time(self, service:Services, time):
        if service.service_id == self.cart['service'].service_id:
            self.cart[service.service_id]['time'] = time
            return True
        
        return False
    
    def total_cost(self):
        return self.cart['service'].price
    
    