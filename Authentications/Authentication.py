from Data.File_handler import Data_management
from CustomErrors.MyExceptions import RegisterError,LoginError
from User.Residents import Resident
from User.Managers import Manager
from colorama import Fore,Style
class Authenticator:
    
    def register_resident(user_name, email, password, phone_number, resident_id):
        '''
        Registers a new resident.
        Args:
            user_name (str): The user's name.
            email (str): The user's email.
            password (str): The user's password.
            phone_number (str): The user's phone number.
            resident_id (str): The ID of the resident.

        Returns:
            None
        Raises:
            RegisterError: If the resident with the same ID already exists.
        '''
        residents=Data_management.load_file('Residents.pkl')
        if resident_id in residents:
            raise RegisterError(Fore.RED+"The Resident with this id allready registered!!"+Fore.RESET)
        new_resident=Resident(user_name,email,password,phone_number,resident_id)
        residents[resident_id]=new_resident
        Data_management.save_file(residents,'Residents.pkl')
        print(Fore.GREEN+f"The resident: {user_name} has been registered Successfully"+Fore.RESET) 
    
    def register_manager(user_name, email, password, phone_number, authentication_number):
        '''
        Registers a new manager.

        Args:
            user_name (str): The manager's name.
            email (str): The manager's email.
            password (str): The manager's password.
            phone_number (str): The manager's phone number.
            authentication_number (str): The authentication number of the ministry.

        Returns:
            None
        Raises:
            RegisterError: If a manager with the same email already exists.
        '''
        Managers=Data_management.load_file('Managers.pkl')
        if email in Managers:
            raise RegisterError(Fore.RED+"The Managers with this email allready registered!!"+Fore.RESET)
        new_manager=Manager(user_name,email,password,phone_number,authentication_number)
        Managers[email]=new_manager
        Data_management.save_file(Managers,'Managers.pkl')
        print(Fore.GREEN+f"The Manager: {user_name} has been registered Successfully"+Fore.RESET) 
    
    def login_resident(id,password):
        '''
        Logs in a resident.

        Args:
            id (str): The resident's ID.
            password (str): The resident's password.

        Returns:
            Resident: The resident object if login successful.

        Raises:
            LoginError: If the ID or password is incorrect.
        '''
        residents=Data_management.load_file('Residents.pkl')
        for resident in residents.values():
            if id==resident.get_id() and password==resident.get_password():
                return resident
        else:
            raise LoginError(Fore.RED+"Wrong ID or password!"+Fore.RESET)

    def login_manager(email,password,authentication_number):
        '''
        Logs in a manager.

        Args:
            email (str): The manager's email.
            password (str): The manager's password.
            authentication_number (str): The authentication number of the ministry.

        Returns:
            Manager: The manager object if login successful.

        Raises:
            LoginError: If the email, password, or authentication number is incorrect.
        '''
        Managers=Data_management.load_file('Managers.pkl')
        for manager in Managers.values():
            if email==manager.get_email() and password==manager.get_password() and authentication_number==manager.get_authentication_number():
                 return manager
        else:
            raise LoginError(Fore.RED+"Wrong Email or password or authentication number!"+Fore.RESET)

    