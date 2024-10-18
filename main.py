from Player import Player
from Member import Member
while True:
    print("\nWelcome to Game Land")
    print('''Are you new player?
1- YES
2- NO
0- Exit ''')
    player_state=input("Your Choice: ")
    print("--------------------")

    if player_state == "1":
        print("Join our community and enjoy more features!")
        print('''
1- Sign up now 
2- Go directly to the games''')
        player_choice=input("Your Choice: ")
        print()

        if player_choice=="1":
            print("Fill the form please.")
            player_name=input("Please enter your name:")
            player_id=input("Enter your ID (6 digits):")
            #check id
            
            #create new member player
            new_member=Member("member",player_name,player_id)
            input('Press Enter to continue >>>')
            #show list of his home page (member)

            #Home page function
                 
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
        player_id=input("Enter your ID (6 digits):")
        #check his data and load it -else- 

    elif player_state=="0":
            print("Thank you")
            print("See you later...")
            break
    else:
            print("Invalid choice. Please try again.")



#Home page member function
def home_page_member():#as parameter should have object (member)
     # welcoming the user by its name
     while True:
          print("Home page (member)")
          #trendig games
          print("1- Games")
          print("2- Community")
          print("3- Achievements and badges (money)")
          print("4- My purchases")
          print("5- Change my name or ID")
          print("0- Exit")
          
          player_choice2=input("Your Choice: ")
          print()
          if player_choice2=="1":
               #show games list
               #games list function
               pass
          elif player_choice2=="2":
               #display the community (can't write)
               pass
          elif player_choice2=="3":
               #display Achievements and badges (money)
               pass 
          elif player_choice2=="4":
               #display the purchases (hints&adds)
               pass
          elif player_choice2=="5":
               #update info
               pass     
          elif player_choice2=="0":
               break
               pass        
          else:
               print("Invalid choice. Please try again.")

