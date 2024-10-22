from colorama import init, Fore, Style
from .user import User
from .sentiment_analyzer import SentimentAnalyzer

class WellnessQuest:
    def __init__(self):
        self.users = {}
        self.sentiment_analyzer = SentimentAnalyzer()
        init()

    def display_welcome_message(self):
        print("\n" + Fore.CYAN + "*" * 50 + Style.RESET_ALL)
        print(" " * 10 + Fore.GREEN + "Welcome to the Wellness Quest!" + Style.RESET_ALL)
        print(" " * 10 + "Track your wellness journey and receive personalized recommendations.")
        print(Fore.CYAN + "*" * 50 + Style.RESET_ALL + "\n")

    def main_menu(self):
        print("\n" + Fore.MAGENTA + "=" * 50 + Style.RESET_ALL)
        print("Main Menu:")
        print("1. Start Emotional Assessment")
        print("2. Journal Prompt")
        print("3. Exit")
        print(Fore.MAGENTA + "=" * 50 + Style.RESET_ALL)
        return input("Choose an option: ")

    def journal_prompt(self):
        """Allow users to write a journal entry based on a prompt."""
        prompt = "Reflect on your day. What made you happy or stressed?"
        print(Fore.CYAN + prompt + Style.RESET_ALL)
        journal_entry = input("Your journal entry: ").strip()

        if journal_entry:
            # Analyze the journal entry using both TextBlob and VADER
            textblob_result = self.sentiment_analyzer.analyze_text_textblob(journal_entry)
            vader_result = self.sentiment_analyzer.analyze_text_vader(journal_entry)

            print(Fore.GREEN + "Thank you for your entry!" + Style.RESET_ALL)
            print(Fore.YELLOW + "TextBlob Analysis:" + Style.RESET_ALL)
            print(f"Polarity: {textblob_result['polarity']}, Subjectivity: {textblob_result['subjectivity']}")
            print(Fore.YELLOW + "VADER Analysis:" + Style.RESET_ALL)
            print(f"Positive: {vader_result['pos']}, Neutral: {vader_result['neu']}, Negative: {vader_result['neg']}, Compound: {vader_result['compound']}")
        else:
            print(Fore.RED + "You didn't enter anything." + Style.RESET_ALL)

    def run(self):
        self.display_welcome_message()

        user_name = input("Please enter your name: ").strip()
        
        if user_name not in self.users:
            self.users[user_name] = User(user_name)
        
        user = self.users[user_name]

        while True:
            choice = self.main_menu()
            
            if choice == '1':
                print("Feature not yet implemented: Emotional Assessment")
                # Implement emotional assessment feature here

            elif choice == '2':
                self.journal_prompt()  # Call the journal prompt method

            elif choice == '3':
                print(Fore.RED + "Exiting Wellness Quest. Take care!" + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + "Invalid choice, please try again." + Style.RESET_ALL)