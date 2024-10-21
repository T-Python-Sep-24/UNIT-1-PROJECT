import random
import time

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
        print("Welcome to the Math Challenge!")
        print(f"You will solve {self.attempts} equations.")
        
        print('''Select difficulty level: 
                1. Easy
                2. Medium
                3. Hard
        ''')
        
        choice = input("Enter the number for difficulty level (1, 2, or 3): ").strip()

        if choice not in ['1', '2', '3']:
            print("Invalid difficulty level. Please restart the program.")
            return

        print('''Select operation: 
                1. Addition
                2. Subtraction
                3. Multiplication
                4. Division
        ''')

        operation_choice = input("Enter the number for operation (1, 2, 3, or 4): ").strip()

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
                    num2 = 1  #avoid division by zero
                correct_answer = num1 / num2
                operation = '/'
            else:
                print("Invalid operation. Please restart the program.")
                return

            print(f"\nQuestion {i + 1}: What is {num1} {operation} {num2}?")
            start_time = time.time()

            for attempt in range(2):
                user_answer = input(f"Attempt {attempt + 1}: Your answer: ")
                end_time = time.time()

                time_taken = (end_time - start_time) / 60
                self.total_time += time_taken

                if float(user_answer) == correct_answer:
                    print("Correct! Great job!")
                    self.correct_count += 1
                    break
                else:
                    if attempt < 1:
                        print("Oops! Try again.")
                    else:
                        print(f"The correct answer is: {correct_answer}")

        total_time_minutes = self.total_time
        print(f"\nTotal time taken for {self.attempts} questions: {total_time_minutes:.2f} minutes")
        print(f"Correct attempts: {self.correct_count}/{self.attempts}")


