from User.Users import  Person
from User.WALLET import Wallet
from colorama import Fore
from CustomErrors.MyExceptions import IDError
from datetime import datetime
import re

class Resident(Person):
    def __init__(self, user_name: str, email: str, password: str, phone_number: str,id:str) -> None:
        super().__init__(user_name, email, password, phone_number)
        self.__set_id(id)
        self.wallet=Wallet()
        self.violations=[]
        self.installment_tracker={}

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
            "Status":False 
        }
        self.violations.append(Violation)

    def is_valid_violation_id(self,violation_id:int)->bool:
        if self.violations:
            for violation in self.violations:
                if violation_id==violation['Violation_id']:
                    return True
                else:
                    return False
        else:
             print(f"there is no fines! for {self.get_id()}")


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
        amount:float=0
        for violation in self.violations:
            amount +=violation['Amount']
        print(f'The amount that you want to pay is {amount}SAR')
        if amount>=4000:
            choice = input("This violation is over 3000 SAR. Would you like to pay in installments? (yes/no): ").lower()
            if choice=='yes':
                self.installment_plan(amount)
                return
        if self.wallet.get_balance()>=amount:
            self.wallet.pay(amount)
            for violation in self.violations:
                violation['Status'] = True  # Mark all violations as paid
                print("All violations have been paid.")

        else:
            print("insufficient amount to make the payment ")
    
    def installment_plan(self,amount:float):
        print("how many months do you want to pay your violations:\n4-months\n6-months")
        choice=input("Choose 4 or 6: ")
        if choice =='4':
            months=4
        elif choice=='6':
            months=6
        else:
            print("invalid choice!")
        monthly_payment=amount/months
        if self.wallet.get_balance()>=monthly_payment:
            violation_ids = [violation['Violation_id'] for violation in self.violations if not violation['Status']]
            self.installment_tracker={
                'total_amount':amount,
                'months_remaining':months,
                'monthly_payment':monthly_payment,
                'total_paid':0,
                'violations_id':violation_ids
                }
            print(f"You have choosen the {months} plan now you will pay {monthly_payment:.2f} see you next month!")
            self.make_installment_payment()
        else:
            print("insufficient amount to make the payment ")
    
    def make_installment_payment(self):
        if self.installment_tracker:
            monthly_payment=self.installment_tracker['monthly_payment']
            if self.wallet.get_balance()>=monthly_payment:
                self.wallet.pay(monthly_payment)
                print(f"paid {monthly_payment:.2f} for this month.")
                self.installment_tracker['total_amount'] -=monthly_payment
                self.installment_tracker['months_remaining']-=1
                self.installment_tracker['total_paid']+=monthly_payment

                if self.installment_tracker['total_amount'] <= 0 or self.installment_tracker['months_remaining'] <= 0:
                    print("All installments have been paid off!") 
                # Mark all violations as paid
                    for violation in self.violations:
                        if  violation['Violation_id'] in self.installment_tracker['violations_id']:
                            violation['Status'] = True
                            print(f"Violation {violation['Violation_id']} is now marked as paid.")
                else:
                    print(f"{self.installment_tracker['months_remaining']} months remaining. "
                    f"Balance left: {self.installment_tracker['total_amount']:.2f} SAR.")
            else:
                print("insufficient amount to make the payment ")
        else:
            print("you do not have an installment plan to pay !")

    def pay_specfic_violation(self,violation_id:int):
        if violation_id in self.violations['Violation_id'] and violation_id not in self.installment_tracker['violations_id']:
            for violation in self.violations:
                if violation['Violation_id']==violation_id:
                    amount=violation['Amount']
                    if self.wallet.get_balance()>=amount:
                        self.wallet.pay(amount)
                        violation['status']=True
                        print(f"Violation {violation['Violation_id']} is now marked as paid.")
                        break
                    else:
                        print("insufficient amount to make the payment ")
    
    def make_discount(self,violation_ministry:str,persentige:float):
        if self.violations:                    
            for violation in self.violations:
                if violation_ministry==violation['Ministry']:
                    previous_amount=violation['Amount']
                    new_amount=previous_amount*(persentige/100)
                    violation['Amount'] =new_amount
            print(f'{Fore.CYAN}All violations from {violation_ministry} hass been disocunted by {persentige}% {Fore.RESET}')           
        else:
            print(f"there is no fines! for {self.get_id()}")
        


        