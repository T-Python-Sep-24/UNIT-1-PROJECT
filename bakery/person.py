from bakery.order import OrderedProduct

class Person:

    def __init__(self, name: str, age: int, gender: str, id: str) -> None:
        self.__name = name
        self.__age = age 
        self.__gender = gender
        self.__id = id

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
    
    def getID(self) -> str:
        '''
        Getter for ID attribute
        '''
        return self.__id
    
    
class Customer(Person):

    def __init__(self, name: str, age: int, gender: str, id: str) -> None:
        super().__init__(name, age, gender, id)
        self.__orderHistory: list[OrderedProduct] = []

    def setOrderHistory(self, orderHistory: list[OrderedProduct]):
        '''
        setter for orderHistory attribute
        '''
        self.__orderHistory = orderHistory

    def getOrderHistory(self,) -> list[OrderedProduct]:
        '''
        Getter for orderHistory attribute
        '''
        return self.__orderHistory
    

class Employee(Person):

    def __init__(self, name: str, age: int, gender: str, id: str) -> None:
        super().__init__(name, age, gender, id)
        self.__id = 'e' + id

    def addProduct(self, prodName: str, qty: int, price: float):
        '''
        This method adds a product to a pickle file containing all products
        '''
        pass
    
    def removeProduct(self, prodName: str):
        '''
        This method removes a product from the system then updates the pickle file that contains all products
        '''
        pass

    def updateProduct(self, prodName: str):
        '''
        This method updates a product from the collection of products then updates the pickle file with the updated product list
        '''
        pass

    def listAllProducts(self):
        '''
        This method retrieves the list of all products from a pickle file
        '''
        pass
