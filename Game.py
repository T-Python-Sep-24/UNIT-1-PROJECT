import pickle
import random
class Game:
    def __init__(self,name:str,game_disc:str,game_adds:list=[],game_style:str='computer') -> None:
        self.__name=name
        self.__game_disc=game_disc
        self.__game_style=game_style
        self.__game_adds=game_adds#load from file
        self.__games_list=self.__load_from_file('games.pkl')
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


    def __save_to_file(self, filename: str):
        try:
            with open(filename,'wb') as file:
                pickle.dump(self.__games_list,file)
        except Exception as e:
            print(f"Error saving data to file: {e}")        

    def __load_from_file(self, filename: str):
        try:
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

    def intro_game(self):
        print("\n" + "=" * 60)
        print(f"🎮 Welcome to the {self.get_game_name()} Game! 🎮")
        print("=" * 60)
        print("\nHere's how to play:")
        print(self.get_game_disc())
        input('\nPress Enter to start 🌟\n')
        print("\n" + "=" * 60)
    
    def rock_paper_scissors(self):
        #Computer-mode
        if self.get_game_style()=='computer':
            while True:
                print("Rock ✊, Paper 📄, Scissors ✂️...")
                player_move=input("Enter your move: ")
                computer_move=(self.__computer_rock_paper_scissors()).lower()
                if player_move.lower() == computer_move :
                    print("It's a draw! ⚖️ ")
                    print("Press Enter to try again 🔥") 
                elif (player_move.lower() == "rock" and computer_move == "scissors") or \
                    (player_move.lower() == "scissors" and computer_move == "paper") or \
                    (player_move.lower() == "paper" and computer_move== "rock"):
                    print("Computer move was: ",computer_move)
                    print("You are the winner 🏆")
                    input('\nPress Enter to go back 🔚')
                    break
                elif (computer_move == "rock" and player_move.lower() == "scissors") or \
                    (computer_move == "scissors" and player_move.lower() == "paper") or \
                    (computer_move == "paper" and player_move.lower() == "rock"):
                    print("Computer move was: ",computer_move)
                    print("You lost 💔")
                    input('\nPress Enter to go back 🔚')
                    break
                else:
                    print("Invalid choice.\nPlease enter 'Rock','Paper' or 'Scissors'")
                    input('Press Enter to continue >>>\n')
        #Multi-mode
        else:
             while True:
                print("Rock ✊, Paper 📄, Scissors ✂️...")
                player1_move=input("Player 1, enter your choice: ")
                player2_move=input("Player 2, enter your choice: ")
                if player1_move.lower() == player2_move.lower():
                    print("It's a draw! ⚖️ ")
                    print("Press Enter to try again 🔥") 
                elif (player1_move.lower() == "rock" and player2_move.lower() == "scissors") or \
                    (player1_move.lower() == "scissors" and player2_move.lower() == "paper") or \
                    (player1_move.lower() == "paper" and player2_move.lower() == "rock"):
                    print("Player 1 wins!🏆") 
                    input('\nPress Enter to go back 🔚')
                    break
                elif (player2_move.lower() == "rock" and player1_move.lower() == "scissors") or \
                    (player2_move.lower() == "scissors" and player1_move.lower() == "paper") or \
                    (player2_move.lower() == "paper" and player1_move.lower() == "rock"):
                    print("Player 2 wins!🏆")
                    input('\nPress Enter to go back 🔚')
                    break
                else:
                    print("Invalid choice.\nPlease enter 'Rock','Paper' or 'Scissors'")
                    input('Press Enter to continue >>>\n')            

        #increase game repetition
        self.__increase_game_repetition()
                
    def __computer_rock_paper_scissors(self) -> str:
        choices = ["rock", "paper", "scissors"]
        random_choice = random.choice(choices)
        return random_choice
    
    def __increase_game_repetition(self):
        search_game=list(filter(lambda game:game['name'] == self.get_game_name() ,self.__games_list))
        search_game[0]['repetition']=search_game[0]['repetition']+1
        self.__save_to_file("games.pkl")
        self.__games_list=self.__load_from_file('games.pkl')
