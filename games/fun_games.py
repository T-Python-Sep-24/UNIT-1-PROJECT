# games/fun_games.py

import random

def math_quiz():
    print("Math Quiz: What is 7 + 3?")
    answer = input("Your answer: ")
    if answer == '10':
        print("Correct! You nailed it!")
    else:
        print("Oops! The correct answer was 10.")

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    number = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))
    
    if guess == number:
        print("Amazing! You guessed the correct number!")
    else:
        print(f"Close, but the correct number was {number}.")

def word_scramble():
    words = ["happiness", "mindfulness", "relaxation", "gratitude", "creativity"]
    word = random.choice(words)
    scrambled = ''.join(random.sample(word, len(word)))
    
    print(f"Unscramble this word: {scrambled}")
    guess = input("Your guess: ")
    
    if guess == word:
        print("Correct! You unscrambled it!")
    else:
        print(f"Nice try! The correct word was {word}.")

def play_game():
    print("🎮 Choose a fun game:")
    print("1. Math Quiz")
    print("2. Guess the Number")
    print("3. Word Scramble")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        math_quiz()
    elif choice == '2':
        guess_the_number()
    elif choice == '3':
        word_scramble()
    else:
        print("Invalid choice, please select a game.")
