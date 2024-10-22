import nltk
from assessments.mood_assessment import assess_mood
from recommendations.activities import recommend_activity
from utils.emotion_generator import generate_emotions
from resources.local_resources import display_resources
from games.fun_games import play_game
from colorama import Fore, init
import sys

# Initialize colorama for Windows support
init(autoreset=True)

# Download NLTK data if not already downloaded
nltk.download('wordnet', quiet=True)

def clear_screen():
    """Clear the console screen for better readability."""
    print("\n" * 100)

def display_welcome(name):
    """Display a welcoming message to the user."""
    print(Fore.CYAN + "🌟 Welcome to Your Emotional Adventure! 🌟")
    print(Fore.GREEN + f"✨ Hello, {name}! Let's embark on a journey of self-discovery and emotional wellness. 🌈")

def main():
    clear_screen()
    name = input(Fore.YELLOW + "👤 Enter your name: ").strip()
    display_welcome(name)

    score = 0  # Initialize score to ensure it exists for recommendations

    while True:
        print(Fore.BLUE + "\n🎭 Menu:")
        print(Fore.MAGENTA + "1️⃣ Emotional Assessment 🧠")
        print(Fore.MAGENTA + "2️⃣ Recommendations 🌻")
        print(Fore.MAGENTA + "3️⃣ Local Mental Health Resources 🇸🇦")
        print(Fore.MAGENTA + "4️⃣ Fun Games Galore 🎮")
        print(Fore.MAGENTA + "5️⃣ Log Mood 🌈")
        print(Fore.MAGENTA + "6️⃣ Exit with a Smile 😊")

        choice = input(Fore.YELLOW + "\nChoose an option (1-6): ")

        if choice == '1':
            # Conduct mood assessment
            score, mood = assess_mood()
            print(Fore.YELLOW + f"Your mood score is: {score:.2f}")
            print(Fore.GREEN + f"Your current mood is: {mood}")

            # Generate and print related emotions
            emotions = generate_emotions(mood)
            print(Fore.YELLOW + f"Related emotions: {', '.join(emotions)}")

            # Provide activity recommendations based on the user's mood score
            activities = recommend_activity(score)
            print(Fore.BLUE + "\n🌟 Recommendations based on your mood assessment:")
            for activity in activities:
                print(Fore.YELLOW + activity)

        elif choice == '2':
            # Provide activity recommendations based on the previously assessed score
            activities = recommend_activity(score)
            print(Fore.GREEN + "🌟 Based on your mood, here are some activities:")
            for activity in activities:
                print(Fore.YELLOW + activity)

        elif choice == '3':
            # Display local mental health resources
            display_resources()

        elif choice == '4':
            # Play a fun game
            play_game()

        elif choice == '5':
         print("Log your mood:")
         print("Options: happy, sad, neutral, anxious, relaxed, frustrated, excited")
         mood = input("Please enter your mood: ").strip().lower()
         valid_moods = ['happy', 'sad', 'neutral', 'anxious', 'relaxed', 'frustrated', 'excited']
    
    if mood in valid_moods:
        detailed_feeling = input("Would you like to describe how you feel? (yes/no): ").strip().lower()
        if detailed_feeling == 'yes':
            description = input("Please describe your feelings: ")
            print(Fore.GREEN + f"Your mood '{mood}' has been logged with the description: '{description}'.")
        else:
            print(Fore.GREEN + f"Your mood '{mood}' has been logged.")
    else:
        print(Fore.RED + "❌ Invalid mood entry. Please enter one of the following: happy, sad, neutral, anxious, relaxed, frustrated, excited.")
if __name__ == '__main__':
    main()
