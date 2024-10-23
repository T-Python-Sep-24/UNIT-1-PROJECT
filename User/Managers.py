from User.Users import Person
import json
from CustomErrors.MyExceptions import AuthenticationError
from datetime import datetime
from colorama import Fore
from User.Residents import Resident
from Data.File_handler import Data_management
from Data.ViolationCounter import load_violation_counter,save_violation_counter
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
    # Predefined authentication number per ministry
    

    def __init__(self, user_name: str, email: str, password: str, phone_number:str,ministry_authentication:int) -> None:
        super().__init__(user_name, email, password, phone_number)
        self.is_valid(ministry_authentication)
        self.authentication_number=ministry_authentication
        self.ministry_name=self.ministry_authentications.get(ministry_authentication)
        self.action_log = []
        self.Ministry_violations=self.__Ministries_Violations()
    
    def get_authentication_number(self)->None:
        '''
        The function returns the authentication number to verfiy manager
        Args:
            self(manager):an object that hold the current manager
        Returns:
            None

        '''
        return self.authentication_number
    
    def is_valid(self,authentication_number:int)->bool:
        '''
        the function is to check the authentication number that the user put 
        Args:
            self(manager): an object that hold the current manager
            authentication_number(int): an authentication number to check 
        Returns:
            True if the authentication that the user put is in the Predefined ministry authentication
        '''
        if authentication_number in self.ministry_authentications:
            return True
        else:
            raise AuthenticationError(Fore.RED+"The number you provided is not register in any of the ministries!!")
        
    def get_ministry_name(self)->str:
        '''
        the function return the name of the manager ministry
        Args:
            self(manager):an object 
        Returns:
            ministry_name(str):the name of the manager ministry
        '''
        return self.ministry_name
    
    def __Ministries_Violations(self)->dict:
        '''
        the function opens a json file and load the content of it 
        Args:
            self(manager):an object
        Returns:
            Ministry_violations(dict):violations for each ministry 

        '''
        with open ('User/Ministry_Violations.json','r',encoding="UTF-8")as file:
                Ministry_violations=json.load(file)
        return Ministry_violations
    
    def log_manager_action(self, action_type: str, details: dict)->None:
        '''
        the function log every action that the manager do and saves it to a list
        Args:
            self(manager):an obejct
            action_type(str):the action that the manager did
            detalis(dict):a dictionary that saves the details of the action the manager did
        Returns:
            None
        '''
        log_entry = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Action": action_type,
            "Details": details    
        }
        self.action_log.append(log_entry)

    def display_manager_log(self)->None:
        '''
        The function displays the logs of the manager
        Args:
            self(manager):an object
        Returns:
            None
        '''
        if self.action_log:
            print(f"Logs for Manager: {self.get_user_name()}")
            for log in self.action_log:
                print(f"Timestamp: {log['Timestamp']}")
                print(f"Action: {log['Action']}")
                print(f"Details: {log['Details']}")
                print("-" * 40)  # Divider between log entries
        else:
            print(f"No logs found for Manager: {self.get_user_name()}")

    def fine_resident(self,Resident_id:str)->None:
        '''
        the function fine a violation for a specfic resident 
        Args:
            self(manager):an object
            Reisdent_id(str): the id of the resident to fine 
        Returns:
            None
        '''
        residents:Resident=Data_management.load_file('Residents.pkl')
        if Resident_id in residents:
            violation_id = load_violation_counter()
            save_violation_counter(violation_id + 1)
            print(f"Violations Type for {self.get_ministry_name()}")
            violations=self.Ministry_violations[self.get_ministry_name()]
            for idx,violation in enumerate(violations,start=1):
                print(f"{idx}. {violation['Violation_type']} - {violation['Amount']} SAR")
            try:
                choice = int(input("Enter choice: "))
            except ValueError:
                print(Fore.RED+"Invalid input! Please enter a valid number."+Fore.RED)
                return

            if 1<=choice<=len(violations):
                selected_violation=violations[choice-1]
                residents[Resident_id].add_violation(violation_id,selected_violation['Violation_type'],selected_violation['Amount'],self.get_ministry_name())
                Data_management.save_file(residents,'Residents.pkl')
                self.log_manager_action(
                    action_type="Fine Issued",
                    details={
                        "Resident ID": Resident_id,
                        "Violation Type": selected_violation['Violation_type'],
                        "Amount": selected_violation['Amount']
                    })
                print(Fore.LIGHTGREEN_EX+f"Violation {selected_violation['Violation_type']} has been added to resident {Resident_id}"+Fore.RESET)
            else:
                print("Invalid input!")
        else:
            print("there is no resident with this ID!")
    
    def search_violations(self,resident_id:str)->None:
        '''
        The function search violation of the manager ministry to a specfic resident
        Args:
            self(manager):an object
            resident_id(str): the resident id of the resident the manager want to search
        Returns:
            None
        '''
        residents:Resident=Data_management.load_file('Residents.pkl')
        if resident_id in residents:
            residents[resident_id].search_violation_by_ministry(self.get_ministry_name())
            self.log_manager_action(
                action_type="Violation Search",
                details={"Resident ID": resident_id}
                )
        else:
            print("there is no resident with this ID!")
    
    def discount_for_specfic_resident(self,Resident_id:str,percentage:float)->None:
        '''
        The function dicount violation of the manager ministry for a specfic reisdent
        Args:
            self(manager):an object
            resident_id(str): the resident id of the resident the manager want to discount thier violations
            percentage(float): the percentage that the manager wants discount
        Returns:
            None
        '''
        residents:Resident=Data_management.load_file('Residents.pkl')
        if Resident_id in residents:
            residents[Resident_id].make_discount(self.get_ministry_name(),percentage) 
            Data_management.save_file(residents,'Residents.pkl')
            self.log_manager_action(
                action_type="Discount Applied to Specific Resident",
                details={
                    "Resident ID": Resident_id,
                    "Percentage": percentage
                }
            )  
        else:
            print("there is no resident with this ID!")
    
    def discount_for_all_resident(self,percentage:float):
        '''
        The function dicount violation of the manager ministry for a all reisdents 
        Args:
            self(manager):an object
            percentage(float): the percentage that the manager wants discount
        Returns:
            None
        '''
        residents:Resident=Data_management.load_file('Residents.pkl')
        for resident_id,resident in residents.items():
            resident.make_discount(self.get_ministry_name(),percentage) 
            Data_management.save_file(residents,'Residents.pkl')
      
        self.log_manager_action(
            action_type="Discount Applied to All Residents",
            details={"Percentage": percentage}
        )
        
            

        


        