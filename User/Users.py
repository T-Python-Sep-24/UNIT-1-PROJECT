import re
from CustomErrors.MyExceptions import PasswordError,EmailError,PhoneNumberError
from colorama import Fore
class Person:
    def __init__(self,user_name:str,email:str,password:str,phone_number:str) -> None:
        self.__set_user_name(user_name)
        self.__set_email(email)
        self.__set_password(password)
        self.__set_phone_number(phone_number)

    def __set_user_name(self,name:str)->None:
            self.__user_name=name        

    def __set_email(self,email:str)->None:
        pattern=r'^[\w\.-]+@[\w\.-]+.\w+$'
        if re.match(pattern,email):
            self.__email=email
        else:
            raise EmailError(Fore.RED+f'''
                  Email is incorrect please provide an email that contain one of theese domains:
                  (@gmail.com, @hotmail.com,@outlook.com)
                  You wrote: {email}''')
            

    def __set_password(self,password:str)->None:
        pattern=r'^(?=.*[A-Z])(?=.*[!@#$%^&*()_+{}\[\]:;<>,.?~\\\/\-])(?=.*\d).{7,}$'
        if re.match(pattern,password):
            self.__password=password
        else:
            raise PasswordError(Fore.RED+'''
                                Password should be:
                                .at leaast 7 characters long
                                .at least 1 capital letter
                                .at least 1 special character
                                .at least 1 digit
                                ''')

    def __set_phone_number(self,phone_number:str)->None:
        pattern=r'^05\d{8}$'
        if re.match(pattern,phone_number):
            self.__phone_number=phone_number
        else:
            raise PhoneNumberError(Fore.RED+'''
                                   Phone number should only :
                                   .stars with 05
                                   .has 10 numbers
                                   .only contains digit
                                   ''')
        

    def get_name(self)->str:
        return self.__user_name
    
    def get_email(self)->str:
        return self.__email
    
    def get_password(self)->str:
        return self.__password
    
    def get_phone_number(self)->int:
        return self.__phone_number
