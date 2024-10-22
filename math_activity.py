import random
import time
from emojis import emojis
from rich.console import Console

console = Console()

class mathActivity:

    def __init__(self):
        self.attempts = 5
        self.correct_count = 0
        self.total_time = 0

    def generate_question(self, difficulty):
        if difficulty == "1":
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
        elif difficulty == "2":
            num1 = random.randint(10, 50)
            num2 = random.randint(10, 50)
        elif difficulty == "3":
            num1 = random.randint(50, 100)
            num2 = random.randint(50, 100)
        return num1, num2

    def math_activity(self):
        console.print("Welcome to the Math Challenge!", style="#C8A1E0")

        while True:
            console.print(f"You will solve {self.attempts} equations.", style="#FFDA76")

            console.print('''Select difficulty level: 
                1. Easy
                2. Medium
                3. Hard
                4. Exit
            ''', style="#B4D6CD")

            choice = input("Enter the number for difficulty level (1, 2, 3, or 4): ").strip()
            print("\033[H\033[J")

            if choice == '4':
                console.print("Exiting the Math Challenge.", style="#C8A1E0")
                return

            if choice not in ['1', '2', '3']:
                console.print("Invalid difficulty level. Please try again.", style="#C62E2E")
                continue

            console.print('''Select operation: 
                1. Addition
                2. Subtraction
                3. Multiplication
                4. Division
            ''', style="#B4D6CD")

            operation_choice = input("Enter the number for operation (1, 2, 3, or 4): ").strip()
            print("\033[H\033[J")

            correct_count = 0
            total_time = 0

            for i in range(self.attempts):
                num1, num2 = self.generate_question(choice)

                if operation_choice == '1':
                    correct_answer = num1 + num2
                    operation = '+'
                elif operation_choice == '2':
                    correct_answer = num1 - num2
                    operation = '-'
                elif operation_choice == '3':
                    correct_answer = num1 * num2
                    operation = '*'
                elif operation_choice == '4':
                    if num2 == 0:
                        num2 = 1  # avoid division by zero
                    correct_answer = num1 / num2
                    operation = '/'
                else:
                    console.print("Invalid operation. Please try again.", style="#C62E2E")
                    return

                print(f"\nQuestion {i + 1}: What is {num1} {operation} {num2}?")
                start_time = time.time()

                for attempt in range(2):
                    user_answer = input(f"Attempt {attempt + 1}: Your answer: ")
                    end_time = time.time()

                    time_taken = (end_time - start_time) / 60
                    total_time += time_taken

                    if float(user_answer) == correct_answer:
                        console.print("Correct! Great job!",emojis.encode(":tada:"), style="#88C273")
                        correct_count += 1
                        break
                    else:
                        if attempt < 1:
                            console.print("Oops! Try again.",emojis.encode(":thinking_face:"), style="#C62E2E")
                        else:
                            console.print(f"The correct answer is: {correct_answer}", style="#D4BDAC")

            total_time_minutes = total_time
            console.print(f"\nTotal time taken for {self.attempts} questions: {total_time_minutes:.2f} minutes", style="#FF8C9E")
            console.print(f"Correct attempts: {correct_count}/{self.attempts}", style="#88C273")

            input("Press Enter to return to the math activity options...")
            print("\033[H\033[J")  # Clear the screen
