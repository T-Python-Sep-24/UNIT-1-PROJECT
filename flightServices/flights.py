
import json
from datetime import datetime
from users import dataEmployee
from users.dataCustomerOrTraveler import Traveler  
from flightServices import flightsM  

class Flight:
    def __init__(self,mainlist):
        self.mainlist = mainlist  
        self.flight_dict = self.mainlist[5]  
        self.reservations = {} 
        self.payments = {}  
    
    def searchFlight(self):
        origin = input("Enter the origin city: ")
        destination = input("Enter the destination city: ")
        route_key = f"{origin} to {destination}"
        available_flights = [flight_id for flight_id, flight_info in self.flight_dict.items()
                             if flight_info['origin'] == origin and flight_info['destination'] == destination]
        if available_flights:
            print(f"Available flights from {origin} to {destination}: {available_flights}")
        else:
            print(f"No flights found from {origin} to {destination}.")

    def reserveFlight(self, traveler:Traveler):
        flight_id = input("Enter the flight ID to reserve: ")
        if flight_id in self.flight_dict:
            self.reservations[traveler.id] = flight_id
            print(f"Traveler {traveler.name} has reserved flight {flight_id}.")
        else:
            print(f"Flight with ID {flight_id} not found.")

    def saveData(self):
        with open("reservations.json", "w", encoding="UTF-8") as fileData:
            json.dump(self.reservations, fileData, indent=4)
        print("Reservation data has been saved.")

        print("Reservations and payments have been saved.")

    def loadData(self):
        try:
            with open("reservations.json", "r", encoding="UTF-8") as fileData:
                self.reservations = json.load(fileData)
            print("Reservations have been loaded.")
        except FileNotFoundError:
            print("No reservation data found.")
