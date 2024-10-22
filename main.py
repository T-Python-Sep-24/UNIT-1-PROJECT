from Player import Player
from Member import Member
import os
while True:
    os.system('cls')
    print("\n🎮🌟 Welcome to Games Galaxy! 🌟🎮")
    print('''Are you new player?
1- YES
2- NO
0- Exit ''')
    player_state=input("Your Choice: ")
    print("-"*50)
    os.system('cls')#diff systems

    if player_state == "1":
        print("Join our community and enjoy more features! ✨")
        print('''
1- Sign up now 
2- Go directly to the games''')
        player_choice=input("Your Choice: ")
        print()

        if player_choice=="1":
            print("Fill the form please.")
            player_name=input("Please enter your name:")
            player_name=player_name.lower()
            player_password=input("Enter your password (6 digits):")
            
            #check password number
            if  player_password.isdigit() and len(player_password)==6:
                
                #create new member instance
                new_member=Member("member",player_name,player_password)
                is_valid_name=new_member.record_new_member(new_member.get_member_name())
                if is_valid_name:
                    #show list of his home page (member)
                    print(f"\nWe’re excited to have you join us, {new_member.get_member_name().capitalize()}! Let’s get started!\n")
                    new_member.home_page_member()
            else:
                print("Invalid password format.\nPlease enter password as 6 digits\n--------------------") 
                input('Press Enter to continue >>>\n')  
                 
        elif player_choice=="2":
            visitor=Player("visitor")
            #show list of his home page (public)
            visitor.home_page_public()
            pass

        else:
                 print("Invalid choice. Please try again.")
        
    elif player_state == "2":
        print("We are happy to see you again ;)")
        player_name=input("Please enter your name:")
        player_name=player_name.lower()
        player_password=input("Enter your password (6 digits):")
        #check password number
        if  player_password.isdigit() and len(player_password)==6:
                #create new member instance
                old_member=Member("member",player_name,player_password)
                #check his data and load it -else-
                is_valid_member=old_member.sign_in_member(old_member.get_member_name())
                if is_valid_member:
                    #show list of his home page (member)
                    print(f"\nWe’re excited to have you join us, {old_member.get_member_name().capitalize()}! Let’s get started!\n")
                    old_member.home_page_member() 
        else:
            print("Invalid ID format.\nPlease enter password as 6 digits\n--------------------") 
            input('Press Enter to continue >>>\n')  
         

    elif player_state=="0":
            print("Thank you")
            print("See you later...")
            break
    else:
            print("Invalid choice. Please try again.")
            input('Press Enter to continue >>>\n')

