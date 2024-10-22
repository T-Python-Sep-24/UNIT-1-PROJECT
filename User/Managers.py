from User.Users import Person
import json
from CustomErrors.MyExceptions import AuthenticationError
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
    # Predefined violations per ministry
    

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
    
    def __Ministries_Violations(self):
        with open ('User/Ministry_Violations.json','r',encoding="UTF-8")as file:
                Ministry_violations=json.load(file)
        return Ministry_violations

    def fine_resident(self,Resident_id:str):
        residents:Resident=Data_management.load_file('Residents.pkl')
        if Resident_id in residents:
            violation_id = load_violation_counter()
            save_violation_counter(violation_id + 1)
            print(f"Violations Type for {self.get_ministry_name()}")
            Ministry_violations=self.__Ministries_Violations()
            violations=Ministry_violations[self.get_ministry_name()]
            for idx,violation in enumerate(violations,start=1):
                print(f"{idx}. {violation['Violation_type']} - {violation['Amount']} SAR")
            choice=int(input("Enter choice: "))
            if 1<=choice<=len(violations):
                selected_violation=violations[choice-1]
                residents[Resident_id].add_violation(violation_id,selected_violation['Violation_type'],selected_violation['Amount'],self.get_ministry_name())
                Data_management.save_file(residents,'Residents.pkl')
            else:
                print("Invalid input!")
        else:
            print("there is no resident with this ID!")
    
    def search_violations(self,resident_id:str):
        residents:Resident=Data_management.load_file('Residents.pkl')
        if resident_id in residents:
            residents[resident_id].search_violation_by_ministry(self.get_ministry_name())
        else:
            print("there is no resident with this ID!")
    
    def discount_for_specfic_resident(self,Resident_id:str,presentage:float):
        residents:Resident=Data_management.load_file('Residents.pkl')
        if Resident_id in residents:
            residents[Resident_id].make_discount(self.get_ministry_name(),presentage) 
            Data_management.save_file(residents,'Residents.pkl')  
        else:
            print("there is no resident with this ID!")
    
    def discount_for_all_resident(self,presentage:float):
        residents:Resident=Data_management.load_file('Residents.pkl')
        for resident in residents:
            resident[resident.get_id()].make_discount(self.get_ministry_name(),presentage) 
            Data_management.save_file(residents,'Residents.pkl')  
        else:
            print("there is no resident with this ID!")
        
            

        


        