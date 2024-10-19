import random
import time
from nltk.corpus import words, wordnet


word_list = words.words()

def get_random_word(length, pos): 
    filtered_words = [word for word in word_list if len(word) == length]

    if pos:
        filtered_words = [word for word in filtered_words if wordnet.synsets(word, pos=pos)]
    return random.choice(filtered_words) if filtered_words else None

def get_word_meaning(word):
    synsets = wordnet.synsets(word)
    if synsets:
        return synsets[0].definition()  
    return "Definition not available for this word."

def spelling_activity():
    total_time = 0
    attempts = 5  # Number of words to spell

    print("Welcome to the Spelling Challenge!")
    print(f"You will spell {attempts} words.")
    
    
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
    pos = Part_f_Speech.get(pos_input)  

    if pos is None:
        print("Invalid word type. Please restart the program.")
        return  

    for _ in range(attempts):
        letter_count = random.randint(*letter_range)  #
        random_word = get_random_word(letter_count, pos)

        if random_word:
            print(f"Your word is: {random_word}")
            print(f"Meaning: {get_word_meaning(random_word)}")  
            time.sleep(25)  # Wait for 10 seconds
            
            # Clear the screen
            print("\033[H\033[J")  
            print("The word has disappeared. Please spell it now:")
            
            start_time = time.time()  
            user_input = input("Please spell the word: ")
            end_time = time.time() 

            
            time_taken = end_time - start_time
            total_time += time_taken

            if user_input.lower() == random_word:
                print("Correct! Great job!")
            else:
                print(f"Oops! The correct spelling is: {random_word}")

        else:
            print("No words found with that length and type. Please try again.")

    print(f"\nTotal time taken for {attempts} words: {total_time:.2f} seconds")


spelling_activity()
