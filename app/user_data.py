# todo user basic data for less inputs
import os
import random
import re
import time

import requests
import dotenv
from tqdm import tqdm
dotenv.load_dotenv()

class User:

    fileName = '../user_data_files/user.json'
    __name: str = ""
    # __id = ""
    __email: str = ""
    __age: int = 0
    __height: float = 0
    __weight: float = 0
    __gender: str = ""

    def __init__(self):

        fileName = '../user_data_files/user.json'
        __name: str = ""
        __email: str = ""
        __age: int = 0
        __height: float = 0
        __weight: float = 0
        __gender: str = ""

    def set_name(self, name: str):
        self.__name = name

    def set_email(self, email: str):

        if self.validate_email(email):
            self.__email = email
        else:
            print("Email is not valid")

    def set_age(self, age: int):
        self.__age = age

    def set_height(self, height: float):
        self.__height = height

    def set_weight(self, weight: float):
        self.__weight = weight

    def set_gender(self, gender: str):
        self.__gender = gender

    def get_name(self) -> str:
        return self.__name

    def get_email(self) -> str:
        return self.__email

    def get_age(self) -> int:
        return self.__age

    def get_height(self) -> float:
        return self.__height

    def get_weight(self) -> float:
        return self.__weight

    def get_gender(self) -> str:
        return self.__gender

    def validate_email(self, email) -> bool:

        pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
        # self.check_email_exists(email)
        # Check if the email matches the Gmail pattern and verified by hunter.io api
        if re.match(pattern, email):

            return True
        else:
            return False

    # def check_email_exists(sef, email):
    #     api_key = os.getenv('emailCheckerAPI')
    #
    #     with tqdm(total=100, desc="Validating Email", ncols=100) as checker_par:
    #         for i in range(90):
    #             time.sleep(0.01)
    #             checker_par.update(1)
    #
    #         response = requests.get(f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={api_key}")
    #         checker_par.update(10)
    #
    #     print(response)
    #     validate = response['data']['status']
    #     print(validate)

        # return response.json()



