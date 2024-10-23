from User.Users import  Person
from User.WALLET import Wallet
from colorama import Fore
from CustomErrors.MyExceptions import IDError
from datetime import datetime
from dateutil.relativedelta import relativedelta
import re

class Resident(Person):
    def __init__(self, user_name: str, email: str, password: str, phone_number: str,id:str) -> None:
        super().__init__(user_name, email, password, phone_number)
        self.__set_id(id)
        self.wallet=Wallet()
        self.violations=[]
        self.discounted_violations = []
        self.installment_tracker={}

    def __set_id(self,id:str)->None:
        '''
        This abstraction method to set the resident id to each resident
        Args:
            self(Resident): an object that holds the cureent resident
            id (str): the input from user that has the unique id
        Returns:
            None
        '''
        pattern=r'\d{10}$'
        if re.match(pattern,id):
            self.__id=id
        else:
            raise IDError(Fore.RED+"ID must be didgits only and 10 digits only !")
        
    def get_id(self)->str:
        '''
        The function returns the unique id for the resident
        Args:
            self(Resident): an object that holds the cureent resident
        Returns:
            a (str) id
        '''
        return self.__id

    def add_violation(self,viloation_id:int,viloation_type:str,amount:float,ministry:str)->None:
        '''
        The function adds a violation to a resident
        Args:
            self(Resident): an object that holds the cureent resident
            violation_id(int): a unique ID that represent a violation
            Violation_type(str): violation name 
            amount(float):violation amount
            ministry(str): the ministry that issued the violation
        Returns:
            None
        '''
        Violation={
            "Violation_id":viloation_id,
            "Violation_type":viloation_type,
            "Amount":amount,
            "Ministry":ministry,
            "Date":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Status":False 
        }
        self.violations.append(Violation)



    def display_violations(self)->None:
        '''
        The function displays every violation for the resident
        Args:
            self(Resident):an object that holds the cureent resident
        Returns:
            None
        '''
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

    def search_violation(self,violation_id:int)->None:
        '''
        The function show the spesfic violation that the user wants using violation ID
        Args:
            self(Resident):an object that holds the cureent resident
            violation_id(int): a unique Id for a violation
        Returns:
            None
        '''
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

    def search_violation_by_ministry(self,violation_ministry:str)->None:
        '''
        The function displays only the violations with the needed violation_ministry
        Args:
            self(Resident):an object that holds the cureent resident
            violation_ministry(str):The ministry to get it's violations
        Returns:
            None
        '''
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
    
    def pay_all_violations(self)->None:
        '''
        The function pays the violations for the resident
        Args:
            self(resident):an object that holds the cureent resident
        Returns:
            None

        '''
        if self.violations:
            if not self.installment_tracker:
                amount:float=0
                for violation in self.violations:
                    if not violation['Status']:
                        amount +=violation['Amount']
                if amount>=4000:
                    choice = input("This violation is over 4000 SAR. Would you like to pay in installments? (yes/no): ").lower()
                    if choice=='yes':
                        self.installment_plan(amount)
                        return
            
            installment_violation_ids = self.installment_tracker.get('violations_id', [])
            violations_to_pay = [violation for violation in self.violations if violation['Violation_id'] not in installment_violation_ids and not violation['Status']]
            if violations_to_pay:
                amount: float = sum(violation['Amount'] for violation in violations_to_pay)
                print(Fore.BLUE+f'The amount that you want to pay is {amount}SAR'+Fore.RESET)
                if self.wallet.get_balance()>=amount:
                    self.wallet.pay(amount)
                    for violation in violations_to_pay:
                        violation['Status'] = True  # Mark all violations as paid
                        print("All violations have been paid.")
                else:
                    print("insufficient amount to make the payment ")
            else:
                print(Fore.YELLOW +"There is no violations to pay"+Fore.RESET)
        else:
                print(f"there is no fines! for {self.get_id()}")
    
    def installment_plan(self,amount:float)->None:
        '''
        The functions allow the user to pay in installments
        Args:
            self(resident):an object that holds the cureent resident
            amount(float):the total amount of the violations 
        Returns:
            None
        '''
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
            today = datetime.now()
            self.installment_tracker={
                'total_amount':amount,
                'months_remaining':months,
                'monthly_payment':monthly_payment,
                'next_month_payment':today,
                'total_paid':0,
                'violations_id':violation_ids
                }
            print(f"You have choosen the {months} plan now you will pay {monthly_payment:.2f} see you next month at {today + relativedelta(months=1)}")
            self.make_installment_payment()
        else:
            print("insufficient amount to make the payment ")         
    
    def make_installment_payment(self)->None:
        '''
        The function allow the user to pay the remaining payment of the installments
        Args:
            self(resident):an object that holds the cureent resident
        Returns:
            None
        '''
        if self.installment_tracker:
            monthly_payment=self.installment_tracker['monthly_payment']
            if self.wallet.get_balance()>=monthly_payment:
                self.wallet.pay(monthly_payment)
                print(f"paid {monthly_payment:.2f} for this month.")
                self.installment_tracker['total_amount'] -=monthly_payment
                self.installment_tracker['months_remaining']-=1
                self.installment_tracker['next_month_payment'] +=relativedelta(months=1)
                self.installment_tracker['total_paid']+=monthly_payment
                if self.installment_tracker['total_amount'] <= 0 or self.installment_tracker['months_remaining'] <= 0:
                    print(Fore.GREEN+"All installments have been paid off!"+Fore.RESET)
                    for violation in self.violations:
                        if  violation['Violation_id'] in self.installment_tracker['violations_id']:
                            violation['Status'] = True
                            print(Fore.LIGHTCYAN_EX+f"Violation {violation['Violation_id']} is now marked as paid."+Fore.RESET)
                    self.installment_tracker.clear()
                   
                else:
                    print(f"{self.installment_tracker['months_remaining']} months remaining. "
                    f"amount left: {self.installment_tracker['total_amount']:.2f} SAR.")
            else:
                print("insufficient amount to make the payment ")
        else:
            print("you do not have an installment plan to pay !")

    def display_installment_details(self)->None:
        '''
        The function displays the installment plan and how much left in it 
        Args:
            self(Resident):an object that holds the cureent resident
        Returns:
            None
        '''
        if self.installment_tracker:
            print(f"""Amount left: {self.installment_tracker['total_amount']:.2f} 
                    Months Remaining: {self.installment_tracker['months_remaining']}
                    Next pyment Date: {self.installment_tracker['next_month_payment']}
                    Next Month payment: {self.installment_tracker['monthly_payment']:.2f}
                    Violations_IDs: {self.installment_tracker['violations_id']}
                    total paid: {self.installment_tracker['total_paid']:.2f}""")
        else:
            print(Fore.YELLOW+"You don't have an installment plan!"+Fore.RESET)

    def pay_specfic_violation(self,violation_id:int)->None:
        '''
        The function allow the user to pay for a specfic violation
        Args:
            self(Resident):an object that holds the cureent resident
            violation_id(int):the id for the violation that the user wants to pay
        Returns:
            None 
        '''
        if self.violations:
                for violation in self.violations:
                    if violation['Violation_id']==violation_id:
                        if violation_id in self.installment_tracker.get('violations_id', []):
                            print(Fore.YELLOW+f"Violation {violation_id} is part of an installment plan and cannot be paid directly."+Fore.RESET)
                            return
                        amount=violation['Amount']
                        if self.wallet.get_balance()>=amount:
                            self.wallet.pay(amount)
                            violation['Status']=True
                            print(f"Violation {violation['Violation_id']} is now marked as paid.")
                            break
                        else:
                            print("insufficient amount to make the payment ")
                    else:
                        print("there is no violation with this id ")
        else:
            print(f"there is no violatiobn! for {self.get_id()}")
            
    
    def make_discount(self,violation_ministry:str,percentage:float)->None:
        '''
        The function make a discount to the user/users based on the manager that is using the program
        Args:
            self(Resident):an object that holds the cureent resident
            violation_ministry(str): this to ensure that the discount of violations is only for the manager ministry
            percentage(float):the percentage of the discount to the violations 
        Returns:
            None
             
        '''
        if self.violations:                    
            for violation in self.violations:
                if violation['Ministry'] == violation_ministry and violation['Violation_id'] not in self.discounted_violations and not violation['Status'] and violation['Violation_id'] not in self.installment_tracker.get('violations_id', []):
                    previous_amount=violation['Amount']
                    new_amount=previous_amount*(percentage/100)
                    violation['Amount'] =new_amount
                    self.discounted_violations.append(violation['Violation_id'])
                    print(f'{Fore.CYAN}violation: {violation['Violation_id']} from {violation_ministry}to Resident {self.get_id()} has been disocunted by {percentage}% {Fore.RESET}')   
                else:
                    if violation['Violation_id'] in self.discounted_violations:
                        print(Fore.YELLOW+f"A discount has already been applied to violation {violation['Violation_id']} by {violation_ministry} to Resident:  {self.get_id()}"+Fore.RESET)
                    elif violation['Violation_id'] in self.installment_tracker.get('violations_id', []):
                        print(Fore.YELLOW+f"The violation with the id of {violation['Violation_id']} in an installment plan "+Fore.RESET)      
        else:
            print(f"there is no fines! for Resident {self.get_id()}")
        


        