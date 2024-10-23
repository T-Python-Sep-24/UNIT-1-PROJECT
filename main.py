from User.Residents import Resident
from User.Managers import Manager
from Authentications.Authentication import Authenticator
from CustomErrors.MyExceptions import *
from colorama import Fore
from datetime import datetime
from Data.File_handler import Data_management

residents=Data_management.load_file('Residents.pkl')
managers = Data_management.load_file('Managers.pkl')
while True:
    try:
        user_type = input("Are you a Resident or a Manager? (Enter 'R' for Resident, 'M' for Manager, or 'E' to Exit): ").strip().upper()
        if user_type=='R':
            while True:
                try:
                    choice = input("Do you want to \n1-Register Resident\n2-Log in Resident\n3-Exit\nEnter Choice: ")
                    if choice=='1':  
                        try:                             
                            user_name = input("Enter name: ")
                            email = input("Enter email: ")
                            password = input("Enter password: ")
                            phone_number = input("Enter phone number: ")
                            resident_id = input("Enter a unique resident ID: ")
                            Authenticator.register_resident(user_name, email, password, phone_number, resident_id)
                            input("Press Enter to continue...")
                        except (RegisterError,EmailError,PasswordError,PhoneNumberError,IDError)as e:
                            print(Fore.RED + str(e) + Fore.RESET)
                            input("Press Enter to continue...")
                        except Exception as e:
                            print(Fore.RED+str(e)+Fore.RESET)
                            input("Press Enter to continue...")

                    elif choice=='2':
                        try:
                            id = input("Enter ID: ")
                            password = input("Enter password: ")
                            resident:Resident = Authenticator.login_resident(id, password) 
                            print(Fore.GREEN+f"Welcome , {resident.get_user_name()}!"+Fore.RESET)
                            input("Press Enter to continue...")

                            while True:
                                try:
                                    print('''
                                    1-List the violations that i have (fine id,type of fine ,date,price,issued by which ministry,status)  
                                    2-search for a specfic violations
                                    3-Add to wallet  
                                    4-check wallet
                                    5-Pay all violations(installment option if the violations is more than 3000 sar)  
                                    6-pay for a specfic violations
                                    7-pay installment violation
                                    8-Display installment details
                                    9-Exit  
                                    ''')
                                    resident_choice=input("choose a number: ")
                                    if resident_choice=='1':
                                        resident.display_violations()
                                        input("Press Enter to continue...")

                                    elif resident_choice=='2':
                                        try:
                                            violation_id = int(input("Enter violation ID: "))
                                            resident.search_violation(violation_id)
                                            input("Press Enter to continue...")
                                        except ValueError:
                                            print(Fore.RED + "Invalid input. Violation ID must be an integer." + Fore.RESET)
                                            input("Press Enter to continue...")

                                    elif resident_choice=='3':
                                        try:
                                            amount=float(input("Enter the amount that You want to add to your wallet :"))
                                            resident.wallet.deposit(amount)
                                            residents[id] = resident
                                            Data_management.save_file(residents, 'Residents.pkl')
                                            input("Press Enter to continue...")
                                        except ValueError :
                                            print(Fore.RED + "Invalid input. Amount must be a valid number." + Fore.RESET)
                                            input("Press Enter to continue...")
                                                         
                                    elif resident_choice=='4':
                                        print(Fore.GREEN+f'Wallet: {resident.wallet.get_balance()}'+Fore.RESET)
                                        input("Press Enter to continue...")
                                                
                                    elif resident_choice == '5':
                                        resident.pay_all_violations()
                                        residents[id] = resident
                                        Data_management.save_file(residents, 'Residents.pkl')
                                        input("Press Enter to continue...")
                                                
                                    elif resident_choice=='6':
                                        try:
                                            violation_id = int(input("Enter violation ID: "))
                                            resident.pay_specfic_violation(violation_id)
                                            residents[id] = resident
                                            Data_management.save_file(residents, 'Residents.pkl')
                                            input("Press Enter to continue...")
                                        except ValueError:
                                            print(Fore.RED + "Invalid input. Violation ID must be an integer." + Fore.RESET)
                                            input("Press Enter to continue...")
                                        except Exception as e:
                                            print(Fore.RED + f"An unexpected error occurred: {str(e)}" + Fore.RESET)
                                            input("Press Enter to continue...")
                                                
                                    elif resident_choice == '7':
                                        resident.make_installment_payment()
                                        residents[id] = resident
                                        Data_management.save_file(residents, 'Residents.pkl')
                                        input("Press Enter to continue...")
                                    
                                    elif resident_choice=='8':
                                        resident.display_installment_details()
                                        input("Press Enter to continue...")
                                                
                                    elif resident_choice == '9':
                                        residents[id] = resident
                                        Data_management.save_file(residents, 'Residents.pkl')
                                        break

                                    else:
                                        print(Fore.RED + "Invalid choice, please try again!" + Fore.RESET)
                                        input("Press Enter to continue...")
                                except ValueError:
                                    print(Fore.RED + "Invalid input. Please enter a valid option." + Fore.RESET) 
                                    input("Press Enter to continue...")

                        except LoginError as e:
                            print(Fore.RED+str(e)+Fore.RESET)
                            input("Press Enter to continue...")
                    elif choice=='3':
                        break
                        
                    else:
                        print(Fore.RED + "Invalid input, please choose a valid option!" + Fore.RESET)
                        input("Press Enter to continue...")

                except Exception as e:
                    print(Fore.RED + f"An unexpected error occurred: {str(e)}" + Fore.RESET)
#-----------------------------------------------------------------------------------------------------
        elif user_type=='M':
            while True:
                try:
                    choice = input("Do you want to \n(1) Register Manager\n(2) Log in Manager\n(3) Exit \nEnter Choice: ")
                    if choice=='1':
                        try:
                            user_name = input("Enter name: ")
                            email = input("Enter email: ")
                            password = input("Enter password: ")
                            phone_number = input("Enter phone number: ")
                            ministry_auth = int(input("Enter ministry authentication: "))
                            Authenticator.register_manager(user_name, email, password, phone_number, ministry_auth)
                            input("Press Enter to continue...")
                        except (EmailError, PasswordError, PhoneNumberError, AuthenticationError) as e:
                            print(Fore.RED + str(e) + Fore.RESET)
                            input("Press Enter to continue...")
                        except RegisterError as e:
                            print(Fore.RED + "Registration error: " + str(e) + Fore.RESET)
                            input("Press Enter to continue...")

                    elif choice=='2':
                        try:
                            email = input("Enter email: ")
                            password = input("Enter password: ")
                            authentication = int(input("Enter authentication number for your ministry: "))
                            manager: Manager = Authenticator.login_manager(email, password, authentication)
                            print(Fore.GREEN + f"Welcome back, {manager.get_user_name()}!" + Fore.RESET)
                            input("Press Enter to continue...")
                            while True:
                                try:
                                    print('''
                                    1-Fine a violation for a Resident
                                    2-Check the violations for a Resident  
                                    3-Make a discount for one of the Residents  
                                    4-Make a discount to all Residents  
                                    5-Manager log  
                                    6-Exit  
                                    ''')
                                    Manager_choice = input('Enter Choice: ')

                                    if Manager_choice == '1':
                                        resident_id = input("Enter Resident ID: ")
                                        manager.fine_resident(resident_id)
                                        managers[email] = manager
                                        Data_management.save_file(managers, 'Managers.pkl')
                                        input("Press Enter to continue...")

                                    elif Manager_choice == '2':
                                        resident_id = input("Enter Resident ID: ")
                                        manager.search_violations(resident_id)
                                        managers[email] = manager
                                        Data_management.save_file(managers, 'Managers.pkl')
                                        input("Press Enter to continue...")

                                    elif Manager_choice == '3':
                                        resident_id = input("Enter Resident ID: ")
                                        try:
                                            percentage = float(input("Enter percentage that you want to discount: "))
                                            manager.discount_for_specfic_resident(resident_id, percentage)
                                            managers[email] = manager
                                            Data_management.save_file(managers, 'Managers.pkl')
                                            input("Press Enter to continue...")
                                        except ValueError:
                                            print(Fore.RED + "Invalid input. Percentage must be a number." + Fore.RESET)
                                            input("Press Enter to continue...")

                                    elif Manager_choice == '4':
                                        try:
                                            percentage = float(input("Enter percentage that you want to discount: "))
                                            manager.discount_for_all_resident(percentage)
                                            managers[email] = manager
                                            Data_management.save_file(managers, 'Managers.pkl')
                                            input("Press Enter to continue...")
                                        except ValueError:
                                             print(Fore.RED + "Invalid input. Percentage must be a number." + Fore.RESET)
                                             input("Press Enter to continue...")

                                    elif Manager_choice == '5':
                                        manager.display_manager_log()
                                        input("Press Enter to continue...")

                                    elif Manager_choice == '6':
                                        managers[email] = manager
                                        Data_management.save_file(managers, 'Managers.pkl')
                                        break

                                    else:
                                        print(Fore.RED + "Invalid choice, please try again!" + Fore.RESET)
                                        input("Press Enter to continue...")
                                except ValueError:
                                        print(Fore.RED + "Invalid input. Please enter a valid option." + Fore.RESET)
                                        input("Press Enter to continue...")
                        except AuthenticationError as e:
                            print(Fore.RED + "Login error: " + str(e) + Fore.RESET)
                            input("Press Enter to continue...")
                    elif choice=='3':
                        break
                    
                    else:
                        print(Fore.RED + "Invalid choice, please try again!" + Fore.RESET)
                        input("Press Enter to continue...")

                except Exception as e:
                    print(Fore.RED + f"An unexpected error occurred: {str(e)}" + Fore.RESET)
                    input("Press Enter to continue...")
        elif user_type =='E':
            print(Fore.CYAN+"See you next time !"+Fore.RESET)
            break

        else:
            print(Fore.RED+"Invaild Input please Choose one of theese letters (R)for resident(M)for manager(E)to exit"+Fore.RESET)
            input("Press Enter to continue...")
    except KeyboardInterrupt :
        print(Fore.YELLOW + "\nSession interrupted. Exiting..." + Fore.RESET)
        break
    except Exception as e:
        print(Fore.RED + f"An unexpected error occurred: {str(e)}" + Fore.RESET)
        input("Press Enter to continue...")



                        




                            