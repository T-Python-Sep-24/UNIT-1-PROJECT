import json
import os
from colorama import Fore, Back,Style  
from users.dataEmployee import Employee
from users.dataCustomerOrTraveler import Traveler
from flightServices.flightsM import FlightsManagement

mainlist = ["employee", {}, "traveler", {}, "flight management", {}]

def save_all_data():
    with open('information.json', 'w', encoding='UTF-8') as file:
        json.dump(mainlist, file, indent=4)

def load_all_data():
    global mainlist
    try:
        if os.path.exists('information.json') and os.path.getsize('information.json') == 0:
            raise ValueError("The file is empty.")
        with open('information.json', 'r', encoding='UTF-8') as file:
            mainlist = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        mainlist = ["employee", {}, "traveler", {}, "flight management", {}]

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

text = "Tuwaiq Airport"
print(text)

def main_menu():
    print("1. Manage Employees\n2. Manage Travelers\n3. Manage Flights\n4. Exit")

def employee_menu():
    print("1. Add Employee\n2. Remove Employee\n3. Search Employee\n4. Save Employee Data\n5. Load Employee Data\n6. Display Employee Data\n7. Back")

def traveler_menu():
    print("1. Add Traveler\n2. Remove Traveler\n3. Search Traveler\n4. Save Traveler Data\n5. Load Traveler Data\n6. Display Traveler Data\n7. Back")

def flight_menu():
    print("1. Add Flight (Manager Only)\n2. Reserve Flight\n3. Search Flight\n4. Save Flight Data\n5. Load Flight Data\n6. Back")

load_all_data()


while True:
    main_menu()
    choice = get_int_input("Select an option: ")

    if choice == 1:  
        while True:
            employee_menu()
            emp_choice = get_int_input("Select an option: ")
            if emp_choice == 1:  # Add Employee
                name = input("Enter name: ")
                employee_id = get_int_input("Enter ID: ")
                email = input("Enter email: ")
                phone = input("Enter phone number: ")
                position = input("Enter position: ")

                # Create an Employee object and add data
                employee1 = Employee(mainlist, name, employee_id, email, phone, position)
                print(employee1.add_data())

            elif emp_choice == 2:  # Remove Employee
                employee1 = Employee(mainlist, "", "", "", "", "")
                print(employee1.remove_data()) 
            
            elif emp_choice == 3:  # SearchEmployee
                print(employee1.search_data())
            
            elif emp_choice == 4:  # Save Employee Data
                employee1.save_data()
            
            elif emp_choice == 5:  # Load Employee Data
                employee1.load_data()

            elif emp_choice == 6:  # Display Employee Data
                employee = Employee(mainlist, "", "", "", "", "")
                employee.display_data()  
            
            elif emp_choice == 7:  # Back to Main Menu
                break

    elif choice == 2:  # Traveler management
        while True:
            traveler_menu()
            trav_choice = get_int_input("Select an option: ")

            if trav_choice == 1:  # Add Traveler
                name = input("Enter name: ")
                traveler_id = get_int_input("Enter traveler ID: ")
                email = input("Enter email: ")
                phone = input("Enter phone number: ")
                birth_date = input("Enter birth date (YYYY-MM-DD): ")

                # Create a Traveler object and add data
                traveler1 = Traveler(mainlist, name, traveler_id, email, phone, birth_date)
                print(traveler1.addDatatra())
            elif trav_choice == 2:  # Remove Traveler
                traveler1= Traveler(mainlist, "", "", "", "", "")
                print(traveler1.removeDdatatra())
            
            elif trav_choice == 3:  # Search Traveler
                traveler1 = Traveler(mainlist, "", "", "", "", "")
                print(traveler1.searchDatatra())

            elif trav_choice == 4:  # Save Traveler Data
                traveler1.saveDatatra()

            elif trav_choice == 5:  # Load Traveler Data
               traveler1.load_datatra()


            elif trav_choice == 6:  # Display Traveler Data
                traveler1 = Traveler(mainlist, "", "", "", "", "")
                traveler1.displayDatatra()    

            elif trav_choice == 7:  # Back to Main Menu
                break

    elif choice == 3:  # Flight management
        while True:
            flight_menu()
            flight_choice = get_int_input("Select an option: ")

            if flight_choice == 1:  # Add Flight (Manager Only)
                flight_management = FlightsManagement(mainlist)
                print(flight_management.add_flight())
            
            elif flight_choice == 2:  # Remove Flight (Manager Only)
                flight_management = FlightsManagement(mainlist)
                print(flight_management.removeFlight())

            elif flight_choice == 3:  # Search Flight
                flight_management = FlightsManagement(mainlist)
                print(flight_management.searchFlight())
            
            elif flight_choice == 4:  # Save Flight Data
                save_all_data()
            
            elif flight_choice == 5:  # Load Flight Data
                load_all_data()
                
            elif flight_choice == 6:  # Back to Main Menu
                break
    elif choice == 4:  # Exit
        # save_all_data()  # Save all data before exiting
        print("Exiting the system. Goodbye!")
        break