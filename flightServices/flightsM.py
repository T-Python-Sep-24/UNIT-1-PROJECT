import json
from datetime import datetime
from users import dataEmployee  # Import the Employee class
from users import dataCustomerOrTraveler

class FlightsManagement:
    def __init__(self, id_flight: int, date_flight: datetime, employee: dataEmployee.Employee):
        self.id_flight = id_flight
        self.date_flight = date_flight
        self.employee = employee  # Employee object
        self.keepDatafli = {}  # Dictionary to hold flight data


    def addFlight(self):
        # Only allow "manager" to add a flight
        if self.employee.position.lower() == "manager":
            if self.id_flight not in self.keepDatafli:
                # Add flight data to the keepDatafli dictionary
                self.keepDatafli[self.id_flight] = {
                    "id_flight": self.id_flight,
                    "date_flight": self.date_flight
                }
                return "Flight added successfully."
            else:
                return f"Flight with ID {self.id_flight} already exists."
        else:
            return "Permission denied. Only managers can add flights."


    def removeFlight(self):
        # Only allow "manager" to remove a flight
        if self.employee.position.lower() == "manager":
            if self.id_flight in self.keepDatafli:
                del self.keepDatafli[self.id_flight]
                return f"Flight with ID {self.id_flight} has been removed."
            else:
                return f"Flight with ID {self.id_flight} not found."
        else:
            return "Permission denied. Only managers can remove flights."

    
    def searchFlight(self):
        if self.id_flight in self.keepDatafli:
            return f"Flight found: {self.keepDatafli[self.id_flight]}"
        else:
            return f"Flight with ID {self.id_flight} not found."

    
    def saveDataFlight(self):
        # Save the keepDatafli dictionary to the JSON file
        with open("information.json", "a", encoding="UTF-8") as fileData:
            json_data = json.dumps(self.keepDatafli, indent=3)
            fileData.write(json_data + "\n")
        return "Flight data has been saved."

    
    def loadDataFlight(self):
        # Load flight data from the JSON file
        with open("information.json", "r", encoding="UTF-8") as fileData:
            loaded_data = json.load(fileData)
        return loaded_data


    def boardingPlane(self, traveler: dataCustomerOrTraveler.Traveler):
        # Only allow "manager" or "GM" to permit boarding and offer customer services
        if self.employee.position.lower() in ["manager", "gm" ,"services customer"]:
            # Traveler is boarding the plane
            return f"Traveler {traveler.name} with ID {traveler.id} is boarding Flight {self.id_flight}."
        else:
            return "Permission denied. Only managers or GMs can permit boarding and offer services."