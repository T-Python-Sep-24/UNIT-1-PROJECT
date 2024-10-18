
import sys
import time

class Player:
    def __init__(self,style:str) -> None:
        self.__style=self.set_player_style(style)
        pass

    def set_player_style(self,style):
        self.__style=style
    def get_player_type(self)->str:
        return self.__style
    
    #Home page public function
    def home_page_public(self):
        while True:
            print("Home page (public)")
            #trendig games
            print("1- Games")
            print("2- Community")
            print("0- Exit")
            player_choice2=input("Your Choice: ")
            print()
            if player_choice2=="1":
                #show games list
                self.loading_animation()
                self.games_list()
                #games list function
            elif player_choice2=="2":
                #display the community and write
                pass
            elif player_choice2=="0":
                break        
            else:
                print("Invalid choice. Please try again.")

    def games_list(self):##as parameter should have object (member)
        while True:
                print("Games list")
                #trendig games
                print("1- Text Adventure Game")
                print("2- Virtual Pet Caretaker")
                print("3- Rhythm Game")
                print("4- Tricky Questions")
                print("5- Rock, Paper, Scissors")
                print("6- X-O game")
                print("7- Timer Challenge")
                print("8- Memory challenge")
                print("#- Return to home page")
                print("0- Exit")
                
                player_choice2=input("Your Choice: ")
                print()
                if player_choice2=="1":
                    #function to start a game
                    pass
                elif player_choice2=="2":
                    #function to start a game
                    pass
                elif player_choice2=="3":
                    #function to start a game
                    pass 
                elif player_choice2=="4":
                    #function to start a game
                    pass
                elif player_choice2=="5":
                    #function to start a game
                    pass
                elif player_choice2=="6":
                    #function to start a game
                    pass
                elif player_choice2=="7":
                    #function to start a game
                    pass
                elif player_choice2=="8":
                    #function to start a game
                    pass 
                elif player_choice2=="#":
                    self.home_page_public()    
                elif player_choice2=="0":
                    break        
                else:
                    print("Invalid choice. Please try again.")

    def loading_animation(self,duration=3):
        end_time = time.time() + duration
        loading_message = "Loading"
        
        while time.time() < end_time:
            for i in range(4):  # Create a rotating effect
                sys.stdout.write(f'\r{loading_message}{"." * i}   ')  # Display dots
                sys.stdout.flush()
                time.sleep(0.5)  # Adjust speed here

        sys.stdout.write('\rLoading complete!   \n')