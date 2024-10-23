class Admin:
    def __init__(self, name, password):
        self.__name = name 
        self.__password = password  

    
    def get_name(self):
        return self.__name

    
    def verify_password(self, password):
        return self.__password == password
