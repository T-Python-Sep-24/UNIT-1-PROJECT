from quiz import PersonalityQuiz, EmotionalIntelligenceQuiz, LearningStyleQuiz
from colorama import init, Fore, Style

# Initialize Colorama
init()

def main():
    print(Fore.CYAN + "Welcome to the Personal Analyst Program!" + Style.RESET_ALL)
    while True:
        print("\n" + Fore.YELLOW + "Please choose an option:" + Style.RESET_ALL)
        print(Fore.GREEN + "1. Take Personality Quiz" + Style.RESET_ALL)
        print(Fore.GREEN + "2. Take Emotional Intelligence Test" + Style.RESET_ALL)
        print(Fore.GREEN + "3. Take Learning Style Assessment" + Style.RESET_ALL)
        print(Fore.RED + "4. Exit" + Style.RESET_ALL)

        command = input(Fore.WHITE + "Enter a number (1-4): " + Style.RESET_ALL).strip()

        if command == "1":
            # Call the Personality Quiz function
            pass
        elif command == "2":
            # Call the Emotional Intelligence Test function
            pass
        elif command == "3":
            # Call the Learning Style Assessment function
            pass
        elif command == "4":
            print(Fore.MAGENTA + "Thank you for using the Personal Analyst Program. Goodbye!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid input. Please enter a number between 1 and 4." + Style.RESET_ALL)

if __name__ == "__main__":
    main()