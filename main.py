from User.Residents import Resident
from User.Managers import Manager
from Authentications.Authentication import Authenticator
from colorama import Fore
from datetime import datetime


while True:
    choice = input("Do you want to \n(1) Register Resident\n(2) Register Manager\n(3) Log in Resident\n(4) Log in Manager?\n(5) Exit \n:")
    if choice == "1":
            user_name = input("Enter username: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            phone_number = input("Enter phone number: ")
            resident_id = input("Enter a unique resident ID: ")
            
            Authenticator.register_resident(user_name, email, password, phone_number, resident_id)

    elif choice == "2":
            user_name = input("Enter name: ")
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
            while True:
                print('''
                        1-List the violations that i have (fine id,type of fine ,date,price,issued by which ministry,status)  
                        2-search for a specfic violations   
                        3-Pay all violations(installment option if the violations is more than 3000 sar)  
                        4-pay for a specfic violations(installment option if the violations is more than 3000 sar)  
                        5-send messages to management to object a violations  
                        6-see response  
                        7-Exit  
                        ''')
                resident_choice=input("choose a number: ")
                if resident_choice=='1':
                      resident.display_violations()
                
                elif resident_choice=='2':
                      violation_id=int(input("enter Violoation ID: "))
                      resident.search_violation(violation_id)
                      input("press enter to continue...")
                        

                elif resident_choice=='3':
                        resident.pay_all_violations()
                
                elif resident_choice=='4':
                        pass
                
                elif resident_choice=='5':
                        pass
                
                elif resident_choice=='6':
                        pass
                
                elif resident_choice=='7':
                        break
                
                
                

    elif choice == "4":
            email = input("Enter email: ")
            password = input("Enter password: ")
            authentication=int(input("Enter Authentication number for your ministry: "))
            manager:Manager = Authenticator.login_manager(email, password,authentication)
            if manager:
                print(Fore.GREEN+f"Welcome back, {manager.get_user_name()}!"+Fore.RESET)
            while True:
                print('''
                        1-Fine a violation for a Resident
                        2-check the violations for a Resident  
                        3-Objections review from Resident and response  
                        4-make a discount to all Resident  
                        5-make a discount for one of the Resident  
                        6-Manager log  
                        7-Exit  
                        ''')
                Manager_choice=input('Enter Choice: ')

                if Manager_choice=='1':
                    resident_id=input(("enter resident ID: "))
                    manager.fine_resident(resident_id)
                    input ("press enter to continue...")
                
                elif Manager_choice=='2':
                    resident_id=input(("enter resident ID: "))
                    manager.search_violations(resident_id)
                    input ("press enter to continue...")
                    
                elif Manager_choice=='3':
                    pass
                    
                elif Manager_choice=='4':
                    pass
                            
                elif Manager_choice=='5':
                    pass
                    
                elif Manager_choice=='6':
                    pass
                    
                elif Manager_choice=='7':
                    break
    elif choice=='5':
          break        
                
                
    else:
        print("Ivnalid Input!")
