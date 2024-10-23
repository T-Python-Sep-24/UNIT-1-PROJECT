from quiz import PersonalityQuiz, EmotionalIntelligenceQuiz, LearningStyleQuiz
from colorama import init, Fore, Style
# Initialize Colorama
init()
def print_welcome():
    print(Fore.CYAN + "\n" + "=" * 50)  # Top border
    print(Fore.CYAN + Style.BRIGHT + " Welcome to Discover Yourself Program!" + Style.RESET_ALL)
    print(Fore.CYAN + "=" * 50 + "\n")  # Bottom border4
def main():
    print_welcome()  # Call the function to print the welcome message

    while True:
        print(Fore.YELLOW + "Please choose an option:" + Style.RESET_ALL)
        print(Fore.GREEN + "1. Take Personality Quiz" + Style.RESET_ALL)
        print(Fore.GREEN + "2. Take Emotional Intelligence Test" + Style.RESET_ALL)
        print(Fore.GREEN + "3. Take Learning Style Assessment" + Style.RESET_ALL)
        print(Fore.RED + "4. Exit" + Style.RESET_ALL)

        command = input(Fore.WHITE + "Enter a number (1-4): " + Style.RESET_ALL).strip()
        print(f"The chosen test : You entered '{command}'")  

        if command == "1":
            quiz = PersonalityQuiz()
            quiz.take_quiz()
        elif command == "2":
            quiz = EmotionalIntelligenceQuiz()
            quiz.take_quiz()
        elif command == "3":
            quiz = LearningStyleQuiz()
            quiz.take_quiz()
        elif command == "4":
            print(Fore.MAGENTA + "Thank you for using the Discover Yourself Program. Goodbye!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid input. Please enter a number between 1 and 4." + Style.RESET_ALL)

if __name__ == "__main__":
     main()
    