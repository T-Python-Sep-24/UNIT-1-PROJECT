
class OrderedProduct:

    def __init__(self, productName: str, qty: int, price: float):
        self.__productName = productName
        self.__qty = qty
        self.__price = price

    
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
