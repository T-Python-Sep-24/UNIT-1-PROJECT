import random

def play_guessing_game():
    """A simple number guessing game."""
    print("🎲 Let's play a number guessing game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("📉 Too low! Try again.")
            elif guess > number_to_guess:
                print("📈 Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("❌ Please enter a valid number.")

def play_trivia_game():
    """A simple trivia quiz game."""
    print("🧠 Welcome to the trivia quiz!")
    questions = {
        "What is the capital of France?": "Paris",
        "What is 2 + 2?": "4",
        "What is the largest ocean on Earth?": "Pacific",
        "Who wrote 'Romeo and Juliet'?": "Shakespeare",
        "What is the chemical symbol for water?": "H2O",
        "What planet is known as the Red Planet?": "Mars",
        "What is the tallest mountain in the world?": "Mount Everest",
        "What is the smallest prime number?": "2",
        "In which year did the Titanic sink?": "1912",
        "What is the hardest natural substance on Earth?": "Diamond"
    }

    score = 0
    total_questions = len(questions)

    for question, answer in questions.items():
        user_answer = input(f"{question} ")
        if user_answer.strip().title() == answer:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer is: {answer}")

    print(f"\n🎉 Quiz Over! Your score: {score}/{total_questions}")
    percentage = (score / total_questions) * 100
    if percentage == 100:
        print("🌟 Perfect score! You're a trivia master!")
    elif percentage >= 70:
        print("👍 Great job! You have a good grasp of trivia.")
    elif percentage >= 50:
        print("🤔 Not bad, but there's room for improvement!")
    else:
        print("😞 Keep trying! Practice makes perfect!")

def play_word_scramble():
    """A simple word scramble game."""
    print("🔤 Let's play a word scramble game!")
    words = ["python", "programming", "emotions", "development", "adventure", "challenge", "creativity", "imagination"]
    word_to_scramble = random.choice(words)
    scrambled_word = ''.join(random.sample(word_to_scramble, len(word_to_scramble)))

    print(f"Scrambled word: {scrambled_word}")
    user_guess = input("Guess the word: ")

    if user_guess.lower() == word_to_scramble:
        print("🎉 Correct! Well done!")
    else:
        print(f"❌ Wrong! The correct word was '{word_to_scramble}'.")

def play_riddles():
    """A simple riddle game."""
    print("🧩 Let's solve some riddles!")
    riddles = {
        "What has keys but can't open locks?": "Piano",
        "What has to be broken before you can use it?": "Egg",
        "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?": "Echo",
        "What can travel around the world while staying in a corner?": "Stamp",
        "What begins with T, ends with T, and has T in it?": "Teapot"
    }

    score = 0
    total_riddles = len(riddles)

    for riddle, answer in riddles.items():
        user_answer = input(f"{riddle} ")
        if user_answer.strip().title() == answer:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer is: {answer}")

    print(f"\n🎉 Riddle Game Over! Your score: {score}/{total_riddles}")

def play_game():
    """Main game menu for users to choose a game."""
    print("🎮 Choose a game to play:")
    print("1️⃣ Guessing Game")
    print("2️⃣ Trivia Quiz")
    print("3️⃣ Word Scramble")
    print("4️⃣ Riddle Game")
    
    while True:
        choice = input("Select an option (1-4): ")

        if choice == '1':
            play_guessing_game()
            break
        elif choice == '2':
            play_trivia_game()
            break
        elif choice == '3':
            play_word_scramble()
            break
        elif choice == '4':
            play_riddles()
            break
        else:
            print("❌ Invalid choice. Please select a valid game.")