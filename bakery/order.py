from datetime import datetime

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

    def __init__(self, orderedProducts: list[OrderedProduct], payment: str, delivered: bool=False, deliveryAddress: str = ""):
        self.__date = datetime.today()
        self.__orderedProducts = orderedProducts
        self.__payment = payment
        self.__delivered = delivered
        self.__deliveryAddress = deliveryAddress

    def getPayment(self) -> str:
        '''Getter for payment attribute'''
        return self.__payment
    
    def isDelivered(self) -> bool:
        '''This method returns True if the order was delivered and False otherwise'''
        return self.__delivered
    
    def setDeliveryAddress(self, deliveryAdd: str):
        '''Setter for delivery address attribute'''
        self.__deliveryAddress = deliveryAdd

    def getDeliveryAddress(self) -> str:
        '''Getter for delivery address attribute'''
        return self.__deliveryAddress
    
    def orderInfo(self) -> Table:
        '''This method returns the details of the order'''
        #Create table of ordered products in an order
        productsTable: Table = Table(title="Order Details:",title_style="bold #aceaff" ,title_justify="left", box=box.SIMPLE, show_footer=True, border_style="#daf5ff")
        
        #Adding columns to the table 
        productsTable.add_column("[bold #fdffc3]Product Name[/]")
        productsTable.add_column("[bold #bdeeff]Quantity[/]", justify = "center", footer=f"Ordered on: {datetime.strftime(self.__date, '%Y-%m-%d %H:%M:%S')}", footer_style="#aceaff")
        productsTable.add_column("[bold #a4d5b5]Price[/]", justify = "center")
        
        #Adding rows for each product in the ordered products
        for prod in self.__orderedProducts:
            totalPerProduct: float = prod.getQty() * prod.getPrice()
            productsTable.add_row(f"[#fdffc3]{prod.getName()}[/]", f"[#bdeeff]{prod.getQty()}[/]", f"[#a4d5b5]{totalPerProduct}[/]")
        
        if self.isDelivered():
            productsTable.add_row(f"[#aceaff]Delivered to:[/]", f"[#daf5ff]{self.getDeliveryAddress()}[/]")
        else:
            productsTable.add_row(None, f"[#aceaff]Ordered for pickup[/]", None)
        
        return productsTable
