from ShoppingCart import ShoppingCart

class Customer:
    def __init__(self, name:str, username:str, password:str):
        self.name = name
        self.__username = username
        self.__password = password
        self.cart = ShoppingCart()
        
    def get_password(self):
        return self.__password
    
    def get_username(self):
        return self.__username
    
    def Reset_ShoppingCart(self):
        self.cart = ShoppingCart()
        
    def checkout(self):
        pass
        
    