from User.Users import  Person
import re
from colorama import Fore
from CustomErrors.MyExceptions import IDError
class Resident(Person):
    def __init__(self, user_name: str, email: str, password: str, phone_number: str,id:str) -> None:
        super().__init__(user_name, email, password, phone_number)
        self.__set_id(id)
        self.viloations=[]
    def __set_id(self,id:str)->None:
        pattern=r'\d{10}$'
        if re.match(pattern,id):
            self.__id=id
        else:
            raise IDError(Fore.RED+"ID must be didgits only and 10 digits only !")
    def get_id(self)->str:
        return self.__id
    
    


    def add_vilation(self,viloation_id,viloation_type,amount)->None:
        Violation={
            "Violation_id":viloation_id,
            "Violation_type":viloation_type,
            "Amount":amount,
            "Status":False
        }
        self.viloations.append(Violation)
