import time
import json
from colorama import Fore
from emojis import emojis
from spellchecker import SpellChecker
from rich.console import Console

console = Console()

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
            console.print("No stories found. Please create some stories first.",style="#C62E2E")
            self.stories = {}
        except json.JSONDecodeError:
            console.print("Error reading the story file. Please check the file format.",style="#C62E2E")
            self.stories = {}

    def load_questions(self):
        try:
            with open("question.json", "r") as file:
                self.questions = json.load(file)
        except FileNotFoundError:
            console.print("No questions found. Please create some questions first.",style="#C62E2E")
            self.questions = {}
        except json.JSONDecodeError:
            console.print("Error reading the question file. Please check the file format.",style="#C62E2E")
            self.questions = {}

    def display_menu(self):
        print("\033[H\033[J")
        console.print("Welcome to the Reading and Writing Challenge! \n",style="#C8A1E0")
        console.print('''
           1. The Hare and the Tortoise
           2. The Elephant and the Ants
           3. The Lion and the Mouse
           4. Write your own story 
           5. Display all kids stories
           6. Exit
        ''',style="#B4D6CD")
         


    def write_to_file(self, content):
        with open('story.txt', 'a') as file:
            file.write(content)

    def check_spelling(self, text):
        words = text.split()
        corrected_text = []
        corrections = []
        
        for word in words:
            if self.spell_checker.unknown([word]):  
                correct_word_candidates = self.spell_checker.candidates(word)
                if correct_word_candidates:  
                    best_suggestion = max(correct_word_candidates, key=lambda w: self.spell_checker.word_frequency[w])  
                    corrected_text.append(best_suggestion)
                    corrections.append((word, best_suggestion))
                else:
                    corrected_text.append(word)  
                corrected_text.append(word)  

        return ' '.join(corrected_text), corrections

    def read_story(self, title, content):
        start_time = time.time()
        print("\033[H\033[J") 
        print(content)
        input(Fore.WHITE+"Press 'Enter' when you finish reading..."+Fore.RESET)  
        
        end_time = time.time()
        time_taken = (end_time - start_time) / 60
        console.print(f"You took {time_taken:.2f} minutes to read '{title}'.",style="#FFF1DB")

    def ask_questions(self, story_number):
        start_time = time.time()
        
        for q in self.questions.get(story_number, []):
            print(q["question"])
            for idx, option in enumerate(q["options"], start=1):
                print(f"{idx}. {option}")

            attempts = 0
            while attempts < 2: 
                user_answer = input("Choose the correct option number: ").strip()
                
                if not user_answer:  # Check if input is empty
                    console.print("Invalid input. Please try again.", style="#C62E2E")
                    continue  # Prompt again without incrementing attempts

                elif user_answer.isdigit() and int(user_answer) - 1 < len(q["options"]):
                    selected_answer = q["options"][int(user_answer) - 1].lower()
                    if selected_answer == q["answer"].lower():
                        console.print("Correct!",emojis.encode(":tada:"), style="#88C273")
                        break
                    else:
                        console.print("Oops! Try again.",emojis.encode(":thinking_face:"), style="#C62E2E")
                        attempts += 1
                else:
                    console.print("Invalid option. Try again.", style="#C62E2E")

            if attempts == 2:
                console.print(f"The correct answer is: {q['answer']}", style="#88C273")

        end_time = time.time()
        time_taken = (end_time - start_time) / 60  
        console.print(f"You took {time_taken:.2f} minutes to answer the questions.", style="#FFF1DB")
       

    def display_loaded_stories(self):
        console.print("Loaded Stories from JSON:" , style= "#FF8C9E")
        for key, (title, content) in self.stories.items():
            console.print(f"Title: {title}",style= "#B4D6CD")
            print(content)
            print("-" * 40)


    def read_write(self):
        while True:
            self.display_menu()
            choose = input("Choose number 1 - 6: ")

            if choose in self.stories:
                title, story_content = self.stories[choose]
                self.read_story(title, story_content)
                input("Press 'Enter' to answer the questions ")
                print("\033[H\033[J")  
                self.ask_questions(choose)

                console.print("Returning to the main menu...", style="#88C273")
                input("Press 'Enter' to continue...")
                print("\033[H\033[J")

            elif choose == '4':
                print("\033[H\033[J")

                story_title = input("Write your story title then press enter: ")
                your_story = input("Write your story then press enter: ")
                corrected_story, corrections = self.check_spelling(your_story)  
                self.write_to_file(f"{story_title} : \n{corrected_story} . \n ")
                
                print(f"\nYour story titled '{story_title}': \n{your_story}\n") 
                
                if corrections:  
                    console.print("Corrections made:", style="#88C273")
                    for original, corrected in corrections:
                        print(f"'{original}' -> '{corrected}'")  
                    console.print("Great job! Keep writing and expressing your creativity! ",emojis.encode(":sparkles:"),style="#E2BFD9")
                    input(Fore.WHITE+"Press 'Enter' when you finish reading..."+Fore.RESET)
                     
                   
            elif choose == '5':
                
                with open('story.txt', 'r') as file:
                    for s in file:
                        print(s.strip())
                input(Fore.WHITE+"Press 'Enter' when you finish reading..."+Fore.RESET)

            elif choose == '6':
                console.print("Exiting the program.", style="#C8A1E0")
                print("\033[H\033[J") 
                break

            else:
                console.print("Invalid choice. Please select again.", style="#C62E2E")


            
            
