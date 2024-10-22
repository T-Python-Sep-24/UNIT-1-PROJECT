from questions import questions
from questions import emotional_intelligence_questions
from questions import learning_style_questions
from results import save_results, load_results
from famous_people import famous_people

class PersonalityQuiz:
    def __init__(self):
        self.questions = questions  # Load your questions here
        self.answers = []

    def display_question(self, question):
        """Display a single question with its options."""
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i + 1}. {option}")

    def get_user_answer(self, question):
        """Prompt user for their answer to a question and return the index."""
        while True:
            try:
                answer = int(input("Select option (1-4): ")) - 1
                if answer < 0 or answer >= len(question["options"]):
                    raise ValueError("Invalid selection.")
                return answer
            except ValueError as e:
                print(e)

    def calculate_score(self):
        """Calculate the total score based on user responses."""
        score = 0
        for question, answer in zip(self.questions, self.answers):
            score += question["weights"][answer]
        return score

    def take_quiz(self):
        """Main method to take the quiz."""
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

        print(f"Your personality type is: {personality_type}")
        print(f"Your personality type is similar to: {famous_person['name']}")
        print(f"Description: {famous_person['description']}")

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
        """Display a single question with its options."""
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i + 1}. {option}")

    def get_user_answer(self, question):
        """Prompt user for their answer to a question and return the index."""
        while True:
            try:
                answer = int(input("Select option (1-4): ")) - 1
                if answer < 0 or answer >= len(question["options"]):
                    raise ValueError("Invalid selection.")
                return answer
            except ValueError as e:
                print(e)

    def calculate_score(self):
        """Calculate the total score based on user responses."""
        score = 0
        for question, answer in zip(self.questions, self.answers):
            score += question["weights"][answer]
        return score

    def take_quiz(self):
        """Main method to take the quiz."""
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

        print(f"Your emotional intelligence level is: {ei_level}")

        # Save results
        user_results = {"score": score, "level": ei_level}
        save_results(user_results)

class LearningStyleQuiz:
    def __init__(self):
        self.questions = learning_style_questions
        self.answers = []

    def display_question(self, question):
        """Display a single question with its options."""
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i + 1}. {option}")

    def get_user_answer(self, question):
        """Prompt user for their answer to a question and return the index."""
        while True:
            try:
                answer = int(input("Select option (1-4): ")) - 1
                if answer < 0 or answer >= len(question["options"]):
                    raise ValueError("Invalid selection.")
                return answer
            except ValueError as e:
                print(e)

    def calculate_score(self):
        """Calculate the total score based on user responses."""
        score = 0
        for question, answer in zip(self.questions, self.answers):
            score += question["weights"][answer]
        return score

    def take_quiz(self):
        """Main method to take the quiz."""
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

        print(f"Your learning style is: {learning_style}")

        # Save results
        user_results = {"score": score, "style": learning_style}
        save_results(user_results)