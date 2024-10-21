# from users.identfyPerson import Person
from users.dataEmployee import Employee
from users.dataCustomerOrTraveler import Traveler
from flightServices.flightsM import FlightsManagement
from flightServices.flights import Flight

# Function to display main menu
def main_menu():
    print("Welcome to the Airport System!")
    print("1. Manage Employees")
    print("2. Manage Travelers")
    print("3. Manage Flights")
    print("4. Exit")

# Function to display employee menu
def employee_menu():
    print("Employee Menu")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Search Employee")
    print("4. Save Employee Data")
    print("5. Load Employee Data")
    print("6. Display Employee Data")
    print("7. Back to Main Menu")

# Function to display traveler menu
def traveler_menu():
    print("Traveler Menu")
    print("1. Add Traveler")
    print("2. Remove Traveler")
    print("3. Search Traveler")
    print("4. Save Traveler Data")
    print("5. Load Traveler Data")
    print("6. Display Traveler Data")
    print("7. Back to Main Menu")

# Function to display flight menu
def flight_menu():
    print("Flight Management")
    print("1. Add Flight (Manager Only)")
    print("2. Search Flight")
    print("3. Reserve Flight")
    print("4. Make Payment")
    print("5. Cancel Reservation")
    print("6. Save Flight Data")
    print("7. Load Flight Data")
    print("8. Back to Main Menu")

# Initialize flight management
flight_management = FlightsManagement()

# Main loop for interacting with the system
while True:
    main_menu()
    choice = input("Select an option: ")

    if choice == '1':  # Employee management
        while True:
            employee_menu()
            emp_choice = input("Select an option: ")
            if emp_choice == '1':  # Add Employee
                name = input("Enter name: ")
                employee_id = input("Enter ID: ")
                email = input("Enter email: ")
                phone = input("Enter phone number: ")
                position = input("Enter position: ")
                employee = Employee(name, employee_id, email, phone, position)
                print(employee.add_data())
            elif emp_choice == '2':  # Remove Employee
                print(employee.remove_data())
            elif emp_choice == '3':  # Search Employee
                print(employee.search_data())
            elif emp_choice == '4':  # Save Employee Data
                employee.save_data()
            elif emp_choice == '5':  # Load Employee Data
                print(employee.load_data())
            elif emp_choice == '6':  # Display Employee Data
                employee.display_data(employee.load_data())
            elif emp_choice == '7':  # Back to Main Menu
                break

    elif choice == '2':  # Traveler management
        while True:
            traveler_menu()
            trav_choice = input("Select an option: ")
            if trav_choice == '1':  # Add Traveler
                name = input("Enter name: ")
                traveler_id = input("Enter traveler ID: ")
                email = input("Enter email: ")
                phone = input("Enter phone number: ")
                birth_date = input("Enter birth date (YYYY-MM-DD): ")
                traveler = Traveler(name, traveler_id, email, phone, birth_date)
                print(traveler.addData())
            elif trav_choice == '2':  # Remove Traveler
                print(traveler.removeData())
            elif trav_choice == '3':  # Search Traveler
                print(traveler.searchData())
            elif trav_choice == '4':  # Save Traveler Data
                traveler.saveData()
            elif trav_choice == '5':  # Load Traveler Data
                print(traveler.loadData())
            elif trav_choice == '6':  # Display Traveler Data
                traveler.displayData(traveler.loadData())
            elif trav_choice == '7':  # Back to Main Menu
                break

    elif choice == '3':  # Flight management
        while True:
            flight_menu()
            flight_choice = input("Select an option: ")
            if flight_choice == '1':  # Add Flight (Manager Only)
                employee = Employee(input("Enter manager name: "), input("Enter manager ID: "),
                                    input("Enter email: "), input("Enter phone: "), "manager")
                flight_management.addFlight(employee)
            elif flight_choice == '2':  # Search Flight
                flight_management.searchFlight()
            elif flight_choice == '3':  # Reserve Flight
                traveler = Traveler(input("Enter traveler name: "), input("Enter traveler ID: "),
                                    input("Enter email: "), input("Enter phone: "), input("Enter birth date: "))
                flight_management.reserveFlight(traveler)
            elif flight_choice == '4':  # Make Payment
                traveler = Traveler(input("Enter traveler name: "), input("Enter traveler ID: "),
                                    input("Enter email: "), input("Enter phone: "), input("Enter birth date: "))
                flight_management.makePayment(traveler)
            elif flight_choice == '5':  # Cancel Reservation
                traveler = Traveler(input("Enter traveler name: "), input("Enter traveler ID: "),
                                    input("Enter email: "), input("Enter phone: "), input("Enter birth date: "))
                flight_management.cancelFlight(traveler)
            elif flight_choice == '6':  # Save Flight Data
                flight_management.saveData()
            elif flight_choice == '7':  # Load Flight Data
                flight_management.loadData()
            elif flight_choice == '8':  # Back to Main Menu
                break

    elif choice == '4':  # Exit
        print("Exiting the system. Goodbye!")
        break
