# todo user basic data for less inputs
import os
import random
import re
import requests
import dotenv
dotenv.load_dotenv()

class User:
    __name = ""
    __id = ""
    __email = ""
    __age = 0
    __height = 0
    __weight = 0
    __gender = ""

    def __init__(self):

        __name = ""
        __id = str(random.randint(100, 999))
        __email = ""
        __age = 0
        __height = 0
        __weight = 0
        __gender = ""

    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id

    def set_email(self, email):

        if self.validate_email(email):
            self.__email = email
        else:
            print("Email is not valid")

    def set_age(self, age):
        self.__age = age

    def set_height(self, height):
        self.__height = height

    def set_weight(self, weight):
        self.__weight = weight

    def set_gender(self, gender):
        self.__gender = gender

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_email(self):
        return self.__email

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height

    def get_weight(self):
        return self.__height

    def get_gender(self):
        return self.__gender

    def validate_email(self, email):

        pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
        email_status = self.check_email_exists(email)
        validate = email_status['data']['status']
        # Check if the email matches the Gmail pattern and verified by hunter.io api
        if re.match(pattern, email) and validate == 'valid':
            return True
        else:
            return False

    def check_email_exists(sef, email):
        api_key = os.getenv('emailCheckerAPI')
        response = requests.get(f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={api_key}")
        return response.json()



