from User.Users import  Person
import re
from colorama import Fore
from CustomErrors.MyExceptions import IDError
from datetime import datetime
class Resident(Person):
    def __init__(self, user_name: str, email: str, password: str, phone_number: str,id:str) -> None:
        super().__init__(user_name, email, password, phone_number)
        self.__set_id(id)
        self.violations=[]
        self.installment_tracker=[]

    def __set_id(self,id:str)->None:
        pattern=r'\d{10}$'
        if re.match(pattern,id):
            self.__id=id
        else:
            raise IDError(Fore.RED+"ID must be didgits only and 10 digits only !")
        
    def get_id(self)->str:
        return self.__id

    def add_violation(self,viloation_id:int,viloation_type:str,amount:float,ministry:str)->None:
        Violation={
            "Violation_id":viloation_id,
            "Violation_type":viloation_type,
            "Amount":amount,
            "Ministry":ministry,
            "Date":datetime.now(),
            "Status":False ,
            "Message":None,
            "Response":None   
        }
        self.violations.append(Violation)

    def display_violations(self):
        if self.violations:
            for violation in self.violations:
                status="paid"if violation['Status'] else "Pending"
                print(f'''
                    violation ID:{violation['Violation_id']}
                    Violation Type:{violation['Violation_type']}
                    price:{violation['Amount']}
                    Issued Date:{violation['Date']}
                    Department/Ministry:{violation['Ministry']}
                    Status: {status}
                    ''')                 
        else:
            print(f"there is no fines! for {self.get_id()}")

    def search_violation(self,violation_id:int):
        if self.violations:                     
            for violation in self.violations:
                if violation_id==violation['Violation_id']:
                    status="paid"if violation['Status'] else "Pending"
                    print(f'''
                    violation ID:{violation['Violation_id']}
                    Violation Type:{violation['Violation_type']}
                    price:{violation['Amount']}SAR
                    Issued Date:{violation['Date']}
                    Department/Ministry:{violation['Ministry']}
                    Status: {status}
                    ''')
                    break
            else:
                print("there is no violation with this ID")                           
        else:
            print(f"there is no fines! for {self.get_id()}")

    def search_violation_by_ministry(self,violation_ministry:str):
        if self.violations:                     
            for violation in self.violations:
                if violation_ministry==violation['Ministry']:
                    status="paid"if violation['Status'] else "Pending"
                    print(f'''
                    violation ID:{violation['Violation_id']}
                    Violation Type:{violation['Violation_type']}
                    price:{violation['Amount']}SAR
                    Issued Date:{violation['Date']}
                    Department/Ministry:{violation['Ministry']}
                    Status: {status}
                    ''')                         
        else:
            print(f"there is no fines! for {self.get_id()}")
    
    def pay_all_violations(self):
        amount=0
        for violation in self.violations:
            amount +=violation['Amount']
        print(f'The amount that you want to pay is {amount}SAR')
        if amount>=3000:
            choice = input("This violation is over 3000 SAR. Would you like to pay in installments? (yes/no): ").lower()
            if choice=='yes':
                pass
            for violation in self.violations:
                violation['Status'] = True  # Mark all violations as paid
                print("All violations have been paid.")