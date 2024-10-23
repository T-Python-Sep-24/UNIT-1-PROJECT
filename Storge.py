from Products import Products
from Services import Services
import pandas as pd
import pyfiglet
from blessed import Terminal
from termcolor import colored
import pickle
import os
from datetime import datetime
import json

class Storge:
    def __init__(self):
        self.__products = self.__load_products_data()
        self.__services = self.__load_Services_data()
        self.__On_Site_Maintenance = self.__load_On_Site_Maintenance_data()
        self.__RegularMaintenance = self.__load_RegularMaintenance_data()
        
        self.__dates_and_times = self.__load_dates_and_times()
            
    def load_upcoming_services(self):
        if not os.path.exists("upcoming_services.pkl"):
            return []  

        with open("upcoming_services.pkl", 'rb') as file:
            return pickle.load(file)
    
    def display_upcoming_services(self):
        current_datetime = datetime.now()
        upcoming_services = self.load_upcoming_services()

        filtered_services = []
        for service in upcoming_services:
            service_datetime_str = f"{service['date'][0].strftime('%m/%d/%Y')} {service['time']}"  # Correctly format date
            service_datetime = datetime.strptime(service_datetime_str, '%m/%d/%Y %H:%M:%S')  # Adjust format if needed

            if service_datetime > current_datetime:
                filtered_services.append(service)

        if not filtered_services:
            return

        print(colored("\nUpcoming services:", 'green', attrs=['bold']))
        for service in filtered_services:
            print(f'Service name: {service["service"].name}, Date: {service["date"][0].strftime("%m/%d/%Y")}, Time: {service["time"]}')
            print(f'Service description: {service["service"].description}')
        print()
    
    # DATEs and TIMEs PART>>
    def __extract_date(self, row):
        return row['Dates'], []
    
    def __load_times(self):
        times_data = pd.read_excel('availableTimes.xlsx')
        return times_data['Times'].tolist()
       
    def __load_dates_and_times(self):
        dates_data = pd.read_excel('availableDates.xlsx')

        dates_list = dates_data.apply(self.__extract_date, axis=1).tolist()

        times_list = self.__load_times()    
        
        dates_times_list = []
        for date in dates_list:
            dates_times_list.append({'date': date, 'times': times_list})

        return dates_times_list
    
    def add_date(self, date):
        for dict in self.__dates_and_times:
            if dict['date'] == date:
                print(f"Date {date} already exists")
                return False
        
        times_list = self.__load_times()  
        self.__dates_and_times.append({'date': date, 'times': times_list})  

        self.__adding_date_to_excel(date)
        return True

    def __adding_date_to_excel(self, date):
        dates_data = pd.read_excel('availableDates.xlsx')
        
        new_row = pd.DataFrame({'Dates': [date]})
        updated_dates_data = pd.concat([dates_data, new_row], ignore_index=True)

        updated_dates_data.to_excel('availableDates.xlsx', index=False)
        self.__dates_and_times = self.__load_dates_and_times()
        
        print(f"Date {date} added to availableDates.xlsx.")

    def display_dates(self):
        if self.__dates_and_times:
            print("\nAvailable Dates")
            for id, entry in enumerate(self.__dates_and_times, start=1):
                date_obj = entry['date'][0]  
                
                date_str = date_obj.strftime('%m/%d/%Y') 
                print(f'{id}. {date_str}', end='  ')  
                
                if id % 4 == 0:  
                    print() 
            print()  
            return True
        else:
            print('Sorry there are no available dates!')
            return False
    
    def display_times(self, index, date):
        date_entry = self.__dates_and_times[index]
        date_obj = date_entry['date'][0]
        
        available_times = date_entry['times']
        
        if available_times:
            print(f"\nAvailable Times for {date_obj.strftime('%m/%d/%Y')}:")
            for id, time in enumerate(available_times, start=1):
                print(f'{id}. {time.strftime("%H:%M:%S")}', end=', ')
                if id % 4 == 0:
                    print()
            print()  
            return True
        else:
            print(f"No available times for {date_obj.strftime('%m/%d/%Y')}")
            return False
            
    def get_dates_and_times(self):
        return self.__dates_and_times
    
    def get_date(self, date_number:int):
        return self.__dates_and_times[date_number-1]['date']
    
    def get_time(self, date_number:int, time_number:int):
        return self.__dates_and_times[date_number-1]['times'][time_number-1]
    
    def delete_date(self, date):
        if not self.__dates_and_times:
            print('Sorry, there are no available dates to delete.')
            return False

        for i, entry in enumerate(self.__dates_and_times):
            if entry['date'] == date:
                del self.__dates_and_times[i]  
                self.__update_dates_excel()  
                print(f"Date {date[0].strftime('%m/%d/%Y')} has been successfully deleted.")
                return True

        print(f"Date {date[0].strftime('%m/%d/%Y')} not found.")
        return False

    def __update_dates_excel(self):
        dates_list = []
        for dict in self.__dates_and_times:
            dates_list.append(dict['date'])
        dates_data = pd.DataFrame({'Dates': dates_list})
        dates_data.to_excel('availableDates.xlsx', index=False)
    
      
    # PRODUCTs PART>>
    def __extractedProducts(self, row):
        return Products(row['Name'], row['price'], row['quantity'])
    
    def __load_products_data(self):
        productsData = pd.read_excel('Products.xlsx')
            
        extractedRows = productsData.apply(self.__extractedProducts, axis=1).tolist()
        
        return extractedRows
    
    def add_product(self, product:Products):
        self.__products.append(product)

    def display_products(self):
        for id, product in enumerate(self.__products, start=1):
            print(f'{id:<1}', end='')
            product.display()
            
    def get_product(self, product_number:int):
        return self.__products[product_number-1]
    
    
    # NORMAL SERVICEs PART>>
    def __extractedServices(self, row):
        return Services(row['Name'], row['Price'], row['Description'])
    
    def __load_Services_data(self):
        servicesData = pd.read_excel('services.xlsx')
            
        extractedRows = servicesData.apply(self.__extractedServices, axis=1).tolist()
        
        return extractedRows
    
    def add_service(self, service:Services):
        self.__services.append(service)

    def display_services(self):
        for id, service in enumerate(self.__services, start=1):
            print(f'{id}. ', end='')
            print(f'Name: {service.name}, Service Id: {service.service_id}, Price: After performing all necessary repairs')
            print(f'Service Description: {service.description}\n')
    
    def get_service(self, service_number:int):
        return self.__services[service_number - 1]
    
    
    # ON SITE MAINTENANCE SERVICEs PART>>
    def __load_On_Site_Maintenance_data(self):
        servicesData = pd.read_excel('On_Site_Maintenance.xlsx')
            
        extractedRows = servicesData.apply(self.__extractedServices, axis=1).tolist()
        
        return extractedRows
    
    def add_On_Site_Maintenance(self, service:Services):
        self.__On_Site_Maintenance.append(service)

    def display_On_Site_Maintenance(self):
        print("Available services:")
        for id, service in enumerate(self.__On_Site_Maintenance, start=1):
            print(f'{id:<5}', end='')
            service.display()
    
    def get_On_Site_Maintenance(self, service_number:int):
        return self.__On_Site_Maintenance[service_number - 1]
    
    
    # REGULAR MAINTENANCE SERVICEs PART>>
    def __load_RegularMaintenance_data(self):
        servicesData = pd.read_excel('RegularMaintenance.xlsx')
            
        extractedRows = servicesData.apply(self.__extractedServices, axis=1).tolist()
        
        return extractedRows
    
    def add_RegularMaintenance(self, service:Services):
        self.__RegularMaintenance.append(service)

    def display_RegularMaintenances(self):
        print("Available services:")
        for id, service in enumerate(self.__RegularMaintenance, start=1):
            print(f'{id:<5}', end='')
            service.display()
    
    def get_RegularMaintenance(self, service_number:int):
        return self.__RegularMaintenance[service_number - 1]
    
    
    # CAR CLEANING SERVICEs PART>>
