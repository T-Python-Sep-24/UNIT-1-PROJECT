import random
from colorama import Fore
class Wallet:
    
    def __init__(self,account_balance:float=0) -> None:
        self.__set_balance(account_balance)

    def __set_balance(self,account_balance):
        if account_balance>=0:
            self.__account_balance=account_balance
        else:
            raise ValueError(" must be posotive amount")        
    

    def get_balance(self)->float:
        return self.__account_balance
    
    def deposit(self,amount:float):
        balance=self.get_balance()
        if amount>0:
            new_balance =balance+amount
            self.__set_balance(new_balance)
            print(f"{Fore.LIGHTBLUE_EX} {amount} added to balance{Fore.RESET} ")
        else:
            raise ValueError("the amount must be a float value and not negative")  

    def pay(self,amount:float):
        balance=self.get_balance()
        new_balance= balance-amount
        self.__set_balance(new_balance)
        print(f"Balance now : {self.get_balance():.2f}")
    