# app.py
from assessments.mood_assessment import assess_mood
from recommendations.activities import recommend_activity
from resources.local_resources import display_resources
from games.fun_games import play_game
from progress.tracking import track_progress
from colorama import Fore, Style, init

# Initialize colorama for Windows support
init(autoreset=True)

def main():
    print(Fore.CYAN + "🌟 Welcome to Your Emotional Adventure! 🌟")
    name = input(Fore.YELLOW + "👤 Enter your name: ")

    print(Fore.GREEN + f"✨ Hello, {name}! Let's start your emotional journey. 🌈")
    
    while True:
        print(Fore.BLUE + "\n🎭 Menu:")
        print(Fore.MAGENTA + "1️⃣ Emotional Assessment 🧠")
        print(Fore.MAGENTA + "2️⃣ Recommendations 🌻")
        print(Fore.MAGENTA + "3️⃣ Local Mental Health Resources 🇸🇦")
        print(Fore.MAGENTA + "4️⃣ Fun Games Galore 🎮")
        print(Fore.MAGENTA + "5️⃣ Track Your Progress 📊")
        print(Fore.MAGENTA + "6️⃣ Exit with a Smile 😊")
        choice = input(Fore.YELLOW + "\nChoose an option (1-6): ")

        if choice == '1':
            mood = assess_mood()
            print(Fore.GREEN + f"Thanks for sharing, {name}! You are feeling {Fore.RED}{mood}.")
        elif choice == '2':
            mood = assess_mood()  # Reuse mood assessment
            activities = recommend_activity(mood)
            print(Fore.GREEN + f"🌟 Based on your mood, here are some recommendations for you: {Fore.YELLOW}{activities}")
        elif choice == '3':
            display_resources()
        elif choice == '4':
            play_game()
        elif choice == '5':
            track_progress()
        elif choice == '6':
            print(Fore.CYAN + "🚪 Exiting... Stay positive and smile! 😄")
            break
        else:
            print(Fore.RED + "❌ Invalid option. Please choose between 1 and 6.")

if __name__ == '__main__':
    main()
