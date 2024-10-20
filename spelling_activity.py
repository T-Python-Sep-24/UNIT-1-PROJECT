import random
import time
from art import *  
from colorama import *
from nltk.corpus import words, wordnet

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

    def get_word_meaning(self,word):
        synsets = wordnet.synsets(word)
        if synsets:
            return synsets[0].definition()  
        return "Definition not available for this word."

    def spelling_activity(self):

        print("Welcome to the Spelling Challenge!")
        print(f"You will spell {self.attempts} words.")
        
        difficulty = input("Select difficulty level: easy, medium, or hard: ").strip().lower()
        if difficulty == "easy":
            letter_range = (3, 5)  
        elif difficulty == "medium":
            letter_range = (6, 8)  
        elif difficulty == "hard":
            letter_range = (9, 11)  
        else:
            print("Invalid difficulty level. Please restart the program.")
            return  

        
        pos_input = input("Select word type: noun, verb, adjective, adverb: ").strip().lower()
        Part_f_Speech = {
            'noun': wordnet.NOUN,
            'verb': wordnet.VERB,
            'adjective': wordnet.ADJ,
            'adverb': wordnet.ADV,
        
        }
        pos = Part_f_Speech.get(pos_input).strip().lower()

        if pos is None:
            print("Invalid word type. Please restart the program.")
            return  

        for a in range(self.attempts):
            letter_count = random.randint(*letter_range)  
            random_word = self.get_random_word(letter_count, pos)

            if random_word:
                print(f"Your word is: {random_word}")
                print(f"Meaning: {self.get_word_meaning(random_word)}")  
                time.sleep(25)  # Wait for 25 seconds
                
                # Clear the screen
                print("\033[H\033[J")  
                print("The word has disappeared. Please spell it now:")
                
                start_time = time.time()  
                user_input = input("Please spell the word: ")
                end_time = time.time() 

                
                time_taken = (end_time - start_time) / 60  
                self.total_time += time_taken 

                if user_input.lower() == random_word:
                    print("Correct! Great job!")
                    self.correct_count+=1
                else:
                    print(f"Oops! The correct spelling is: {random_word}")

            else:
                print("No words found with that length and type. Please try again.")

        print(f"\nTotal time taken for {self.attempts} words: {self.total_time:.2f} minutes")
        print(f"Correct attempts: {self.correct_count}/{self.attempts}")


