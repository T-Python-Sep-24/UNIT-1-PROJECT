from Products import Products
from Services import Services

class Storge:
    def __init__(self):
        self.__products = []
        self.__services = []

    def add_product(self, product:Products):
        self.__products.append(product)

    def display_products(self):
        print("Available products in stock:")
        i=1
        for product in self.__products:
            print(i)
            print(product.display())
            i+=1
            
    def get_product(self, product_number:int):
        return self.__products[product_number]
    
    def add_service(self, services:Services):
        self.__services.append(services)

    def display_services(self):
        print("Available services:")
        i=1
        for services in self.__services:
            print(i)
            print(services.display())
            i+=1
            
    def get_services(self, services_number:int):
        return self.__services[services_number]
