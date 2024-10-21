from datetime import datetime
import pickle, json

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

class Cart:

    def __init__(self):
        self.__orderedProducts: list[OrderedProduct] = []
        
    def addItem(self, productName, qty):
        '''A method that adds a product with a name and quantity to the cart'''
        menu: dict = self.__loadFromJSON()
        price: float = 0.0
        if menu:
            if productName in menu:
                price = menu[productName]["price"] * qty

        product: OrderedProduct = OrderedProduct(productName, qty, price)
        self.decreaseAvailableProductsQty(productName, qty)
        self.__orderedProducts.append(product)
        self.saveCartData()

    def removeItem(self, prodName):
        '''A method that removes a product with a specific name from the cart'''
        for prod in self.__orderedProducts:
            if prod.getName() == prodName:
                #Return the canclled product to the menu of available products
                self.returnProductsToMenu(prodName, prod.getQty())
                #Remove the product from the list of ordered products 
                self.__orderedProducts.remove(prod)
                #Save modified cart details
                self.saveCartData()
                break

    def updateItemQty(self, prodName: str, qty: int):
        '''A method that updates the quantity of a product in the cart'''
        for prod in self.__orderedProducts:
            if prod.getName() == prodName:
                #First: return the products that are in the cart back to the menu
                self.returnProductsToMenu(prodName, prod.getQty())
                #Second: decrease the amount of available products by the new quantity
                self.decreaseAvailableProductsQty(prodName, qty)
                #Set the new quantity value
                prod.setQty(qty)
                #Save modified cart details
                self.saveCartData()
                break

    def returnProductsToMenu(self, prodName: str, qty: int) -> str:
        '''This method returns the cancelled products to the menu of available products'''
        menu: dict = self.__loadFromJSON()
        
        if menu:
            #Check that the product is on the menu
            if prodName in menu:
                #Modify the quantity of the product
                menu[prodName]["qty"] += qty
                with open("bakeryData/menu.json", "w", encoding="utf-8") as file:
                    #Store the modified menu back to the json file 
                    json.dump(menu, file, indent = 4)
                return f"Quantity of '{prodName}' was updated successfully."
            else:
                return f"Product '{prodName}' isn't on the menu."
        else: 
            return "Your menu is empty."

    def decreaseAvailableProductsQty(self, prodName: str, qty: int) -> str:
        '''This method updates a product's quantity then saves the modified menu to the json file'''
        menu: dict = self.__loadFromJSON()
        
        if menu:
            #Check that the product is on the menu
            if prodName in menu:
                #Modify the quantity of the product
                menu[prodName]["qty"] -= qty
                with open("bakeryData/menu.json", "w", encoding="utf-8") as file:
                    #Store the modified menu back to the json file 
                    json.dump(menu, file, indent = 4)
                return f"Quantity of '{prodName}' was updated successfully."
            else:
                return f"Product '{prodName}' isn't on the menu."
        else: 
            return "Your menu is empty."
    
    def calculateTotal(self) -> float:
        '''A method that calculate and return the total price of the products in the cart'''
        total: float = 0.0
        for prod in self.__orderedProducts:
            total += prod.getPrice()
        
        return total
    
    def viewCart(self) -> str:
        '''This method displays cart contents when called'''  
        products: str = ""  
        try:
            with open("bakeryData/cartDetails.pkl", "rb") as file:
                #Get the information from the json file by using .load() function
                self.__orderedProducts = pickle.load(file)
            for prod in self.__orderedProducts:
                products += f"• {prod.getName()}. Quantity: {prod.getQty()} pieces. Price: {prod.getPrice()} SR.\n"
            return f"{products}Total price: {self.calculateTotal()} SR."
        
        except FileNotFoundError:
            return "File doesn't Exist."
        except EOFError:
            return "Your cart is empty"
        except Exception as e:
            return f"An error occured, {e.__class__}"
        
    def saveCartData(self):
        '''
        This method stores cart data in a pickle file to retrieve when needed
        '''
        with open("bakeryData/cartDetails.pkl", "wb") as file:
            #Store the customer in a pickle file
            pickle.dump(self.__orderedProducts, file)

    def clearCart(self):
        '''This method clears all products from the cart and returns the products to the menu'''
        menu: dict = self.__loadFromJSON()
        for prod in self.__orderedProducts:
            #Find the product that hase the same name as the one in the cart
            if prod.getName() in menu:
                #Return the quantity back to how it was before products were added to cart
                menu[prod.getName()]["qty"] += prod.getQty()

        with open("bakeryData/menu.json", "w", encoding="utf-8") as file:
                #Store the modified menu back to the json file 
                json.dump(menu, file, indent = 4)
        #Open the cart in write mode to clear its contents
        open("bakeryData/cartDetails.pkl", "wb").close()

    def __loadFromJSON(self) -> dict: 
        '''Call this method whenever you want to load from a json file and make neccessary checks'''
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