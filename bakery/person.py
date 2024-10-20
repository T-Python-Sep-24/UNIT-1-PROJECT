from bakery.order import OrderedProduct, Order
import pickle, json


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
    
    def listAllProducts(self):
        '''
        This method retrieves the list of all products from json file and returns a formatted string containing the menu
        '''
        menuFormatted: str = ""
        menu: dict = self.__loadFromJSON()

        if menu:
            #Format and store the menu 
            for prod in menu:
                menuFormatted += f"⟡ {prod}.\tQuantity: {menu[prod]['qty']}\tPrice per piece: {menu[prod]['qty']}SR.\n"
            return menuFormatted
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
        self.__loadFromFile()
        return self.__orderHistory
    
    def getRole(self):
        '''
        Getter for role attribute
        '''
        return self.__role
    
    def saveToFile(self):
        '''
        Call this when you want to store your customer data in a pickle file
        '''
        with open("bakeryData/customerDetails.pkl", "wb") as file:
            #Store the customer in a pickle file
            pickle.dump(self, file)

    def __loadFromFile(self) -> list[Order]: 
        '''
        Call this method whenever you want to load from a pickle file and make neccessary checks
        '''
        try:
            with open("bakeryData/customerDetails.pkl", "rb") as file:
                #Get the information from the json file by using .load() function
                self.__orderHistory = pickle.load(file)
        except FileNotFoundError:
            print("File doesn't Exist.")
        except Exception as e:
            print(f"An error occured, {e.__class__}")
    

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
        while choice != '4':
            try:
                if choice == '1':
                    newName: str = input("Enter the new name: ")
                    return self.updateProductName(prodName, newName)
                elif choice == '2':
                    newQty: int = int(input("Enter the new quantity: "))
                    if not isinstance(newQty, int):
                        raise ValueError
                    return self.updateProductQty(prodName, newQty)
                elif choice == '3':
                    newPrice: float = float(input("Enter the new price: "))
                    if not isinstance(newPrice, float):
                        raise ValueError
                    return self.updateProductPrice(prodName, newPrice)
                else:
                    print("Invalid choice, try again..")
            except ValueError:
                print("Please enter numbers only.")
