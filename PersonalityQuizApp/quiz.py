from questions import questions
from questions import emotional_intelligence_questions
from questions import learning_style_questions
from results import save_results, load_results
from famous_people import famous_people
from Emotions_Tips import emotional_intelligence_advice  
from Learning_Tips import learning_style_advice  
from colorama import init, Fore, Style

# Initialize Colorama
init() 

class PersonalityQuiz:
    def __init__(self):
        self.questions = questions  # Load your questions here
        self.answers = []

    def display_question(self, question):
        # Display a single question with its options.
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i + 1}. {option}")

    def get_user_answer(self, question):
        # Prompt user for their answer to a question and return the index.
        while True:
            try:
                answer = int(input("Select option (1-4): ")) - 1
                if answer < 0 or answer >= len(question["options"]):
                    raise ValueError("Invalid selection.")
                return answer
            except ValueError as e:
                print(e)

    def calculate_score(self):
        # Calculate the total score based on user responses.
        score = 0
        for question, answer in zip(self.questions, self.answers):
            score += question["weights"][answer]
        return score

    def take_quiz(self):
        # Main method to take the quiz.
        for question in self.questions:
            self.display_question(question)
            answer = self.get_user_answer(question)
            self.answers.append(answer)

        score = self.calculate_score()

        # Determine personality type based on score
        if score < 0:
            personality_type = "Introvert"
        elif score < 10:
            personality_type = "Ambivert"
        else:
            personality_type = "Extrovert"

        # Get the famous person associated with the personality type
        famous_person = famous_people[personality_type]
        print(Fore.CYAN + "\n" + "=" * 90)  # Top border
        print(Fore.YELLOW + f"Your Personality Type is: {personality_type}" + Style.RESET_ALL)  # Personality type in yellow
        print(Fore.CYAN + "=" * 90 + Style.RESET_ALL)  # Divider
        print(Fore.MAGENTA + f"Your personality type is similar to: {famous_person['name']}" + Style.RESET_ALL)  # Famous person in magenta
        print(Fore.GREEN + f"Description: {famous_person['description']}" + Style.RESET_ALL)  # Description in green
        print(Fore.CYAN + "=" * 50 + Style.RESET_ALL)  # Bottom border

        # Save results including famous person's details
        user_results = {
            "score": score,
            "type": personality_type,
            "famous_person": famous_person["name"],
            "description": famous_person["description"]
        }
        save_results(user_results)


class EmotionalIntelligenceQuiz:
    def __init__(self):
        self.questions = emotional_intelligence_questions  
        self.answers = []

    def display_question(self, question):
        # Display a single question with its options
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i + 1}. {option}")

    def get_user_answer(self, question):
        # Prompt user for their answer to a question and return the index
        while True:
            try:
                answer = int(input("Select option (1-4): ")) - 1
                if answer < 0 or answer >= len(question["options"]):
                    raise ValueError("Invalid selection.")
                return answer
            except ValueError as e:
                print(e)

    def calculate_score(self):
        # Calculate the total score based on user responses
        score = 0
        for question, answer in zip(self.questions, self.answers):
            score += question["weights"][answer]
        return score

    def take_quiz(self):
        # Main method to take the quiz
        for question in self.questions:
            self.display_question(question)
            answer = self.get_user_answer(question)
            self.answers.append(answer)

        score = self.calculate_score()

        # Determine emotional intelligence level based on score
        if score < 5:
            ei_level = "Low Emotional Intelligence"
        elif score < 10:
            ei_level = "Average Emotional Intelligence"
        else:
            ei_level = "High Emotional Intelligence"

        # Get tailored advice and books based on emotional intelligence level
        advice_data = emotional_intelligence_advice[ei_level]
        
        # Display results in the CLI
        print(Fore.CYAN + "\n" + "=" * 90)  # Top border
        print(Fore.YELLOW + f"Your Emotional Intelligence Level is: {ei_level}" + Style.RESET_ALL)  # Level in yellow
        print(Fore.CYAN + "=" * 90 + Style.RESET_ALL)  # Bottom border
        print(Fore.MAGENTA + "\nAdvice Based on Your Emotional Intelligence Level:" + Style.RESET_ALL)
        print(Fore.MAGENTA + "-" * 50 + Style.RESET_ALL)  # Separator line
        for item in advice_data["advice"]:
            print(Fore.GREEN + item + Style.RESET_ALL)  # Advice in green

        print(Fore.MAGENTA + "\nRecommended Books:" + Style.RESET_ALL)
        print(Fore.MAGENTA + "-" * 50 + Style.RESET_ALL)  # Separator line
        for book in advice_data["books"]:
            print(Fore.RESET + book + Style.RESET_ALL)  # Books in green
            print(Fore.CYAN + "=" * 50 + Style.RESET_ALL)  # Bottom border

        # Prepare results to save
        user_results = {
            "score": score,
            "level": ei_level,
            "advice": advice_data["advice"],
            "books": advice_data["books"]
        }

        save_results(user_results)
 

class LearningStyleQuiz:
    def __init__(self):
        self.questions = learning_style_questions  # Load your questions
        self.answers = []

    def display_question(self, question):
        # Display a single question with its options.
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i + 1}. {option}")

    def get_user_answer(self, question):
        # Prompt user for their answer to a question and return the index.
        while True:
            try:
                answer = int(input("Select option (1-4): ")) - 1
                if answer < 0 or answer >= len(question["options"]):
                    raise ValueError("Invalid selection.")
                return answer
            except ValueError as e:
                print(e)

    def calculate_score(self):
        # Calculate the total score based on user responses.
        score = 0
        for question, answer in zip(self.questions, self.answers):
            score += question["weights"][answer]
        return score

    def take_quiz(self):
        # Main method to take the quiz.
        for question in self.questions:
            self.display_question(question)
            answer = self.get_user_answer(question)
            self.answers.append(answer)

        score = self.calculate_score()

        # Determine learning style based on score
        if score < 5:
            learning_style = "Visual"
        elif score < 10:
            learning_style = "Auditory"
        else:
            learning_style = "Kinesthetic"

        print(Fore.CYAN + "\n" + "=" * 90)  # Top border
        print(Fore.YELLOW + f"Your learning style is: {learning_style}" + Style.RESET_ALL)  # Level in yellow
        print(Fore.CYAN + "=" * 90 + Style.RESET_ALL)  # Bottom border
        # Get advice, resources, and tools based on learning style
        advice_data = learning_style_advice[learning_style]

              # Print advice
        print(Fore.MAGENTA + "\nAdvice Based on Your Learning Style:" + Style.RESET_ALL)
        print(Fore.MAGENTA + "-" * 50 + Style.RESET_ALL)  # Separator line
        for item in advice_data["advice"]:
            print(Fore.CYAN + item + Style.RESET_ALL)  # Advice in green

        # Print recommended resources
        print(Fore.MAGENTA + "\nRecommended Resources:" + Style.RESET_ALL)
        print(Fore.MAGENTA + "-" * 50 + Style.RESET_ALL)  # Separator line
        for resource in advice_data["resources"]:
            print(Fore.RESET + resource + Style.RESET_ALL)  # Resources in green

        # Print recommended tools
        print(Fore.MAGENTA + "\nRecommended Tools:" + Style.RESET_ALL)
        print(Fore.MAGENTA + "-" * 50 + Style.RESET_ALL)  # Separator line
        for tool in advice_data["tools"]:
            print(Fore.GREEN + tool + Style.RESET_ALL)  # Tools in green

        print(Fore.CYAN + "=" * 50 + Style.RESET_ALL)  # Bottom border
        # Save results
        user_results = {
            "score": score,
            "style": learning_style,
            "advice": advice_data["advice"],
            "resources": advice_data["resources"],
            "tools": advice_data["tools"]
        }
        save_results(user_results)
