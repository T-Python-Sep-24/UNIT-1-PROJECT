from datetime import datetime
import pickle, json

#Using rich library to style output on terminal
from rich.table import Table
from rich import box
from rich.text import Text

class OrderedProduct:

    def __init__(self, productName: str, qty: int, price: float):
        self.__productName = productName
        self.__qty = qty
        self.__price = price

    def setQty(self, qty: int):
        '''
        Setter for quantity(qty) attribute
        '''
        self.__qty = qty
    
    def getName(self) -> str:
        '''
        Getter for name attribute
        '''
        return self.__productName
    
    def getQty(self) -> int:
        '''
        Getter for qty attribute
        '''
        return self.__qty
    
    def getPrice(self) -> float:
        '''
        Getter for price attribute
        '''
        return self.__price

class Order:

    def __init__(self, orderedProducts: list[OrderedProduct]):
        self.__date = datetime.today()
        self.__orderedProducts = orderedProducts

    def orderInfo(self) -> str:
        '''This method returns the details of the order'''
        products: str = ""
        for prod in self.__orderedProducts:
            total: float = prod.getQty() * prod.getPrice()
            products += f"Product name: {prod.getName()}. Quantity: {prod.getQty()}. Price: {total}\n"
        return f"{products} Ordered on: {self.__date}\n"
