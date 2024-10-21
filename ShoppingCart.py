from Products import Products

class ShoppingCart:
    def __init__(self):
        self.cart = {}
        
    def add_to_cart(self, product:Products, quantity:int):
        if quantity <= product.quantity:
            self.cart[product.product_id] = [product, quantity]
            product.quantity -= quantity
            return True
        
        return False
        
    def display(self):
        if self.is_empty():
            return False
        else:
            for i, product in enumerate(self.cart, start=1):
                print(f'{i}. Name: {product[0].name}, Price: {product[0].price}, Quantity: {product[1]}')
                
            return True
    
    def delete_from_cart(self, product:Products, unWantedQuantity:int, all=False):
        if product:
            newQuantity = self.cart[product.product_id][1] - unWantedQuantity
            if all or newQuantity <= 0:
                del self.cart[product.product_id]
            else:
                self.cart[product.product_id][1] -= unWantedQuantity
            return True
        
        return False
    
    