from User.Residents import Resident
from User.Managers import Manager
from Authentications.Authentication import Authenticator
from colorama import Fore,Style


choice = input("Do you want to (1) Register Resident, (2) Register Manager, (3) Log in Resident, or (4) Log in Manager? ")

if choice == "1":
        user_name = input("Enter username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        phone_number = input("Enter phone number: ")
        resident_id = input("Enter a unique resident ID: ")
        
        Authenticator.register_resident(user_name, email, password, phone_number, resident_id)

elif choice == "2":
        user_name = input("Enter username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        phone_number = input("Enter phone number: ")
        ministry_auth = int(input("Enter ministry authentication: "))

        Authenticator.register_manager(user_name, email, password, phone_number, ministry_auth)

elif choice == "3":
        username = input("Enter ID: ")
        password = input("Enter password: ")
        resident:Resident = Authenticator.login_resident(username, password)
        if resident:
            print(Fore.GREEN+f"Welcome back, {resident.get_user_name()}!"+Fore.RESET)
            

elif choice == "4":
        email = input("Enter email: ")
        password = input("Enter password: ")
        authentication=int(input("Enter Authentication number for your ministry: "))
        manager:Manager = Authenticator.login_manager(email, password,authentication)
        if manager:
            print(Fore.GREEN+f"Welcome back, {manager.get_user_name()}!")
            
else:
       print("Ivnalid Input!")
