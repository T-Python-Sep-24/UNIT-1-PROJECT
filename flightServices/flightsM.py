import json
from datetime import datetime
from users import dataEmployee  
from users import dataCustomerOrTraveler

class FlightsManagement:
    def __init__(self, mainlist) -> None:
        self.mainlist = mainlist
        self.flight_dict = self.mainlist[5]

    def add_flight(self):
        name = input("Enter your name: ")
        position = input("Enter your position: ")
        if position.lower() == "manager":
            flight_id = input("Enter flight ID: ")
            origin = input("Enter origin city: ")
            destination = input("Enter the destination city: ")
            route_key = f"{origin} to {destination}"           
            date_flight = datetime.today().strftime('%Y-%m-%d') 
            if flight_id not in self.flight_dict:
                self.flight_dict[flight_id] = {
                    "origin": origin,
                    "destination": destination,
                    "date": date_flight
            }
                self.saveDataFlight()
                return f"Flight with ID {flight_id} added successfully by {name} (Manager)."
            else:
                return f"Flight with ID {flight_id} already exists."
        else:
            return f"Permission denied. {name} is not a manager."
    
    def removeFlight(self):
        name = input("Enter your name: ")
        position = input("Enter your position: ")
        if position.lower() == "manager":
            flight_id = input("Enter flight ID to remove: ")
            if flight_id in self.flight_dict:
                del self.flight_dict[flight_id]
                self.saveDataFlight(show_message=False)
                return f"Flight with ID {flight_id} has been removed by {name} (Manager)."
            else:
                return f"Flight with ID {flight_id} not found."
        else:
            return f"Permission denied. {name} is not a manager."
    
    def searchFlight(self):
        flight_id = input("Enter flight ID to search: ")
        if flight_id in self.flight_dict:
            flight_info = self.flight_dict[flight_id]
            return f"Flight found: Origin: {flight_info['origin']}, Destination: {flight_info['destination']}, Date: {flight_info['date']}"
        else:
            return f"Flight with ID {flight_id} not found."

    def displayFlights(self):
        if self.flight_dict:
            for flight_id, flight_info in self.flight_dict.items():
                print(f"ID: {flight_id}, Origin: {flight_info['origin']}, Destination: {flight_info['destination']}, Date: {flight_info['date']}")
        else:
            print("No flight data found.")

    def boardingPlane(self):
        name = input("Enter your name (employee): ")
        employee_id = input("Enter your employee ID: ")
        employee_dict = self.mainlist[1]
        if employee_id in employee_dict:
            flight_id = input("Enter flight ID for boarding: ")
            if flight_id in self.flight_dict:
                flight_info = self.flight_dict[flight_id]
                print(f"{name} (Employee) is managing boarding for flight {flight_id} to {flight_info['destination']}.")
                print(f"Boarding started for Flight {flight_id}.")
                return f"Boarding process completed for flight {flight_id}."
            else:
                return f"Flight with ID {flight_id} not found."
        else:
            return f"Permission denied. {name} is not a registered employee."
    
    def saveDataFlight(self , show_message=True):
        with open("information.json", "w", encoding="UTF-8") as file:
            json.dump(self.mainlist, file, indent=4)
        if show_message:
            print("Flight data has been saved to 'information.json'.")
  
    def loadDataFlight(self):
        try:
            with open("information.json", "r", encoding="UTF-8") as file:
                loaded_data = json.load(file)
                self.flight_dict = loaded_data[5]  
                self.mainlist[5] = self.flight_dict  
                print("Flight data has been loaded.")
        except FileNotFoundError:
            print("No flight data file found.")
        except json.JSONDecodeError:
            print("Error decoding flight data from the file.")