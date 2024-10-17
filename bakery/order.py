
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
        total = 0.0
        for prod in self.__orderedProducts:
            total += prod.getPrice()
        
        return total
    
    def storeCartData(self):
        '''
        This method stores cart data in a pickle file to retrieve when needed
        '''
        with open("bakeryData/cartDetails.pkl", "wb") as file:
            #Store the customer in a pickle file
            pickle.dump(self, file)
        

    def clearCart(self):
        '''
        This method clears all products from the cart
        '''
        #Open the cart in write mode to clear its contents
        open("bakeryData/cartDetails.pkl", "w").close()
            