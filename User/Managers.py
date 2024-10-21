from User.Users import Person
from CustomErrors.MyExceptions import AuthenticationError
from colorama import Fore

class Manager(Person):
    ministry_authentications={
    96399:"Ministry of Human Resources and Social Development",
    66711:"Ministry of Interior",
    87320:"Ministry of Commerce",
    85606:"Ministry of Environment, Water, and Agriculture",
    68211:"Saudi Arabian Cybersecurity Authority (SCA)",
    54675:"Ministry of Islamic Affairs, Dawah, and Guidance",
    80347:"Ministry of Health",
    57336:"General Authority of Zakat and Tax (GAZT)",
    91101:"Ministry of Interior (Traffic Department)"
    }
    def __init__(self, user_name: str, email: str, password: str, phone_number:str,ministry_authentication:int) -> None:
        super().__init__(user_name, email, password, phone_number)
        self.is_valid(ministry_authentication)
        self.authentication_number=ministry_authentication
        self.ministry_name=self.ministry_authentications.get(ministry_authentication)
    
    def get_authentication_number(self):
        return self.authentication_number
    
    def is_valid(self,authentication_number:int)->bool:
        if authentication_number in self.ministry_authentications:
            return True
        else:
            raise AuthenticationError(Fore.RED+"The number you provided is not register in any of the ministries!!")
        
    def get_ministry_name(self):
        return self.ministry_name