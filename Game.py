import pickle
import random
import json
import time
import keyboard
import colorama
import subprocess
import os

class Game:
    def __init__(self,name:str,game_disc:str,game_style:str='computer') -> None:
        self.__name=name
        self.__game_disc=game_disc
        self.__game_style=game_style
        self.__games_list=self.__load_from_file('games.pkl')
        self.board = [[" " for _ in range(3)] for _ in range(3)]#X-O game
        self.current_player = "X"#X-O game
        self.location = "village" #Advanture game
        self.treasure_found = False #Advanture game
        self.rythemscore = 0#rythem game
        self.game_duration = 15#rythem game
        search_game=any(game['name'] == self.get_game_name() for game in self.__games_list)
        if search_game:
            return
        else:
            self.add_game_to_list()
    # Getters
    def get_game_name(self):
        return self.__name

    def get_game_disc(self):
        return self.__game_disc

    def get_game_style(self):
        return self.__game_style

    def get_game_adds(self):
        return self.__game_adds


    # Setters
    def set_game_name(self, name: str):
        self.__name = name

    def set_game_disc(self, game_disc: str):
        self.__game_disc = game_disc

    def set_game_style(self, game_style: str):
        self.__game_style = game_style

    def set_game_adds(self, game_adds: str):
        self.__game_adds = game_adds

    #files
    def __save_to_file(self, filename: str):
        try:
            if filename =='games.pkl':
                with open(filename,'wb') as file:
                    pickle.dump(self.__games_list,file)     
        except Exception as e:
            print(colorama.Fore.RED+f"Error saving data to file: {e}")        

    def __load_from_file(self, filename: str):
        try:
            if filename.endswith(".json"):
                with open(filename,'r') as file:
                    return json.load(file)
            elif filename.endswith(".pkl"):
                with open(filename,'rb') as file:
                    return pickle.load(file) 
        except (FileNotFoundError, EOFError):
            return []    
        
    def add_game_to_list(self):       
        game={
            "name":self.get_game_name(),
            "repetition":0
        }
        self.__games_list.append(game)
        self.__save_to_file('games.pkl')

    def display_trending_game(self)-> str:
        games_list= self.__games_list
        
        best_repitition=[]
        games_list.sort(key=lambda x: x["repetition"],reverse=True)
        for r in range(0,min(3, len(games_list))):  
            best_repitition.append(games_list[r])
        return colorama.Fore.RESET+f"Trending Games 🔥: {colorama.Fore.YELLOW+best_repitition[0]["name"]}, \
{best_repitition[1]["name"]}, \
{best_repitition[2]["name"]+colorama.Fore.RESET}"
        
        

    def intro_game(self):
        print(colorama.Fore.WHITE+"\n" + "=" * 50+colorama.Fore.RESET)
        print(colorama.Fore.BLUE+f"🎮 Welcome to the {self.get_game_name()} Game! 🎮"+colorama.Fore.RESET)
        print("=" * 50)
        print(colorama.Fore.BLUE+"\nHere's how to play:")
        print(colorama.Fore.WHITE+self.get_game_disc())
        input(colorama.Fore.YELLOW+'\nPress Enter to start 🌟\n')
        print(colorama.Fore.WHITE+"\n" + "=" * 50)
    
    def __increase_game_repetition(self):
        search_game=list(filter(lambda game:game['name'] == self.get_game_name() ,self.__games_list))
        search_game[0]['repetition']=search_game[0]['repetition']+1
        self.__save_to_file("games.pkl")
        self.__games_list=self.__load_from_file('games.pkl')

    def increase_player_score(self,player):
        if player.get_player_type()=='member':
            members_list=player.get_memberData_list()
            for item in members_list :
                if item['name']==player.get_member_name():
                    item['score']+=2
                    break    
            player.set_memberData_list(members_list)
    
    '''rock_paper_scissors game'''
    def rock_paper_scissors(self) -> bool:
         #increase game repetition
        self.__increase_game_repetition()
        game_result=False
        #Computer-mode
        if self.get_game_style()=='computer':
            while True:
                print("Rock ✊, Paper 📄, Scissors ✂️ ...")
                player_move=input("Enter your move: ")
                computer_move=(self.__computer_rock_paper_scissors()).lower()
                if player_move.lower() == computer_move :
                    print(colorama.Fore.YELLOW+"It's a draw! ⚖️ ")
                    print(colorama.Fore.BLUE+"Press Enter to try again 🔥\n"+colorama.Fore.RESET) 
                elif (player_move.lower() == "rock" and computer_move == "scissors") or \
                    (player_move.lower() == "scissors" and computer_move == "paper") or \
                    (player_move.lower() == "paper" and computer_move== "rock"):
                    print("Computer move was: ",computer_move)
                    print(colorama.Fore.GREEN+"You are the winner 🏆")##color it green($$$)
                    game_result=True
                    input(colorama.Fore.BLUE+'\nPress Enter to go back 🔚'+colorama.Fore.RESET)
                    break
                elif (computer_move == "rock" and player_move.lower() == "scissors") or \
                    (computer_move == "scissors" and player_move.lower() == "paper") or \
                    (computer_move == "paper" and player_move.lower() == "rock"):
                    print("Computer move was: ",computer_move)
                    print(colorama.Fore.RED+"You lost 💔"+colorama.Fore.RESET)##color it red($$$)
                    input(colorama.Fore.BLUE+'\nPress Enter to go back 🔚'+colorama.Fore.RESET)
                    break
                else:
                    print(colorama.Fore.RED+"Invalid choice.\nPlease enter 'Rock','Paper' or 'Scissors'")
                    input(colorama.Fore.WHITE+'Press Enter to continue >>>\n') 
        #Multi-mode
        else:
             while True:
                print("Rock ✊, Paper 📄, Scissors ✂️...")
                player1_move=input("Player 1, enter your choice: ")
                player2_move=input("Player 2, enter your choice: ")
                if player1_move.lower() == player2_move.lower():
                    print(colorama.Fore.YELLOW+"It's a draw! ⚖️ ")
                    print(colorama.Fore.BLUE+"Press Enter to try again 🔥\n") 
                elif (player1_move.lower() == "rock" and player2_move.lower() == "scissors") or \
                    (player1_move.lower() == "scissors" and player2_move.lower() == "paper") or \
                    (player1_move.lower() == "paper" and player2_move.lower() == "rock"):
                    print(colorama.Fore.GREEN+"Player 1 wins!🏆") ##color it green($$$)
                    game_result=True
                    input(colorama.Fore.BLUE+'\nPress Enter to go back 🔚'+colorama.Fore.RESET)
                    break
                elif (player2_move.lower() == "rock" and player1_move.lower() == "scissors") or \
                    (player2_move.lower() == "scissors" and player1_move.lower() == "paper") or \
                    (player2_move.lower() == "paper" and player1_move.lower() == "rock"):
                    print(colorama.Fore.GREEN+"Player 2 wins!🏆")##color it green($$$)
                    game_result=True
                    input(colorama.Fore.BLUE+'\nPress Enter to go back 🔚'+colorama.Fore.RESET)
                    break
                else:
                    print(colorama.Fore.RED+"Invalid choice.\nPlease enter 'Rock','Paper' or 'Scissors'")
                    input(colorama.Fore.WHITE+'Press Enter to continue >>>\n')            

       
        return game_result       
    
    def __computer_rock_paper_scissors(self) -> str:
        choices = ["rock", "paper", "scissors"]
        random_choice = random.choice(choices)
        return random_choice
    



    '''# X-O game'''

    def init_board(self) -> list:
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        return self.board

    def init_current_player(self):
        self.current_player = "X"  # Player 1 is X, Player 2 is O 
        return self.current_player

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)

    def print_numbered_board(self):
        numbered_board = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]
        for row in numbered_board:
            print(" | ".join(row))
            print("-" * 9)

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True

        return False

    def is_board_full(self):
        return all(cell != " " for row in self.board for cell in row)

    def player_move(self):
        while True:
            move = input(f"Player {self.current_player}, choose your move (1-9): ")
            try:
                move = int(move)
                if move < 1 or move > 9:
                    print(colorama.Fore.RED+"Invalid input. Please enter a number between 1 and 9.")
                    input(colorama.Fore.WHITE+'Press Enter to continue >>>\n')
                    continue
                row, col = divmod(move - 1, 3)
                if self.board[row][col] != " ":
                    print(colorama.Fore.RED+"Cell already taken, try again.")
                    input(colorama.Fore.WHITE+'Press Enter to continue >>>\n')
                    continue
                return row, col
            except ValueError:
                print(colorama.Fore.RED+"Invalid input. Please enter a number between 1 and 9.")
                input(colorama.Fore.WHITE+'Press Enter to continue >>>\n')

    def computer_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == " "]
        return random.choice(empty_cells)

    def XO_game(self):
        self.__increase_game_repetition()
        self.init_board()  # Initialize the board
        self.init_current_player()  # Initialize the current player

        while True:
            print("Choose the game mode:")
            print(colorama.Fore.BLUE+"1- Computer Mode")
            print("2- Multi-Players Mode"+colorama.Fore.RESET)
            mode = input("Your Choice: ")
            if mode in ["1", "2"]:
                break
            else:
                print(colorama.Fore.RED+"Invalid choice. Please try again.")
                input(colorama.Fore.WHITE+'Press Enter to continue >>>\n')
        self.print_numbered_board()
        while True:
            self.print_board()

            if mode == "2" or (mode == "1" and self.current_player == "X"):
                row, col = self.player_move()
            else:
                row, col = self.computer_move()
                print(f"Computer chose: {row * 3 + col + 1}")

            self.board[row][col] = self.current_player

            if self.check_winner():
                self.print_board()
                print(colorama.Fore.GREEN+f"Player {self.current_player} wins! 🎉")
                input(colorama.Fore.BLUE+'\nPress Enter to go back 🔚'+colorama.Fore.RESET)
                if self.current_player=="O" and mode=="1":
                    print(colorama.Fore.RED+"You lost 💔"+colorama.Fore.RESET)
                    return False
                else:
                    return True

            if self.is_board_full():
                self.print_board()
                print(colorama.Fore.YELLOW+"It's a draw! 🤝")
                input(colorama.Fore.BLUE+'\nPress Enter to go back 🔚'+colorama.Fore.RESET)

                return False

            # Switch players
            self.current_player = "O" if self.current_player == "X" else "X"
            
    '''Adventure game'''
    def adventure_game(self):
        self.__increase_game_repetition()

        print("Welcome to the Lost Treasure of Eldoria!")
        while not self.treasure_found:
            if self.location == "village":
                self.village()
            elif self.location == "forest":
                self.forest()
            elif self.location == "treasure":
                self.treasure()
            elif self.location == "End":
                return False  
        return True        

    def village(self):
        print(colorama.Fore.YELLOW+"\nYou are in a small village. The villagers speak of a hidden treasure."+colorama.Fore.RESET)
        choice = input("Do you want to go to the Enchanted Forest to find the treasure? (yes/no) ").strip().lower()
        if choice == "yes":
            self.location = "forest"
        else:
            print(colorama.Fore.YELLOW+"You grew old and weak over the years 👵. Despite your many attempts,\n \
you were unable to find the treasure you had always dreamed of. In the end,\n\
you passed away without realizing your dream. 😔")
            input(colorama.Fore.BLUE+'\nPress Enter to go back 🔚'+colorama.Fore.RESET)
            self.location = "End"

    def forest(self):
        print(colorama.Fore.YELLOW+"\nYou enter the Enchanted Forest. It's dark and full of strange noises."+colorama.Fore.RESET)
        choice = input("Do you want to explore deeper into the forest? (yes/no) ").strip().lower()
        if choice == "yes":
            self.location = "treasure"
        else:
            print(colorama.Fore.YELLOW+"You lost your courage halfway and returned to your village feeling \n\
disappointed. 🏡 After a while, you discovered that another adventurer \n\
had found the treasure. Thus, you lost your dream of finding it.🚫")
            input(colorama.Fore.BLUE+'\nPress Enter to go back 🔚'+colorama.Fore.RESET)
            self.location = "End"

    def treasure(self):
        print(colorama.Fore.YELLOW+"\nYou find the Eldoria Oak tree! The treasure is buried beneath its roots!"+colorama.Fore.RESET)
        choice = input("Do you want to dig for the treasure? (yes/no) ").strip().lower()
        if choice == "yes":
            self.treasure_found = True
            print(colorama.Fore.GREEN+"Congratulations! You've found the treasure of Eldoria! 🎉")
            input(colorama.Fore.BLUE+'\nPress Enter to go back 🔚'+colorama.Fore.RESET)
        else:
            print(colorama.Fore.YELLOW+"You decide not to dig and leave the treasure buried. 🚫")
            input(colorama.Fore.BLUE+'\nPress Enter to go back 🔚'+colorama.Fore.RESET)
            self.location = "End"

    '''Rhythm game'''
    def rhythm_game(self):
        self.__increase_game_repetition()
        start_time = time.time()
        while time.time() - start_time < self.game_duration:
            key = random.choice(['a', 's', 'd', 'f'])
            print(f"Press '{key}'! ⏳")
            start_time_key = time.time()
            while time.time() - start_time_key < 1.5:  # 1 second to press
                if keyboard.is_pressed(key):
                    print("Nice! 🎉")
                    self.rythemscore += 1
                    break
            else:
                print(f"Oops! You missed '{key}'! 💔")
            time.sleep(0.5) 
        if (self.rythemscore>4):
            print(colorama.Fore.GREEN+f"Great! Your score is: {self.rythemscore} 🎮")
            input(colorama.Fore.BLUE+'\nPress Enter to go back 🔚'+colorama.Fore.RESET)
            return True
        else:
            print(colorama.Fore.RED+f"Game Over! Your score is: {self.rythemscore} 🎮")
            input(colorama.Fore.BLUE+'\nPress Enter to go back 🔚'+colorama.Fore.RESET)
            return False   
        
    '''Crazy game'''
    def crazy_game(self):
        self.__increase_game_repetition()
        ques_list=self.__load_from_file("questions.json")
        ques_choosen=random.choice(ques_list)
        while True:
            print(f'''Question:\n{ques_choosen["question"]}\n1- {ques_choosen["choices"][0]}
2- {ques_choosen["choices"][1]}\n3- {ques_choosen["choices"][2]}''')
            identifier=input("Your Choice:")
            player_answer=""
            if identifier=="1":
                player_answer=ques_choosen["choices"][0]
            elif identifier=="2":
                player_answer=ques_choosen["choices"][1]
            elif identifier=="3":
                player_answer=ques_choosen["choices"][2]
            else:
                print(colorama.Fore.RED+"Invalid choice. Please try again.")
                input(colorama.Fore.WHITE+'Press Enter to continue >>>\n')
            if(player_answer==ques_choosen["right"]):
                print(colorama.Fore.GREEN+"Congratulations! 🎉 You answered correctly! ✅")
                input(colorama.Fore.BLUE+'\nPress Enter to go back 🔚'+colorama.Fore.RESET)
                return True
            else:
                print(colorama.Fore.RED+f'''Unfortunately, that's an incorrect answer. ❌\n
Correct Answer: {ques_choosen["right"]}''')
                input(colorama.Fore.BLUE+'\nPress Enter to go back 🔚'+colorama.Fore.RESET)
                return False  


    '''Pacman game'''
    def pacman_game(self):
        
        try:
            self.__increase_game_repetition()
            script_path = os.path.join(os.path.dirname(__file__), 'run_pacman.py')
            result=subprocess.run(['python', script_path],capture_output=True, text=True)
            print(result.stdout)
            print(result.stderr)
            input("wewewe")
        except Exception as e:
            print(e)
        finally:
            return True

    '''Memory game'''
    def memory_game(self):
        try:
            self.__increase_game_repetition()
            subprocess.run(['freegames', 'play', 'memory'])
        except Exception as e:
            print(e)
        finally:
            return True

  