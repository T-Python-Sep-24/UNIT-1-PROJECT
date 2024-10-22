import os
import time
import random
from art import *
from gtts import gTTS
from colorama import *
from emojis import emojis
from rich.console import Console
from nltk.corpus import words, wordnet

console = Console()

class SpellingActivity:

    def __init__(self):
        self.word_list = words.words()
        self.total_time = 0
        self.attempts = 5 # Number of words to spell
        self.correct_count = 0

    def get_random_word(self, length, pos): 
        filtered_words = [word for word in self.word_list if len(word) == length]

        if pos:
            filtered_words = [word for word in filtered_words if wordnet.synsets(word, pos=pos)]
        return random.choice(filtered_words) if filtered_words else None

    def get_word_meaning(self, word):
        synsets = wordnet.synsets(word)
        if synsets:
            return synsets[0].definition()  
        return "Definition not available for this word."
    
    def speak(self, text):
        voice = gTTS(text=text, lang='en')
        voice.save("temp.mp3")
        
        for _ in range(3): 
            os.system("afplay temp.mp3")
            time.sleep(1)

    

    def spelling_activity(self):
        console.print("Welcome to the Spelling Challenge!",style="#C8A1E0")
        console.print(f"You will spell {self.attempts} words.",style="#FFDA76")
        
        console.print('''Select difficulty level: 
                      
                1. Easy (3 to 5 letters)
                2. Medium (6 to 8 letters)
                3. Hard (9 to 11 letters)
            ''',style="#B4D6CD")
        
        choice = input("Enter the number for difficulty level (1, 2, or 3): ").strip()
        print("\033[H\033[J") 


        if choice == '1':
            letter_range = (3, 5)  
        elif choice == '2':
            letter_range = (6, 8)  
        elif choice == '3':
            letter_range = (9, 11)  
        else:
            console.print("Invalid difficulty level. Please restart the program.",style="#C62E2E")
            return  
        
        console.print('''Select word type: 
                1. Noun
                2. Verb
                3. Adjective
                4. Adverb
        ''',style="#B4D6CD")

        pos_input = input("Enter the number for word type (1, 2, 3, or 4): ").strip().lower()
        print("\033[H\033[J") 

        Part_f_Speech = {
            '1': wordnet.NOUN,
            '2': wordnet.VERB,
            '3': wordnet.ADJ,
            '4': wordnet.ADV,
        }
        pos = Part_f_Speech.get(pos_input)

        if pos is None:
            console.print("Invalid word type. Please restart the program.",style="#C62E2E")
            return  

        for a in range(self.attempts):
            letter_count = random.randint(*letter_range)  
            random_word = self.get_random_word(letter_count, pos)

            if random_word:
                console.print(f"Your word is: {random_word}",style="#FFF1DB")
                self.speak(random_word) 
                console.print(f"Meaning: {self.get_word_meaning(random_word)}",style="#FFF1DB")  
                time.sleep(25)  
                console.print("The word will disappear in seconds.",style="#FFDA76")
                time.sleep(10)  

                # Clear the screen
                print("\033[H\033[J")  
                

                for attempt in range(2):  # allow two attempts
                    start_time = time.time()
                    user_input = input(f"Attempt {attempt + 1}: Please spell the word: ")
                    end_time = time.time()

                    time_taken = (end_time - start_time) / 60  
                    self.total_time += time_taken 

                    if user_input.lower() == random_word:
                        console.print("Correct! Great job! ",emojis.encode(":tada:"),style="#88C273")         
                        

                        self.correct_count += 1
                        break  
                    else:
                        if attempt < 1:  # only print on the first attempt
                            console.print(f"Oops! Try again.",emojis.encode(":thinking_face:"),style="#C62E2E")
                        else :
                            console.print(f"The Correct spell {random_word}",style="#D4BDAC")
                        
            else:
                console.print("No words found with that length and type. Please try again.",style="#C62E2E")
        print("\033[H\033[J") 
        console.print(f"\nTotal time taken for {self.attempts} words: {self.total_time:.2f} minutes",style="#FF8C9E")
        console.print(f"Correct attempts: {self.correct_count}/{self.attempts}",style="#FF8C9E")


