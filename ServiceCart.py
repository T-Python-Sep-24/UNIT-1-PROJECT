from Services import Services

class ServiceCart:
    def __init__(self):
        self.cart = {}
        
    def add_to_cart(self, service:Services, date, time):
        if len(service.dates_and_times['dates']) > 0 and len(service.dates_and_times['times']) > 0:
            self.cart[service.service_id] = {'service': service, 'date': date, 'time': time}
            # Here I should remove date and time from there lists in Services class
            return True
            
        return False
        
    def display(self):
        if self.is_empty():
            return False
        else:
            print(f'Service. Name: {self.cart['service'].name}, Price: {self.cart['service'].price}, Will be on Date: {self.cart['date']}, At {self.cart['time']}')
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