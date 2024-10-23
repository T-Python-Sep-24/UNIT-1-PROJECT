from Player import Player
from Member import Member
import os
import colorama
import art

def clear_screen():
    # Clear the terminal screen for Windows or Unix/Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_screen()#diff systems
    title=art.text2art("Galaxy Games", space=2)
    print(colorama.Fore.MAGENTA+ title)
    print(colorama.Fore.WHITE+"Welcome to Galaxy Games ! 🎮")
    print("Are you a new player?")
    print(colorama.Fore.BLUE + "1- YES")
    print(colorama.Fore.BLUE + "2- NO")
    print(colorama.Fore.RED + "0- Exit")
    player_state = input(colorama.Fore.WHITE + "Your Choice: ")

 

    if player_state == "1":
        clear_screen()
        print(colorama.Fore.WHITE +"Join our community and enjoy more features! ✨")
        print(colorama.Fore.BLUE +'1- Sign up now')
        print(colorama.Fore.BLUE +"2- Go directly to the games")
        player_choice=input(colorama.Fore.WHITE +"Your Choice: ")


        if player_choice=="1":     
            print(colorama.Back.WHITE+colorama.Fore.BLACK+"SIGN UP"+colorama.Back.RESET,"\n")
            print(colorama.Fore.WHITE +"Fill the form please.")
            player_name=input(colorama.Fore.BLUE +"Please enter your name:"+colorama.Fore.RESET)
            player_name=player_name.lower()
            player_password=input(colorama.Fore.BLUE +"Enter your password (6 digits):"+colorama.Fore.RESET)
            
            #check password number
            if  player_password.isdigit() and len(player_password)==6:
                
                #create new member instance
                new_member=Member("member",player_name,player_password)
                is_valid_name=new_member.record_new_member(new_member.get_member_name())
                if is_valid_name:
                    #show list of his home page (member)
                    print(colorama.Fore.WHITE +f"We’re excited to have you join us, {new_member.get_member_name().capitalize()}! Let’s get started!\n")
                    new_member.home_page_member()
            else:
                print(colorama.Fore.RED +"Invalid password format.\nPlease enter password as 6 digits\n--------------------") 
                input(colorama.Fore.WHITE +'Press Enter to continue >>>\n')  
                 
        elif player_choice=="2":

            visitor=Player("visitor")
            dummy_member=Member("member","dummy member","000000")
            #show list of his home page (public)

            visitor.home_page_public(dummy_member)
            pass

        else:

                 print(colorama.Fore.RED+"Invalid choice. Please try again.")
                 input(colorama.Fore.WHITE +'Press Enter to continue >>>\n')
        
    elif player_state == "2":
        clear_screen()
        print(colorama.Back.WHITE+colorama.Fore.BLACK+"SIGN IN"+colorama.Back.RESET,"\n")
        print(colorama.Fore.WHITE +"We are happy to see you again ;)")
        player_name=input(colorama.Fore.BLUE +"Please enter your name:"+colorama.Fore.RESET)
        player_name=player_name.lower()
        player_password=input(colorama.Fore.BLUE+"Enter your password (6 digits):"+colorama.Fore.RESET)
        #check password number
        if  player_password.isdigit() and len(player_password)==6:
                #create new member instance
                old_member=Member("member",player_name,player_password)
                #check his data and load it -else-
                is_valid_member=old_member.sign_in_member(old_member.get_member_name())
                if is_valid_member:
                    #show list of his home page (member)
                    old_member.home_page_member() 
        else:
 
            print(colorama.Fore.RED+"Invalid ID format.\nPlease enter password as 6 digits\n--------------------") 
            input(colorama.Fore.WHITE +'Press Enter to continue >>>\n')  
         

    elif player_state=="0":
            clear_screen()
            thanks=art.text2art("Thank you",font='cybermedum')
            print(colorama.Fore.MAGENTA+thanks)
            break
    else:
 
            print(colorama.Fore.RED+"Invalid choice. Please try again.")
            input(colorama.Fore.WHITE +'Press Enter to continue >>>\n')

