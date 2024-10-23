from Services import Services
from Storge import Storge

class ServiceCart:
    def __init__(self):
        self.cart = {}
        
    def add_to_cart(self, service: Services, date, thetime, storge: Storge):
        if not storge.get_dates_and_times():
            print('Sorry there are no dates available')
            return False
        
        for entry in storge.get_dates_and_times():
            if entry['date'] == date:
                if entry['times']:
                    if thetime in entry['times']:
                        self.cart = {'service': service, 'date': date, 'time': thetime}
                        return True
                    print('Sorry the time is not available!')
                    return False
                print('Sorry there are no times available!')
                return False
        
        print('Sorry the date is not available')
        return False
        
    def display(self):
        if not self.cart:
            print('Cart is empty.')
            return False
        else:
            service = self.cart['service']
            print(f'Service: Name: {service.name}, Price: SAR {service.price}, Will be on Date: {self.cart["date"][0].strftime("%m-%d-%Y")}, At {self.cart["time"]}\n')
            print(f'Service Description: {service.description}\n')
            return True
        
    def delete_cart(self, service:Services):
        self.cart = {}
    
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
    
    