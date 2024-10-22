from bakery.order import *
from bakery.cart import Cart
import json

#Using rich for customizing output on terminal
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
        menu: dict = self.loadFromJSON()

        #Creating a table object to display menu
        menuTable: Table = Table(title = "Stellar Bakery Menu", title_style="italic bold #f0cfff", border_style="#dadada",expand=False, box=box.MINIMAL_DOUBLE_HEAD)

        #Adding columns to the table
        menuTable.add_column("[bold #fdffc3]Product Name[/]")
        menuTable.add_column("[bold #bdeeff]Quantity[/]", justify = "center")
        menuTable.add_column("[bold #a4d5b5]Price Per Piece[/]", justify = "center")

        if menu:
            #Create a row for each product in the menu 
            for prod in menu:
                menuTable.add_row(f"[#feffde]{prod}[/]",f"[#daf5ff]{menu[prod]['qty']}[/]",f"[#ccefd8]{menu[prod]['price']} SR[/]")
            return menuTable
        else: 
            return "Your menu is empty."
        
    def loadFromJSON(self) -> dict: 
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

    def __init__(self, name: str, age: int, gender: str, phone: str, password: str, deliveryAddress: str):
        super().__init__(name, age, gender, phone, password)
        self.__deliveryAdress = deliveryAddress
        self.__orderHistory: list[Order] = []
        self.__role = "customer"
        self.__cart = Cart()
    
    def setDeliveryAddress(self, deliveryAddress: str):
        '''Setter for delivery address attribute'''
        self.__deliveryAdress = deliveryAddress

    def getDeliveryAddress(self):
        '''Getter for delivery adress attribute'''
        return self.__deliveryAdress

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

    def setCart(self, cart: Cart):
        '''Setter for cart attribute'''
        self.__cart = cart

    def getCart(self) -> Cart:
        '''Getter for cart attribute'''
        return self.__cart

    def getInfo(self) -> str:
        '''
        This method returns a Table object containing customer info
        '''
        #Using rich to style the customer info below 
        infoTable: Table =  Table("[bold #5dd6ff]Personal information:[/]", title_justify="left", box=box.MINIMAL_DOUBLE_HEAD, border_style="#daf5ff")
        infoTable.add_row(f"[#aceaff]Name:[/] [not bold #daf5ff]{self.getName()}.[/]", style="bold")
        infoTable.add_row(f"[#aceaff]Age:[/] [not bold #daf5ff]{self.getAge()}.[/]", style="bold")
        infoTable.add_row(f"[#aceaff]Gender:[/] [not bold #daf5ff]{self.getGender()}.[/]", style="bold")
        infoTable.add_row(f"[#aceaff]Phone number:[/] [not bold #daf5ff]{self.getPhone()}.[/]", style="bold")
        infoTable.add_row(f"[#aceaff]Delivery address:[/] [not bold #daf5ff]{self.getDeliveryAddress()}.[/]", style="bold")
        #Make sure that there are previous orders to display
        if self.__orderHistory != []:
            for order in self.__orderHistory:
                infoTable.add_row(order.orderInfo())
        else:
            infoTable.add_row(f"[bold #aceaff]Order History:[/] [italic #daf5ff]You have no previous orders..[/]")
        return infoTable

class Employee(Person):

    def __init__(self, name: str, age: int, gender: str, phone: str, password: str):
        super().__init__(name, age, gender, phone, password)
        self.__role = "employee"

    def getRole(self):
        '''
        Getter for role attribute
        '''
        return self.__role

    def addProduct(self, prodName: str, qty: int, price: float, expDate: str):
        '''
        This method adds a product to a json file containing all products
        '''
        #Use the method below to get the menu from the json file
        menu: dict = Person.loadFromJSON()

        menu[prodName]= {
            'qty': qty,
            'price': price,
            'exp date': expDate
        }
        with open("bakeryData/menu.json", "w", encoding="utf-8") as file:
            #Store the modified menu in a json file 
            json.dump(menu, file, indent = 4)
    
    def removeProduct(self, prodName: str) -> str:
        '''
        This method removes a product from the menu then saves the modified menu to the json file
        '''
        menu: dict = Person.loadFromJSON()
        
        if menu:
            #Check if the product is on the menu
            if prodName in menu:
                del menu[prodName]
                with open("bakeryData/menu.json", "w", encoding="utf-8") as file:
                    #Store the modified menu back to the json file 
                    json.dump(menu, file, indent = 4)
                return Text(f"Product '{prodName}' was deleted successfully.", style="#baf5ce")
            else: 
                return Text(f"Product '{prodName}' isn't on the menu.", style="red")
        else: 
            return Text("The menu is empty.", style="italic #fbfbe2")

    def updateProductName(self, prodName: str, newName) -> Text:
        '''
        This method updates a product's name then saves the modified menu to the json file
        '''
        menu: dict = Person.loadFromJSON()
        
        if menu:
            #Check that the product is on the menu
            if prodName in menu:
                #Update the price of the product
                menu[newName] = menu[prodName]
                del menu[prodName]
                with open("bakeryData/menu.json", "w", encoding="utf-8") as file:
                    #Store the modified menu back to the json file 
                    json.dump(menu, file, indent = 4)
                return Text(f"Name of '{prodName}' was updated successfully.", style="#baf5ce")
            else:
                return Text(f"Product '{prodName}' isn't on the menu.", style="red")
        else: 
            return Text("Your menu is empty.", style="italic #fbfbe2")

    def updateProductQty(self, prodName: str, qty: int) -> Text:
        '''
        This method updates a product's quantity then saves the modified menu to the json file
        '''
        menu: dict = Person.loadFromJSON()
        
        if menu:
            #Check that the product is on the menu
            if prodName in menu:
                #Modify the quantity of the product
                menu[prodName]["qty"] = qty
                with open("bakeryData/menu.json", "w", encoding="utf-8") as file:
                    #Store the modified menu back to the json file 
                    json.dump(menu, file, indent = 4)
                return Text(f"Quantity of '{prodName}' was updated successfully.", style="#baf5ce")
            else:
                return Text(f"Product '{prodName}' isn't on the menu.", style="red")
        else: 
            return Text("Your menu is empty.", style="italic #fbfbe2")
        
    def updateProductPrice(self, prodName: str, price: float) -> Text:
        '''
        This method updates a product's price then saves the modified menu to the json file
        '''
        menu: dict = Person.loadFromJSON()
        
        if menu:
            #Check that the product is on the menu
            if prodName in menu:
                #Update the price of the product
                menu[prodName]["price"] = price
                with open("bakeryData/menu.json", "w", encoding="utf-8") as file:
                    #Store the modified menu back to the json file 
                    json.dump(menu, file, indent = 4)
                return Text(f"Price of '{prodName}' was updated successfully.", style="#baf5ce")
            else:
                return Text(f"Product '{prodName}' isn't on the menu.", style="red")
        else: 
            return Text("The menu is empty.", style="italic #fbfbe2")
        
    def updateProduct(self, prodName: str, choice: str) -> Text:
        '''
        This method takes product name and choice as arguments and updates the product based on the choice entered
        If the choice was 1 -> update product name
        If the choice was 2 -> update product quantity
        If the choice was 3 -> update product price
        '''
        if choice == '1':
            newName: str = Prompt.ask("[#fbfbe2]Enter the new name[/]")
            return self.updateProductName(prodName, newName)
        elif choice == '2':
            newQty: int = IntPrompt.ask("[#fbfbe2]Enter the new quantity[/]")
            return self.updateProductQty(prodName, newQty)
        elif choice == '3':
            newPrice: float = FloatPrompt.ask("[#fbfbe2]Enter the new price[/]")
            return self.updateProductPrice(prodName, newPrice)

    #Overriding the method from parent class to modify its contents
    def listAllProducts(self) -> Table:
        '''
        This method retrieves the list of all products from json file and returns a Table object containing the menu
        '''

        #Retrieving menu from the json file
        menu: dict = Person.loadFromJSON(self)

        #Creating a table object to display menu
        menuTable: Table = Table(title = "Stellar Bakery Menu", title_style="italic bold #f0cfff", border_style="#dadada",expand=False, box=box.MINIMAL_DOUBLE_HEAD)

        #Adding columns to the table
        menuTable.add_column("[bold #fdffc3]Product Name[/]")
        menuTable.add_column("[bold #bdeeff]Quantity[/]", justify = "center")
        menuTable.add_column("[bold #a4d5b5]Price Per Piece[/]", justify = "center")
        menuTable.add_column("[bold #ffbfcb]Expiry Date[/]", justify = "center")

        if menu:
            #Create a row for each product in the menu 
            for prod in menu:
                menuTable.add_row(f"[#feffde]{prod}[/]",f"[#daf5ff]{menu[prod]['qty']}[/]",f"[#ccefd8]{menu[prod]['price']} SR[/]", f"[#ffd7f0]{menu[prod]['exp date']}")
            return menuTable
        else: 
            return Text("The menu is empty.", style="italic #fbfbe2")

    def checkExpired(self) -> Table:
        '''This method returns a Table containing all expired items'''

        #Retrieving menu from the json file
        menu: dict = Person.loadFromJSON(self)

        #Create table of expired products on the menu
        expiredTable: Table = Table(title="Expired Products:",title_style="bold #ffd7f0" ,title_justify="left", box=box.SIMPLE, show_footer=True, border_style="#daf5ff")
        
        #Adding columns to the table 
        expiredTable.add_column("[bold #fdffc3]Product Name[/]")
        expiredTable.add_column("[bold #bdeeff]Quantity[/]", justify = "center")
        expiredTable.add_column("[bold #a4d5b5]Price[/]", justify = "center")
        expiredTable.add_column("[bold #ffd7f0]Expiry Date[/]", justify = "center")
        
        #This flag is to check if the loop ended with no expired products found
        hasExpired: bool = False
        if menu:
            #Loops over products in the menu and checks expiry date
            for prodName in menu:
                expDate: datetime = datetime.strptime(menu[prodName]['exp date'], '%Y-%m-%d')
                #Converting datetime object to string then back to datetime to get desired format
                todayStr: str = datetime.strftime(datetime.today(), '%Y-%m-%d')
                todaysDate: datetime = datetime.strptime(todayStr, '%Y-%m-%d')

                if expDate < todaysDate:
                    expiredTable.add_row(f"[#feffde]{prodName}[/]",f"[#daf5ff]{menu[prodName]['qty']}[/]",f"[#ccefd8]{menu[prodName]['price']} SR[/]", f"[#ffd7f0]{menu[prodName]['exp date']}")
                    hasExpired = True
            if hasExpired == False:
                expiredTable.add_row(None, "There are no expired products..", None, style="italic #fbfbe2")
            return expiredTable
        else:      
            return Text("The menu is empty.", style="italic #fbfbe2")
        
    def checkOutOfStock(self) -> Table:
        '''This method returns a Table containing all out of stock items'''

        #Retrieving menu from the json file
        menu: dict = Person.loadFromJSON(self)

        #Create table of out of stock products on the menu
        oofTable: Table = Table(title="Out of Stock Products:",title_style="bold #ffd7f0" ,title_justify="left", box=box.SIMPLE, show_footer=True, border_style="#daf5ff")
        
        #Adding columns to the table 
        oofTable.add_column("[bold #fdffc3]Product Name[/]")
        oofTable.add_column("[bold #bdeeff]Quantity[/]", justify = "center")
        oofTable.add_column("[bold #a4d5b5]Price[/]", justify = "center")
        oofTable.add_column("[bold #ffd7f0]Expiry Date[/]", justify = "center")
        
        #This flag is to check if the loop ended with no out of stock products found
        ranOut: bool = False
        if menu:
            #Loops over products in the menu and checks quantity
            for prodName in menu:
                if menu[prodName]["qty"] == 0:
                    oofTable.add_row(f"[#feffde]{prodName}[/]",f"[#daf5ff]{menu[prodName]['qty']}[/]",f"[#ccefd8]{menu[prodName]['price']} SR[/]", f"[#ffd7f0]{menu[prodName]['exp date']}")
                    ranOut = True
            if ranOut == False:
                oofTable.add_row(None, "There are no out of stock products..", None, style="italic #fbfbe2")
            return oofTable
        else:      
            return Text("The menu is empty.", style="italic #fbfbe2")
        