from ShoppingCart import ShoppingCart

class Customer:
    def __init__(self, name:str, username:str, password:str):
        self.name = name
        self.username = username
        self.password = password
        self.cart = ShoppingCart()
        
    def Reset_ShoppingCart(self):
        self.cart = ShoppingCart()
        
        
    