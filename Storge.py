from Products import Products
from Services import Services
import pandas as pd

class Storge:
    def __init__(self):
        self.__products = self.__load_products_data()
        self.__services = self.__load_Services_data()
        self.__On_Site_Maintenance = self.__load_On_Site_Maintenance_data()
        self.__RegularMaintenance = self.__load_RegularMaintenance_data()
        
        self.__dates_and_times = self.__load_dates_and_times()
    
    # DATEs and TIMEs PART>>
    def __extract_date(self, row):
            return row['Date'], []
    
    def __load_times(self):
        times_data = pd.read_excel('availableTimes.xlsx')
        return times_data['Time'].tolist()
       
    def __load_dates_and_times(self):
        dates_data = pd.read_excel('availableDates.xlsx')

        extracted_dates_times = dates_data.apply(self.__extract_date, axis=1).tolist()
        dates_times = dict(extracted_dates_times)

        times_list = self.__load_times()  
        
        for date in dates_times.keys():
            dates_times[date] = times_list  

        return dates_times
    
    def add_date(self, date):
        if date in self.__dates_and_times:
            print(f"Date {date} already exists")
            return False
        
        times_list = self.__load_times()  
        self.__dates_and_times[date] = times_list  

        self.__adding_date_to_excel(date)
        return True

    def __adding_date_to_excel(self, date):
        dates_data = pd.read_excel('availableDates.xlsx')
        
        new_row = pd.DataFrame({'Date': [date]})
        updated_dates_data = pd.concat([dates_data, new_row], ignore_index=True)

        updated_dates_data.to_excel('availableDates.xlsx', index=False)
        self.__dates_and_times = self.__load_dates_and_times()
        
        print(f"Date {date} added to availableDates.xlsx.")

    def display_dates(self):
        print("Available dates")
        for date in self.__dates_and_times:
            print(date)
    
    def display_times(self, date):
        if date in self.__dates_and_times:
            print(f"Available times for {date}:")
            for time in self.__dates_and_times[date]:
                print(time)
        else:
            print(f"No available times for {date}. Date not found.")
            
    def get_dates_and_times(self):
        return self.__dates_and_times
    
    def delete_date(self, date):
        if date in self.__dates_and_times:
            del self.__dates_and_times[date]
            self.__update_dates_excel()  
        else:
            print(f"Date {date} not found.")

    def __update_dates_excel(self):
        dates_data = pd.DataFrame({'Date': list(self.__dates_and_times.keys())})
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
        print("Available products in stock:")
        for id, product in enumerate(self.__products, start=1):
            print(f'{id:<5}', end='')
            print(product.display())
            
    def get_product(self, product_number:int):
        return self.__products[product_number]
    
    
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
        print("Available services:")
        for id, service in enumerate(self.__services, start=1):
            print(f'{id:<5}', end='')
            print(service.display())
    
    def get_services(self, services_number:int):
        return self.__services[services_number]
    
    
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
            print(service.display())
    
    def get_On_Site_Maintenance(self, service_number:int):
        return self.__On_Site_Maintenance[service_number]
    
    
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
            print(service.display())
    
    def get_RegularMaintenance(self, service_number:int):
        return self.__RegularMaintenance[service_number]
    
    
    # CAR CLEANING SERVICEs PART>>
