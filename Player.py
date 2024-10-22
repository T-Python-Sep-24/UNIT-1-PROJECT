
import sys
import time
import pickle
import os

from Game import Game
class Player:
    def __init__(self,style:str='member') -> None:
        self.__style=self.set_player_style(style)
        self.__masseges=self.__load_from_file("masseges.pkl")

    def set_player_style(self,style):
        self.__style=style
    def get_player_type(self)->str:
        return self.__style
    
    def __save_to_file(self,filename: str):
        try:
            with open(filename,'wb') as file:
                pickle.dump(self.__masseges,file)
        except Exception as e:
            print(f"Error saving data to file: {e}")
    def __load_from_file(self,filename: str):
            try:
                with open(filename,'rb') as file:
                    return pickle.load(file) 
            except (FileNotFoundError, EOFError):
                return []
    #Home page public function
    def home_page_public(self):
        os.system('cls')
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
                self.display_chat_community()
                input('Press Enter to continue >>>\n')
            elif player_choice2=="0":
                break        
            else:
                print("Invalid choice. Please try again.")
                input('Press Enter to continue >>>\n')

    def games_list(self):
        os.system('cls')
        while True:
                print("Games list")
                #trendig games
                print("1- Adventure")
                print("2- Rhythm")
                print("3- Crazy Questions")
                print("4- Rock, Paper, Scissors")
                print("5- X-O game")
                print("6- Pacman")
                print("7- Simon Says")
                print("0- Go back")
                
                player_choice2=input("Your Choice: ")
                print()
                if player_choice2=="1":
                    #function to start a game
                    self.loading_animation()
                    os.system('cls')
                    game_disc=''' Start in a Village: Begin with an ancient map hinting at hidden treasure. 🗺️
Objectives: Your goal is to make choices that lead you to the treasure. Be cautious and consider your options:
1. Decide to explore further or dig for treasure. 🏴‍☠️
2. Uncover the treasure 🎉 or abandon your quest.'''
                    advanture_game=Game('Adventure',game_disc)
                    advanture_game.intro_game()          
                    if(advanture_game.adventure_game()):
                        advanture_game.increase_player_score(self)
                elif player_choice2=="2":
                    #function to start a game
                    self.loading_animation()
                    os.system('cls')
                    game_disc='''Your mission is to match your keystrokes to the beat!🎶
Objectives:
1. Press the correct key (a, s, d, or f) as prompted. ⏱️
2. Score points for each correct hit! 🎯
3. Avoid missing beats to maintain your rhythm! 💔'''
                    rhythm_game=Game('Rhythm',game_disc)
                    rhythm_game.intro_game()          
                    if(rhythm_game.rhythm_game()):
                        rhythm_game.increase_player_score(self)
                    
                elif player_choice2=="3":
                    #function to start a game
                    self.loading_animation()
                    #os.system('cls')
                    game_disc=''' Prepare for a fun and unpredictable challenge!
Objectives:
1. Answer a series of wild and wacky question! ❓
2. Use your creativity and humor to impress! 😂'''
                    crazy_game=Game('Crazy',game_disc)
                    crazy_game.intro_game()          
                    if(crazy_game.crazy_game()):
                        crazy_game.increase_player_score(self)

                elif player_choice2=="4":
                    self.loading_animation()
                    os.system('cls')
                    #function to start a game
                    game_disc='''Rock-Paper-Scissors is played between two players. 
Each player simultaneously choose one of three shapes.
Objective: The objective of the game is to choose a shape that defeats \nthe opponent's shape based on the following rules:
1. Rock crushes Scissors (Rock wins) ✊ ✂️
2. Scissors cuts Paper (Scissors wins) ✂️ 📄
3. Paper covers Rock (Paper wins) 📄 ✊'''
                    rock_paper_scissors_game=Game('Rock-Paper-Scissors',game_disc)
                    rock_paper_scissors_game.intro_game()
                    print("Choose the game mode:")
                    print("1- Computer Mode")
                    print("2- Multi-Players Mode")
                    game_mode=input("Your Choice: ")
                    if game_mode=="1":
                        if(rock_paper_scissors_game.rock_paper_scissors()):
                            rock_paper_scissors_game.increase_player_score(self)
                    elif game_mode=="2":
                        rock_paper_scissors_game.set_game_style('multi')
                        if(rock_paper_scissors_game.rock_paper_scissors()):
                            rock_paper_scissors_game.increase_player_score(self)
                    else:
                        print("Invalid choice. Please try again.")    
                elif player_choice2=="5":
                    #function to start a game
                    self.loading_animation()
                    os.system('cls')
                    #function to start a game
                    game_disc=''' X-O game is played on a 3x3 grid between two players.
Each player takes turns marking a square with their symbol: (❌ or ⭕).
Objective: The goal of the game is to be the first player to get three of their marks in a row, either horizontally, vertically, or diagonally.
1. Players alternate placing their mark in an empty square (choose number 1-9).
                                    1 | 2 | 3
                                    -----------
                                    4 | 5 | 6
                                    -----------
                                    7 | 8 | 9
2. The game ends when a player wins or all squares are filled (draw 🤝).
3. Players must block 🚫 opponents while trying to create their own ➕ winning line.'''
                    xo_game=Game('X-O',game_disc)
                    xo_game.intro_game()          
                    if(xo_game.XO_game()):
                        xo_game.increase_player_score(self)
                    
                elif player_choice2=="6":
                    self.loading_animation()
                    os.system('cls')
                    #function to start a game
                    game_disc='''Start in a Maze: Enter a colorful maze filled with dots and ghosts. 🌈
Objectives: Your goal is to eat all the dots while avoiding ghosts. Stay alert and make strategic moves:
1. Avoid the ghosts to stay a live! 👻
2. focus on eating all the dots to clear the maze! 🍒'''
                    pacman_game=Game('Pacman',game_disc)
                    pacman_game.intro_game()          
                    if(pacman_game.pacman_game()):
                        pacman_game.increase_player_score(self)
                        os.system('cls')
                    pass
                elif player_choice2=="7":
                    self.loading_animation()
                    os.system('cls')
                    #function to start a game
                    game_disc='''Start the Challenge: Get ready to test your memory with a fun number matching game! 🔢
Objectives: Your goal is to match pairs of numbers and reveal parts of a hidden picture. Stay sharp and make clever choices:
1. Select two numbers from the grid to find a match! 🔍
2. Each successful match reveals a piece of the mystery picture! 🖼️'''
                    memory_game=Game('Memory',game_disc)
                    memory_game.intro_game()          
                    if(memory_game.memory_game()):
                        memory_game.increase_player_score(self)
                        os.system('cls')
                    pass    
                elif player_choice2=="0":
                    break        
                else:
                    print("Invalid choice. Please try again.")
                    input('Press Enter to continue >>>\n')

    def loading_animation(self,duration=2):
        end_time = time.time() + duration
        loading_message = "Loading"
        
        while time.time() < end_time:
            for i in range(4):
                sys.stdout.write(f'\r{loading_message}{"." * i}   ') 
                sys.stdout.flush()
                time.sleep(0.5)  # speed here

        sys.stdout.write('\rLoading complete!   \n')

                
    def write_chat_community(self):
        self.display_chat_community()
        while True:
            username = self.get_member_name().capitalize()
            message = input("Type your message (or type '0' to exit): ")

            if message == '0':
                break

            self.__masseges.append(f"{username}: {message}")
            self.__save_to_file("masseges.pkl")
            os.system('cls')
            self.display_chat_community()

    def display_chat_community(self):
        os.system('cls')
        self.__masseges=self.__load_from_file("masseges.pkl")
        while True:
            
            print("---"*5," Community Messages ","---"*5)
            for msg in self.__masseges:
                print()
                print(msg,"\n")
            print("----------------------"*2)
            break





