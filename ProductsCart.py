from Products import Products

class ProductsCart:
    def __init__(self):
        self.cart = {}
        
    def add_to_cart(self, product:Products, quantity:int):
        if quantity <= product.quantity:
            if product.product_id not in self.cart:
                self.cart[product.product_id] = {'product': product, 'quantity': quantity}
                product.quantity -= quantity
                return True
            else:
                newQuantity = self.cart[product.product_id]['quantity'] + quantity
                if newQuantity <= product.quantity:
                    self.cart[product.product_id]['quantity'] += quantity
                    product.quantity -= quantity
                    return True
        print('The quantity you want to ADD is bigger than the actual quantity in the stock')  
        return False
        
    def display(self):
        if not self.cart:
            return False
        else:
            i=1
            for key, value in self.cart.items():
                print(f'{i}. Name: {value['product'].name}, Price: {value['product'].price}, Quantity: {value['quantity']}')
                i+=1
                
            return True
    
    def delete_from_cart(self, product:Products, unWantedQuantity:int, all=False):
        if product.product_id in self.cart:
            if unWantedQuantity <= self.cart[product.product_id]['quantity']:
                newQuantity = self.cart[product.product_id]['quantity'] - unWantedQuantity
                if all or newQuantity <= 0:
                    del self.cart[product.product_id]
                else:
                    self.cart[product.product_id]['quantity'] -= unWantedQuantity
                return True
            print('The quantity you want to delete is bigger than the actual quantity you added')
        
        return False
    
    def total_cost(self):
        totalCost = 0
        for value in self.cart.values():
            totalCost += value['product'].price * value['quantity']
            
        return totalCost