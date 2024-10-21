from bakery.order import *
import json
from rich import print
from rich.table import Table
from rich import box
from rich.prompt import Prompt, IntPrompt, FloatPrompt

class Person:

    def __init__(self, name: str, age: int, gender: str, phone: str, password: str) -> None:
        self.__name = name
        self.__age = age 
        self.__gender = gender
        self.__phone = phone
        self.__password = password
        self.__role = ''

    def setName(self, name: str):
        '''
        Setter for name attribute
        '''
        self.__name = name

    def setAge(self, age: int):
        '''
        Setter for age attribute
        '''
        self.__age = age

    def setGender(self, gender: str):
        '''
        Setter for gender attribute
        '''
        self.__gender = gender

    def setPhone(self, phone: str):
        '''
        Setter for gender attribute
        '''    
        self.__phone = phone

    def setPassword(self, password: str):
        '''
        Setter for gender attribute
        '''    
        self.__password = password    

    def getName(self) -> str:
        '''
        Getter for name attribute
        '''
        return self.__name

    def getAge(self) -> int:
        '''
        Getter for age attribute
        '''
        return self.__age
    
    def getGender(self) -> str:
        '''
        Getter for gender attribute
        '''
        return self.__gender
    
    def getPhone(self) -> str:
        '''
        Getter for phone attribute
        '''
        return self.__phone
    
    def getPassword(self) -> str:
        '''
        Getter for password attribute
        '''
        return self.__password
    
    def getRole(self):
        '''
        Getter for role attribute
        '''
        return self.__role
    
    def listAllProducts(self) -> Table:
        '''
        This method retrieves the list of all products from json file and returns a Table object containing the menu
        '''
        menu: dict = self.__loadFromJSON()

        #Creating a table object to display menu
        menuTable: Table = Table(title = "[bold purple]Stellar Bakery Menu[/]", expand=False, box=box.SIMPLE)

        #Adding columns to the table
        menuTable.add_column("Product Name", style = "bold cyan")
        menuTable.add_column("Quantity", style = "bold magenta", justify = "center")
        menuTable.add_column("Price Per Piece", style = "bold green", justify = "center")

        if menu:
            #Create a row for each product in the menu 
            for prod in menu:
                menuTable.add_row(f"[bold #f2f4bd]{prod}[/]",f"[bold #f2f4bd]{menu[prod]['qty']}[/]",f"[bold #a4d5b5]{menu[prod]['price']} SR[/]")
            return menuTable
        else: 
            return "Your menu is empty."
        
    def __loadFromJSON(self) -> dict: 
        '''
        Call this method whenever you want to load from a json file and make neccessary checks
        '''
        menu: dict = {}
        try:
            with open("bakeryData/menu.json", "r", encoding="utf-8") as file:
                #Get the information from the json file by using .load() function
                menu = json.load(file)
        except FileNotFoundError:
            print("File doesn't Exist.")
        except Exception as e:
            print(f"An error occured, {e.__class__}")
        finally:
            return menu
        
class Customer(Person):

    def __init__(self, name: str, age: int, gender: str, phone: str, password: str):
        super().__init__(name, age, gender, phone, password)
        self.__orderHistory: list[Order] = []
        self.__role = "customer"

    def setOrderHistory(self, orderHistory: list[Order]):
        '''
        setter for orderHistory attribute
        '''
        self.__orderHistory = orderHistory

    def getOrderHistory(self,) -> list[Order]:
        '''
        Getter for orderHistory attribute
        '''
        return self.__orderHistory
    
    def getRole(self):
        '''
        Getter for role attribute
        '''
        return self.__role

    def getInfo(self) -> str:
        '''
        This method returns a formatted string containing customer info
        '''
        info: str = f"Name: {self.getName()}.\nAge: {self.getAge()}.\nGender: {self.getGender()}.\nPhone number: {self.getPhone()}.\nOrder history:\n"

        for order in self.getOrderHistory():
            info += {order.orderInfo()}
        
        return info

class Employee(Person):

    def __init__(self, name: str, age: int, gender: str, phone: str, password: str):
        super().__init__(name, age, gender, phone, password)
        self.__role = "employee"

    def getRole(self):
        '''
        Getter for role attribute
        '''
        return self.__role

    def addProduct(self, prodName: str, qty: int, price: float):
        '''
        This method adds a product to a json file containing all products
        '''
        #Use the method below to get the menu from the json file
        menu: dict = self.__loadFromJSON()

        menu[prodName]= {
            'qty': qty,
            'price': price
        }
        with open("bakeryData/menu.json", "w", encoding="utf-8") as file:
            #Store the modified menu in a json file 
            json.dump(menu, file, indent = 4)
    
    def removeProduct(self, prodName: str) -> str:
        '''
        This method removes a product from the menu then saves the modified menu to the json file
        '''
        menu: dict = self.__loadFromJSON()
        
        if menu:
            #Check if the product is on the menu
            if prodName in menu:
                del menu[prodName]
                with open("bakeryData/menu.json", "w", encoding="utf-8") as file:
                    #Store the modified menu back to the json file 
                    json.dump(menu, file, indent = 4)
                return f"Product '{prodName}' was deleted successfully."
            else: 
                return f"Product '{prodName}' isn't on the menu."
        else: 
            return "Your menu is empty."

    def updateProductName(self, prodName: str, newName):
        '''
        This method updates a product's name then saves the modified menu to the json file
        '''
        menu: dict = self.__loadFromJSON()
        
        if menu:
            #Check that the product is on the menu
            if prodName in menu:
                #Update the price of the product
                menu[newName] = menu[prodName]
                del menu[prodName]
                with open("bakeryData/menu.json", "w", encoding="utf-8") as file:
                    #Store the modified menu back to the json file 
                    json.dump(menu, file, indent = 4)
                return f"Name of '{prodName}' was updated successfully."
            else:
                return f"Product '{prodName}' isn't on the menu."
        else: 
            return "Your menu is empty."

    def updateProductQty(self, prodName: str, qty: int):
        '''
        This method updates a product's quantity then saves the modified menu to the json file
        '''
        menu: dict = self.__loadFromJSON()
        
        if menu:
            #Check that the product is on the menu
            if prodName in menu:
                #Modify the quantity of the product
                menu[prodName]["qty"] = qty
                with open("bakeryData/menu.json", "w", encoding="utf-8") as file:
                    #Store the modified menu back to the json file 
                    json.dump(menu, file, indent = 4)
                return f"Quantity of '{prodName}' was updated successfully."
            else:
                return f"Product '{prodName}' isn't on the menu."
        else: 
            return "Your menu is empty."
        
    def updateProductPrice(self, prodName: str, price: float):
        '''
        This method updates a product's price then saves the modified menu to the json file
        '''
        menu: dict = self.__loadFromJSON()
        
        if menu:
            #Check that the product is on the menu
            if prodName in menu:
                #Update the price of the product
                menu[prodName]["price"] = price
                with open("bakeryData/menu.json", "w", encoding="utf-8") as file:
                    #Store the modified menu back to the json file 
                    json.dump(menu, file, indent = 4)
                return f"Price of '{prodName}' was updated successfully."
            else:
                return f"Product '{prodName}' isn't on the menu."
        else: 
            return "Your menu is empty."
        
    def updateProduct(self, prodName: str, choice: str) -> str:
        '''
        This method takes product name and choice as arguments and updates the product based on the choice entered
        If the choice was 1 -> update product name
        If the choice was 2 -> update product quantity
        If the choice was 3 -> update product price
        '''
        if choice == '1':
            newName: str = Prompt.ask("[#f2f4bd]Enter the new name[/]")
            return self.updateProductName(prodName, newName)
        elif choice == '2':
            newQty: int = IntPrompt.ask("[#f2f4bd]Enter the new quantity[/]")
            return self.updateProductQty(prodName, newQty)
        elif choice == '3':
            newPrice: float = FloatPrompt.ask("[#f2f4bd]Enter the new price[/]")
            return self.updateProductPrice(prodName, newPrice)

    def checkExpiry(self):
        '''This method checks if there are any expired objects'''