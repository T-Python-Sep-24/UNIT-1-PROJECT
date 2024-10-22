from quiz import PersonalityQuiz, EmotionalIntelligenceQuiz, LearningStyleQuiz

def main():
    print("Welcome to the Personal Analyst Program!")
    while True:
        print("\nPlease choose an option:")
        print("1. Take Personality Quiz")
        print("2. Take Emotional Intelligence Test")
        print("3. Take Learning Style Assessment")
        print("4. View Results")
        print("5. Exit")

        command = input("Enter a number (1-5): ").strip()

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
            results = load_results()
            if results:
                for res in results:
                    print(res)
            else:
                print("No previous results found.")
        elif command == "5":
            print("Thank you for using the Personal Analyst Program. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")
# Placeholder function to load results
def load_results():
    return []
if __name__ == "__main__":
    main()