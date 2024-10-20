from User.Users import  Person

class Resident(Person):
    def __init__(self, user_name: str, email: str, password: str, phone_number: str,id:int) -> None:
        super().__init__(user_name, email, password, phone_number)
        self.__set_id(id)
    
    def __set_id(self,id:int)->None:
        self.__id=id
    
    def get_id(self)->int:
        return self.__id
