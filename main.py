import time
from art import *
from datetime import datetime  
from colorama import *
from math_activity import mathActivity
from reading_and_writing_activity import Story
from spelling_activity import SpellingActivity

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
         #searching for a child by their ID
        try:
            with open('children.txt', 'r') as file:
                for line in file:
                    id, registered_name = line.strip().split(',')
                    if id == child_id:
                        child = Child(id, registered_name)  
                        print(f"Child found: ID: {child.child_id}, Name: {child.name}")
                       
                        Child.activity(child.child_id)
                        return child  
        except FileNotFoundError:
            return None
        return None

    
    def activity(child_id):
        #print the activity log for a child based on their ID
        print(f"\nActivity Log for Child ID: {child_id}\n")
        try:
            with open('activity_log.txt', 'r') as file:
                for line in file:
                    log_id, name, activity, time_spent, date = line.strip().split(',')
                    if log_id == child_id:
                        print(f"Activity: {activity}, time spent: {time_spent} minutes, Date: {date}")
        except FileNotFoundError:
            print("No activity log found.")

    def log_activity(self, activity, time_spent):
        #log activity details to a text file, including child's name and date
        with open('activity_log.txt', 'a') as file:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
            file.write(f"{self.child_id},{self.name},{activity},{time_spent},{date}\n") 

def register_child():
    #function to register a new child
    while True:
        child_id = input("Enter unique ID: ")
        if Child.id_exists(child_id):
            print("This ID already exists. Please choose a different ID.")
        else:
            name = input("Enter child's name: ")
            child = Child(child_id, name)
            child.save_data()  
            print("Child registered successfully!")
            break

def main():
    timeTotal = 0
    print(text2art("Welcome to the ...... for Kids "))

    while True:
        print(text2art('''      
               Choose an option: 
               1. Register Child
               2. Login Child
               3. Search Child by ID
               4. Exit
        ''', font ='straight'))
        choice = input(text2art("Choose number 1 - 4: ", font='straight'))

        if choice == '1':
            register_child()  

        elif choice == '2':
            child_id = input("Enter ID: ")
            name = input("Enter name: ")
            child = Child.get_child(name, child_id) 
            if child:  
                print(f"Welcome, {child.name}!") 

                while True:
                    print(text2art('''      
                           Choose the activity you would like to do: 
                           1. Spelling Activity
                           2. Reading And Writing Activity
                           3. Math Activity 
                           4. Exit
                    ''', font ='straight'))
                    activity_choice = input(text2art("Choose number 1 - 4: ", font='straight'))

                    if activity_choice == '1':
                        start_time = time.time()
                        spelling_activity = SpellingActivity()
                        spelling_activity.spelling_activity()
                        end_time = time.time()

                        total = (end_time - start_time) / 60
                        timeTotal += total
                        print(f"You took {total:.2f} minutes in this activity.")
                        child.log_activity("Spelling Activity", total)  

                    elif activity_choice == '2':
                        start_time = time.time()
                        read_write = Story()
                        read_write.read_write() 
                        end_time = time.time()

                        total = (end_time - start_time) / 60
                        timeTotal += total
                        print(f"You took {total:.2f} minutes in this activity.")
                        child.log_activity("Reading and Writing Activity", total)  

                    elif activity_choice == '3':
                        start_time = time.time()
                        operation = mathActivity()
                        operation.math_activity()
                        end_time = time.time()

                        total = (end_time - start_time) / 60
                        timeTotal += total
                        print(f"You took {total:.2f} minutes in this activity.")
                        child.log_activity("Math Activity", total)  
                        
                    elif activity_choice == '4':
                        print("Thank you for using the app! Goodbye!")
                        return

                    else:
                        print("Invalid choice. Please select a valid number.")
            else:
                print("Login failed. Please check the ID and name.")

        elif choice == '3':
            child_id = input("Enter the ID of the child to search: ")
            child = Child.search_by_id(child_id) 

        elif choice == '4':
            print("Thank you for using the app! Goodbye!")
            break  

        else:
            print("Invalid choice. Please select a valid number.")

main()
