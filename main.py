from reading_and_writing_activity import Story
from spelling_activity import SpellingActivity
from art import *  
from colorama import *


def main():

    print(text2art("Welcome to the  ...... for Kids "))

    while True:
        print(text2art('''      
               Choose the activity you would like to do: 
                                    
               1. Spelling Activity
               2. Reading And Writing Activity
               3. Exit
        ''', font ='straight'))
        choose = input(text2art("Choose number 1 - 3: ",font='straight'))

        if choose == '1':
            spelling_activity = SpellingActivity()
            spelling_activity.spelling_activity()

        elif choose == '2':
            read_write = Story()
            read_write.read_write() 

        elif choose == '3':
            print("Thank you for using the ... . Goodbye!")
            break  

        else:
            print("Invalid choice. Please select a valid number.")

main()