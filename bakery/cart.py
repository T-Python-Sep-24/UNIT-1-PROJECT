from bakery.order import OrderedProduct
import json

#Using rich library to style output on terminal
from rich.table import Table
from rich import box
from rich.text import Text

class Cart:

    def __init__(self):
        self.__orderedProducts: list[OrderedProduct] = []
        
    def getOrderedProducts(self):
        '''Getter for ordered products attribute'''
        return self.__orderedProducts

    def addToCart(self, productName, qty):
        '''A method that adds a product with a name and quantity to the cart'''
        menu: dict = self.__loadFromJSON()
        price: float = 0.0
        if menu:
            if productName in menu:
                #If the availble quantity is enough procceed
                if (menu[productName]["qty"] - qty) > 0:
                    price = menu[productName]["price"]
                    product: OrderedProduct = OrderedProduct(productName, qty, price)
                    self.decreaseAvailableProductsQty(productName, qty)
                    self.__orderedProducts.append(product)
                else:
                    return Text("Available quantity is less than the ordered quantity.", style="red")
            else:
                return Text(f"Product '{productName}' isn't on the menu.", style="red")

    def removeFromCart(self, prodName):
        '''A method that removes a product with a specific name from the cart'''
        for prod in self.__orderedProducts:
            if prod.getName() == prodName:
                #Return the canclled product to the menu of available products
                self.returnProductsToMenu(prodName, prod.getQty())
                #Remove the product from the list of ordered products 
                self.__orderedProducts.remove(prod)
                return True
        return False

    def updateCart(self, prodName: str, qty: int) -> bool:
        '''A method that updates the quantity of a product in the cart'''
        for prod in self.__orderedProducts:
            if prod.getName() == prodName:
                #First: return the products that are in the cart back to the menu
                self.returnProductsToMenu(prodName, prod.getQty())
                #Second: decrease the amount of available products by the new quantity
                self.decreaseAvailableProductsQty(prodName, qty)
                #Set the new quantity value
                prod.setQty(qty)
                return True
        return False

    def returnProductsToMenu(self, prodName: str, qty: int):
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

    def decreaseAvailableProductsQty(self, prodName: str, qty: int):
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
    
    def calculateTotal(self) -> float:
        '''A method that calculate and return the total price of the products in the cart'''
        total: float = 0.0
        for prod in self.__orderedProducts:
            total += prod.getPrice()
        
        return total
    
    def viewCart(self) -> Table:
        '''This method displays cart contents when called'''  

        #Creating a table object to display menu
        cartTable: Table = Table(title = "Cart Details", title_style="italic bold #fdffc3", border_style="#dadada",expand=False, box=box.SIMPLE_HEAVY)

        #Adding columns to the table
        cartTable.add_column("[bold #fdffc3]Product Name[/]")
        cartTable.add_column("[bold #bdeeff]Quantity[/]", justify = "center")
        cartTable.add_column("[bold #a4d5b5]Price[/]", justify = "center")

        if self.__orderedProducts != []:
            #Add a row for each product in the cart
            for prod in self.__orderedProducts:
                cartTable.add_row(f"[#fdffc3]{prod.getName()}[/]", f"[#bdeeff]{prod.getQty()}[/]", f"[#a4d5b5]{prod.getPrice()} SR[/]")
            cartTable.add_section()
            cartTable.add_row(None, None, f"Total price: {self.calculateTotal()} SR", style="white")
            return cartTable
        else:
            return Text("Your cart is empty..", style="italic #fdffc3")

    def clearCart(self) -> bool:
        '''This method clears all products from the cart and returns the products to the menu of available products'''
        if self.__orderedProducts != []:
            for prod in self.__orderedProducts:
                self.returnProductsToMenu(prod.getName(), prod.getQty())
            #Empty the list of ordered products
            self.__orderedProducts = []
            return True
        #If the cart is already empty return false
        return False

    def __loadFromJSON(self) -> dict: 
        '''Call this method whenever you want to load from a json file and make neccessary checks'''
        menu: dict = {}
        try:
            with open("bakeryData/menu.json", "r", encoding="utf-8") as file:
                #Get the information from the json file by using .load() function
                menu = json.load(file)
        except FileNotFoundError:
            print(Text("File doesn't Exist.", style="red"))
        except Exception as e:
            print(Text(f"An error occured, {e.__class__}", style="red"))
        finally:
            return menu