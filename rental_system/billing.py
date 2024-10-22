from datetime import datetime
from colorama import Fore, Style

class BillingManager:
    def __init__(self, rental_manager):
        self.rental_manager = rental_manager

    def generate_bill(self, rental_id):
        
        try:
            rental_id = int(rental_id) 
            if 0 <= rental_id < len(self.rental_manager.rentals):
                rental = self.rental_manager.rentals[rental_id]
                device_name = rental['device_name']
                for device in self.rental_manager.device_manager.devices:
                    if device['name'] == device_name:
                        days_rented = self.calculate_days(rental['start_date'], rental['end_date'])
                        total_cost = device['daily_price'] * days_rented
                        print(f"Bill for {rental['renter_name']}:\nDevice: {device_name}\nDays rented: {days_rented}\nTotal: {total_cost}")
                        return
            else:
                print("Invalid rental ID.")
        except (ValueError, IndexError):
            print("Invalid rental ID. Please enter a valid number.")

    def calculate_days(self, start_date, end_date):
        date_format = "%Y-%m-%d"
        start = datetime.strptime(start_date, date_format)
        end = datetime.strptime(end_date, date_format)
        return (end - start).days
