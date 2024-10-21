import time
import json
from art import *
from colorama import Fore
from spellchecker import SpellChecker

class Story:

    def __init__(self):
        self.load_stories()
        self.load_questions()
        self.spell_checker = SpellChecker()

    def load_stories(self):
        try:
            with open("story.json", "r") as file:
                self.stories = json.load(file)
        except FileNotFoundError:
            print("No stories found. Please create some stories first.")
            self.stories = {}
        except json.JSONDecodeError:
            print("Error reading the story file. Please check the file format.")
            self.stories = {}

    def load_questions(self):
        try:
            with open("question.json", "r") as file:
                self.questions = json.load(file)
        except FileNotFoundError:
            print("No questions found. Please create some questions first.")
            self.questions = {}
        except json.JSONDecodeError:
            print("Error reading the question file. Please check the file format.")
            self.questions = {}

    def display_menu(self):
        print(text2art("Welcome to the Reading and Writing Challenge! \n", font='straight'))
        print(text2art('''
           1. The Hare and the Tortoise
           2. The Elephant and the Ants
           3. The Lion and the Mouse
           4. Write your own story 
           5. Display all kids stories
           6. Exit
        ''', font='straight'))

    def write_to_file(self, content):
        with open('story.txt', 'a') as file:
            file.write(content)

    def check_spelling(self, text):
        words = text.split()
        corrected_text = []
        corrections = []
        for word in words:
            corrected_word = self.spell_checker.candidates(word)
            
            if corrected_word:  # Check if candidates is not empty
                correct_word = corrected_word.pop()  # Get one of the suggestions
                corrected_text.append(correct_word)
                corrections.append((word, correct_word))
            else:
                corrected_text.append(word)  # If no correction found, keep the original word
                
        return ' '.join(corrected_text), corrections


    def read_story(self, title, content):
        start_time = time.time()
        print(content)
        input("Press 'Enter' when you finish reading...")  
        
        end_time = time.time()
        time_taken = (end_time - start_time) / 60
        print(f"{Fore.GREEN}You took {time_taken:.2f} minutes to read '{title}'.{Fore.RESET}")

    def ask_questions(self, story_number):
        start_time = time.time()
        
        for q in self.questions.get(story_number, []):
            print(q["question"])
            for idx, option in enumerate(q["options"], start=1):
                print(f"{idx}. {option}")

            attempts = 0
            while attempts < 2: 
                user_answer = input("Choose the correct option number: ")
                if int(user_answer) - 1 < len(q["options"]):
                    selected_answer = q["options"][int(user_answer) - 1].lower()
                    if selected_answer == q["answer"].lower():
                        print(Fore.GREEN + "Correct!" + Fore.RESET)
                        break
                    else:
                        print(Fore.RED + "Wrong! Try again." + Fore.RESET)
                        attempts += 1
                else:
                    print(Fore.RED + "Invalid option. Try again." + Fore.RESET)

            if attempts == 2:
                print(Fore.RED + f"The correct answer is: {q['answer']}" + Fore.RESET)

        end_time = time.time()
        time_taken = (end_time - start_time) / 60  
        print(f"{Fore.GREEN}You took {time_taken:.2f} minutes to answer the questions.{Fore.RESET}")

    def display_loaded_stories(self):
        print(Fore.YELLOW + "Loaded Stories from JSON:" + Fore.RESET)
        for key, (title, content) in self.stories.items():
            print(f"{Fore.CYAN}Title: {title}{Fore.RESET}")
            print(content)
            print("-" * 40)


    def read_write(self):
        self.display_menu()
        choose = input("Choose number 1 - 5: ")

        while True:
            if choose in self.stories:
                title, story_content = self.stories[choose]
                self.read_story(title, story_content)
                input("Press 'Enter' to answer the questions ")
                print("\033[H\033[J")  
                self.ask_questions(choose)

            elif choose == '4':
                story_title = input("Write your story title then press enter: ")
                your_story = input("Write your story then press enter: ")
                corrected_story, corrections = self.check_spelling(your_story)  
                self.write_to_file(f"{story_title} : \n{corrected_story} . \n ")
                
                print(f"\nYour story titled '{story_title}': \n{corrected_story}\n")  
                if corrections:  
                    print("Corrections made:")
                    for original, corrected in corrections:
                        print(f"'{original}' -> '{corrected}'")  

            elif choose == '5':
                with open('story.txt','r') as file:
                    for s in file:
                        print(s.strip())

            elif choose == '6':
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please select again.")

            self.display_menu()
            choose = input("Choose number 1 - 6: ")
