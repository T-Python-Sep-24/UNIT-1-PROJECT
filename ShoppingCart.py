from Products import Products

class ShoppingCart:
    def __init__(self):
        self.cart = {}
        
    def add_to_cart(self, product:Products, quntity:int):
        self.cart[product.product_id] = [product, quntity]
        
    def display(self):
        for i, product in enumerate(self.cart, start=1):
            print(f'{i}. Name: {product[0].name}, Price: {product[0].price}, Quantity: {product[1]}')
    
    def delete_from_cart(self, product:Products, updatedQuntity:int, all=False):
        if product:
            if all:
                del self.cart[product.product_id]
            else:
                self.cart[product.product_id][1] = updatedQuntity
            return True
        
        return False
    
    def checkout(self):
        pass