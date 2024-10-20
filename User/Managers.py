from User.Users import Person
from CustomErrors.MyExceptions import AuthenticationError
from colorama import Fore

class Manager(Person):
    ministry_authentications={
    123456789012:"Ministry of Human Resources and Social Development",
    12345678901:"Ministry of Interior",
    1234567890:"Ministry of Commerce",
    12345789:"Ministry of Environment, Water, and Agriculture",
    1234578:"Saudi Arabian Cybersecurity Authority (SCA)",
    1234567:"Ministry of Islamic Affairs, Dawah, and Guidance",
    123456:"Ministry of Health",
    12345:"General Authority of Zakat and Tax (GAZT)",
    1234:"Ministry of Interior (Traffic Department)"
    }
    def __init__(self, user_name: str, email: str, password: str, phone_number:str,ministry_authentication:int) -> None:
        super().__init__(user_name, email, password, phone_number)
        self.is_valid(ministry_authentication)
        self.ministry_name=self.ministry_authentications.get(ministry_authentication)
    
    def is_valid(self,authentication_number:int)->bool:
        if authentication_number in self.ministry_authentications:
            return True
        else:
            raise AuthenticationError(Fore.RED+"The number you provided is not register in any of the ministries!!")
        
    def get_ministry_name(self):
        return self.ministry_name