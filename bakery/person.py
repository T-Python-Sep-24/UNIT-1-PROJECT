from bakery.order import OrderedProduct
import pickle, json


class Person:

    def __init__(self, name: str, age: int, gender: str, phone: str) -> None:
        self.__name = name
        self.__age = age 
        self.__gender = gender
        self.__phone = phone

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
    
    
class Customer(Person):

    def __init__(self, name: str, age: int, gender: str, phone: str):
        super().__init__(name, age, gender, phone)
        self.__orderHistory: list[OrderedProduct] = []

    def setOrderHistory(self, orderHistory: list[OrderedProduct]):
        '''
        setter for orderHistory attribute
        '''
        self.__orderHistory = orderHistory

    def getOrderHistory(self,) -> list[OrderedProduct]:
        '''
        Getter for orderHistory attribute
        '''
        return self.__orderHistory
    
    def saveToFile(self):
        '''
        Call this when you want to store your customer data in a pickle file
        '''
        with open("../bakeryData/customerDetails.pkl", "wb") as file:
            #Store the customer in a pickle file
            pickle.dump(self, file)
    

class Employee(Person):

    def __init__(self, name: str, age: int, gender: str, phone: str):
        super().__init__(name, age, gender, phone)

    def addProduct(self, prodName: str, qty: int, price: float):
        '''
        This method adds a product to a json file containing all products
        '''
        #Use the method below to get the menu from the json file
        menu: dict = self.loadFromJSON()

        menu[prodName]= {
            'qty': qty,
            'price': price
        }
        with open("../bakeryData/menu.json", "w", encoding="utf-8") as file:
            #Store the modified menu in a json file 
            json.dump(menu, file, indent = 4)
    
    def removeProduct(self, prodName: str) -> str:
        '''
        This method removes a product from the menu then saves the modified menu to the json file
        '''
        menu: dict = self.loadFromJSON()
        
        if menu:
            #Check if the product is on the menu
            if prodName in menu:
                del menu[prodName]
                with open("../bakeryData/menu.json", "w", encoding="utf-8") as file:
                    #Store the modified menu back to the json file 
                    json.dump(menu, file, indent = 4)
                return f"Product '{prodName}' was deleted successfully."
            else: 
                return f"Product '{prodName}' isn't on the menu."
        else: 
            return "Your menu is empty."

    def updateProductQty(self, prodName: str, qty: int):
        '''
        This method updates a product's quantity then saves the modified menu to the json file
        '''
        menu: dict = self.loadFromJSON()
        
        if menu:
            #Check that the product is on the menu
            if prodName in menu:
                #Modify the quantity of the product
                menu[prodName]["qty"] = qty
                with open("../bakeryData/menu.json", "w", encoding="utf-8") as file:
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
        menu: dict = self.loadFromJSON()
        
        if menu:
            #Check that the product is on the menu
            if prodName in menu:
                #Update the price of the product
                menu[prodName]["price"] = price
                with open("../bakeryData/menu.json", "w", encoding="utf-8") as file:
                    #Store the modified menu back to the json file 
                    json.dump(menu, file, indent = 4)
                return f"Price of '{prodName}' was updated successfully."
            else:
                return f"Product '{prodName}' isn't on the menu."
        else: 
            return "Your menu is empty."

    def listAllProducts(self):
        '''
        This method retrieves the list of all products from json file and returns a formatted string containing the menu
        '''
        menuFormatted: str = ""
        menu: dict = self.loadFromJSON()

        if menu:
            #Format and store the menu 
            for prod in menu:
                menuFormatted += f"⟡ {prod} Quantity: {menu[prod]['qty']} Price per piece: {menu[prod]['qty']}SR.\n"
            return menuFormatted
        else: 
            return "Your menu is empty."
        
    def loadFromJSON(self) -> dict: 
        '''
        Call this method whenever you want to load from a json file and make neccessary checks
        '''
        menu: dict = {}
        try:
            with open("../bakeryData/menu.json", "r", encoding="utf-8") as file:
                #Get the information from the json file by using .load() function
                menu = json.load(file)
        except FileNotFoundError:
            print("File doesn't Exist.")
        except Exception as e:
            print(f"An error occured, {e.__class__}")
        finally:
            return menu
        
