import time
from emojis import emojis
from art import *
from colorama import *
from datetime import datetime  
from rich.console import Console
from rich.table import Table
from math_activity import mathActivity
from reading_and_writing_activity import Story
from spelling_activity import SpellingActivity
console = Console()

class Child:
    def __init__(self, child_id, name):

        self.child_id = child_id
        self.name = name

    def save_data(self):
        #saving child's data to a text file
        with open('children.txt', 'a') as file:
            file.write(f"{self.child_id},{self.name}\n")

    
    def id_exists(child_id):
        #checking if the child ID already exists in the file
        try:
            with open('children.txt', 'r') as file:
                for line in file:
                    id, _ = line.strip().split(',')
                    if id == child_id:
                        return True
        except FileNotFoundError:
            return False
        return False
    
    def get_child(name, child_id):
        #retrieving child's information using their name and ID
        try:
            with open('children.txt', 'r') as file:
                for line in file:
                    id, registered_name = line.strip().split(',')
                    if id == child_id and registered_name == name:
                        return Child(id, registered_name)  
        except FileNotFoundError:
            return None
        return None

   
    def search_by_id(child_id):
         # Searching for a child by their ID
        try:
            with open('children.txt', 'r') as file:
                for line in file:
                    id, registered_name = line.strip().split(',')
                    if id == child_id:
                        child = Child(id, registered_name) 
                        console.print(f"Child found: ID: {child.child_id}, Name: {child.name}",style="#FF8C9E")
                        Child.activity(child.child_id)
                        return child  
        except FileNotFoundError:
            return None
        return None

    def activity(child_id):
        console.print(f"\nActivity Log for Child ID: {child_id}\n", style="#FFECC8")
        try:
            with open('activity_log.txt', 'r') as file:
                found_activity = False
                table = Table(title="Child Activity Log", title_style="#C8A1E0", border_style="#674188")

                table.add_column("Activity")
                table.add_column("Time Spent (minutes)")
                table.add_column("Date")

                for line in file:
                    log_id, name, activity, time_spent, date = line.strip().split(',')
                    if log_id == child_id:
                        found_activity = True
                        time_spent = round(float(time_spent), 2)  

                        table.add_row(activity,f"{time_spent:.2f}", date)

                if found_activity:
                    console.print(table)
                    console.print("Data retrieved successfully.", style="#3EB489")
                    input("Press enter to return.")
                    print("\033[H\033[J") 

                else:
                    console.print("No activities found for this child ID.", style="#C62E2E")

        except FileNotFoundError:
            console.print("No activity log found.", style="#C62E2E")

    def log_activity(self, activity, time_spent):

        with open('activity_log.txt', 'a') as file:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
            file.write(f"{self.child_id},{self.name},{activity},{time_spent:.2f},{date}\n") 

def register_child():
    while True:
        child_id = input(Fore.WHITE + "Enter unique ID (10 digits): " + Fore.RESET)
        if len(child_id) != 10 or not child_id.isdigit():
            console.print("ID must be exactly 10 digits. Please try again.", style="#C62E2E")
            continue
        
        if Child.id_exists(child_id):
            console.print("This ID already exists. Please choose a different ID.", style="#C62E2E")
        else:
            name = input("Enter child's name (letters only): ")
            if not name.isalpha():
                console.print("Name must contain letters only. Please try again.", style="#C62E2E")
                continue
            
            child = Child(child_id, name)
            child.save_data()
            print("\033[H\033[J") 
            console.print("Child registered successfully!", style="#88C273")
            break


def main():
    timeTotal = 0
    console.print("")

    while True:
        console.print("ــــــWelcome to Bright mindsــــــ  " , style=("blink #C8A1E0" ))
        emojis.encode(":thinking_face:")
        

        
        console.print('''      
               Choose an option: 
               1. Register Child 
               2. Login Child
               3. Search Child by ID
               4. Exit
        ''',style="#B4D6CD")
        choice = input(Fore.WHITE+"Choose number 1 - 4: "+Fore.RESET)
        # Clear the screen
        print("\033[H\033[J") 

        if choice == '1':
            console.print("ــــــWelcome to Bright mindsــــــ  " , style=("blink #C8A1E0" ))
            register_child()  

        elif choice == '2':
            console.print("ــــــWelcome to Bright mindsــــــ  " , style=("blink #C8A1E0" ))
            child_id = input("Enter ID: ")
            name = input("Enter name: ")
            print("\033[H\033[J") 
            child = Child.get_child(name, child_id) 
            if child:  
                console.print(f"Welcome, {child.name}!",style="#C8A1E0") 

                while True:
                    console.print('''      
                Choose the activity you would like to do: 
                1. Spelling Activity 
                2. Reading And Writing Activity
                3. Math Activity 
                4. Exit
                    ''',style="#B4D6CD")
                    activity_choice = input("Choose number 1 - 4: ")

                    if activity_choice == '1':
                        start_time = time.time()
                        # Clear the screen
                        print("\033[H\033[J") 
                        spelling_activity = SpellingActivity()
                        spelling_activity.spelling_activity()
                        end_time = time.time()

                        total = (end_time - start_time) / 60
                        timeTotal += total
                        console.print(f"You took {timeTotal:.2f} minutes in this activity.",style="#FFF1DB")
                        child.log_activity("Spelling Activity", total)  

                    elif activity_choice == '2':
                        start_time = time.time()
                        # Clear the screen
                        print("\033[H\033[J") 
                        read_write = Story()
                        read_write.read_write() 
                        end_time = time.time()

                        total = (end_time - start_time) / 60
                        timeTotal += total
                        console.print(f"You took {timeTotal:.2f} minutes in this activity.",style="#FFF1DB")
                        child.log_activity("Reading and Writing Activity", total)  

                    elif activity_choice == '3':
                        start_time = time.time()
                        # Clear the screen
                        print("\033[H\033[J") 
                        operation = mathActivity()
                        operation.math_activity()
                        end_time = time.time()

                        total = (end_time - start_time) / 60
                        timeTotal += total
                        console.print(f"You took {float(timeTotal):.2f} minutes in this activity.", style="#FFF1DB")
                        child.log_activity("Math Activity", total)  
                        
                    elif activity_choice == '4':
                        # Clear the screen
                        print("\033[H\033[J") 
                        console.print("Thank you for using the app! Goodbye!",style="#C8A1E0")
                        break

                    else:
                        console.print("Invalid choice. Please select a valid number.",style="#C62E2E")
            else:
                console.print("Login failed. Please check the ID and name.",style="#C62E2E")

        elif choice == '3': 
            # Clear the screen
            print("\033[H\033[J") 
            console.print("ــــــWelcome to the Bright mindsــــــ  " , style=("blink #C8A1E0" ))
            child_id = input("Enter the ID of the child to search: ")
            child = Child.search_by_id(child_id) 

        elif choice == '4':
            # Clear the screen
            print("\033[H\033[J") 
            console.print("Thank you for using the ...! Goodbye!",style="#C8A1E0")
            break  

        else:
            console.print("Invalid choice. Please select a valid number.",style="#C62E2E")

main()
