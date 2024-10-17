from bakery.order import OrderedProduct
import pickle, json


class Person:

    def __init__(self, name: str, age: int, gender: str, id: str) -> None:
        self.__name = name
        self.__age = age 
        self.__gender = gender
        self.__id = id

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
    
    def getID(self) -> str:
        '''
        Getter for ID attribute
        '''
        return self.__id
    
    
class Customer(Person):

    def __init__(self, name: str, age: int, gender: str, id: str):
        super().__init__(name, age, gender, id)
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

    def __init__(self, name: str, age: int, gender: str, id: str):
        super().__init__(name, age, gender, id)
        self.__id = 'e' + id

    def getID(self) -> str:
        '''
        Override method from parent class and add 'e' before the employee id to distinguish them
        '''
        return self.__id

    def addProduct(self, prodName: str, qty: int, price: float):
        '''
        This method adds a product to a pickle file containing all products
        '''
        #Make sure the file exists to avoid errors
        try:
            with open("../bakeryData/menu.json", "r", encoding="utf-8") as file:
                #Get the information from the json file by using .load() function
                menu = json.load(file)
        except FileNotFoundError:
            return "The menu is empty."
        except Exception as e:
            return f"An error occured, {e.__class__}"
        finally:
            menu[prodName]= {
                'qty': qty,
                'price': price
            }
            with open("../bakeryData/menu.json", "w", encoding="utf-8") as file:
                #Stores the modified menu in a json file 
                json.dump(menu, file, indent = 4)
    
    def removeProduct(self, prodName: str) -> str:
        '''
        This method removes a product from the menu then updates the json file that contains all products
        '''
        try:
            with open("../bakeryData/menu.json", "r", encoding="utf-8") as file:
                #Get the information from the json file by using .load() function
                menu = json.load(file)
        except FileNotFoundError:
            return "The menu is empty."
        except Exception as e:
            return f"An error occured, {e.__class__}"
        else:
            #Check if the product is on the menu
            if prodName in menu:
                del menu[prodName]
                with open("../bakeryData/menu.json", "w", encoding="utf-8") as file:
                    #Stores the modified menu back to the json file 
                    json.dump(menu, file, indent = 4)
                return f"Product '{prodName}' was deleted successfully."
            else: 
                return f"Product '{prodName}' isn't on the menu."

    def updateProductQty(self, prodName: str, qty: int):
        '''
        This method updates a product's quantity then saves the modified menu to the json file
        '''
        try:
            with open("../bakeryData/menu.json", "r", encoding="utf-8") as file:
                #Get the information from the json file by using .load() function
                menu = json.load(file)
        except FileNotFoundError:
            return "The menu is empty."
        except Exception as e:
            return f"An error occured, {e.__class__}"
        else:
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
        
    def updateProductPrice(self, prodName: str, price: float):
        '''
        This method updates a product's price then saves the modified menu to the json file
        '''
        try:
            with open("../bakeryData/menu.json", "r", encoding="utf-8") as file:
                #Get the information from the json file by using .load() function
                menu = json.load(file)
        except FileNotFoundError:
            return "The menu is empty."
        except Exception as e:
            return f"An error occured, {e.__class__}"
        else:
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

    def listAllProducts(self):
        '''
        This method retrieves the list of all products from json file and returns a formatted string containing the menu
        '''
        menuFormatted: str = ""
        try:
            with open("../bakeryData/menu.json", "r", encoding="utf-8") as file:
                #Get the information from the json file by using .load() function
                menu = json.load(file)
        except FileNotFoundError:
            return "The menu is empty."
        except Exception as e:
            return f"An error occured, {e.__class__}"
        else:
            #Format and store the menu 
            for prod in menu:
                menuFormatted += f"⟡ {prod} Quantity: {menu[prod]['qty']} Price per piece: {menu[prod]['qty']}SR.\n"
            return menuFormatted
