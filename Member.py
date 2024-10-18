from Player import Player
class Member(Player):
    def __init__(self, style: str,name:str,id:str) -> None:
        super().__init__(style)
        self.__name=self.set_member_name(name)
        self.__id=self.set_member_id(id)

    def set_member_name(self,name):
        self.__name=name

    def get_member_name(self):
        return self.__name 
    
    def set_member_id(self,id):
        self.__id=id

    def get_member_id(self):
        return self.__id   