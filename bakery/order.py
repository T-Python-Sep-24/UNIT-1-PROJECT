
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

from datetime import datetime

class Order:

    def __init__(self, orderedProducts: list[OrderedProduct]):
        self.__date = datetime.today()
        self.__orderedProducts = orderedProducts

    def orderInfo(self) -> str:
        '''
        This method returns the details of the order
        '''
        products: str = ""
        for prod in self.__orderedProducts:
            total: float = prod.getQty() * prod.getPrice()
            products += f"Product name: {prod.getName()}. Quantity: {prod.getQty()}. Price: {total}\n"
        return f"{products} Ordered on: {self.__date}"
        


import pickle

class Cart:

    def __init__(self):
        self.__orderedProducts: list[OrderedProduct] = []
        
    def addItem(self, prodName, qty):
        '''
        A method that adds a product with a name and quantity to the cart
        '''
        product: OrderedProduct = OrderedProduct(prodName, qty)
        self.__orderedProducts.append(product)

    def removeItem(self, prodName):
        '''
        A method that removes a product with a specific name from the cart
        '''
        for prod in self.__orderedProducts:
            if prod.getName() == prodName:
                self.__orderedProducts.remove(prod)
                break
    
    def calculateTotal(self):
        '''
        Calculate and return the total price of the products in the cart
        '''
        total: float = 0.0
        for prod in self.__orderedProducts:
            total += prod.getPrice()
        
        return total
    
    def saveCartData(self):
        '''
        This method stores cart data in a pickle file to retrieve when needed
        '''
        with open("bakeryData/cartDetails.pkl", "wb") as file:
            #Store the customer in a pickle file
            pickle.dump(self.__orderedProducts, file)
    
    def viewCart(self):
        '''
        This method displays cart contents when called
        '''    
        try:
            with open("bakeryData/customerDetails.pkl", "rb") as file:
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

    def clearCart(self):
        '''
        This method clears all products from the cart
        '''
        #Open the cart in write mode to clear its contents
        open("bakeryData/cartDetails.pkl", "wb").close()
            