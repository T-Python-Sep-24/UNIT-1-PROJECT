
import sys
import time
import os
from Game import Game
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
            print("0- Exit")#Done
            player_choice2=input("Your Choice: ")
            print()
            if player_choice2=="1":
                #show games list
                self.games_list()
                #games list function
            elif player_choice2=="2":
                #display the community and write
                pass
            elif player_choice2=="0":
                break        
            else:
                print("Invalid choice. Please try again.")

    def games_list(self):
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
                    self.loading_animation()
                    os.system('cls')
                    #function to start a game
                    game_disc='''Rock-Paper-Scissors is played between two players. 
Each player simultaneously choose one of three shapes.
Objective: The objective of the game is to choose a shape that defeats \nthe opponent's shape based on the following rules:
1. Rock crushes Scissors (Rock wins)✊✂️
2. Scissors cuts Paper (Scissors wins)✂️📄
3. Paper covers Rock (Paper wins)📄✊'''
                    rock_paper_scissors_game=Game('Rock-Paper-Scissors',game_disc)
                    rock_paper_scissors_game.intro_game()
                    print("Choose the game mode:")
                    print("1- Computer Mode")
                    print("2- Multi-Players Mode")
                    game_mode=input("Your Choice: ")
                    if game_mode=="1":
                        rock_paper_scissors_game.rock_paper_scissors()
                    elif game_mode=="2":
                        rock_paper_scissors_game.set_game_style('multi')
                        rock_paper_scissors_game.rock_paper_scissors()
                        pass
                    else:
                        print("Invalid choice. Please try again.")    
                elif player_choice2=="6":
                    #function to start a game
                    pass
                elif player_choice2=="7":
                    #function to start a game
                    pass
                elif player_choice2=="8":
                    #function to start a game
                    pass    
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