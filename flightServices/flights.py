
import json
from datetime import datetime
from users import dataEmployee
from users import dataCustomerOrTraveler  # Import the Traveler class
from flightServices import flightsM  # Import flightsM, which contains the keepDatafli dictionary

class Flight:
    def __init__(self):
        self.keepDatafli = flightsM.keepDatafli  # Use the external dictionary for flight data
        self.reservations = {}  # Dictionary to hold reservations
        self.payments = {}  # Dictionary to hold payment data

    def searchFlight(self):
        # Traveler searches for a flight
        origin = input("Enter the origin city: ")
        destination = input("Enter the destination city: ")
        route_key = f"{origin} to {destination}"

        # Search for flights matching the route
        available_flights = [flight_id for flight_id, flight_info in self.keepDatafli.items() if flight_info['route'] == route_key]

        if available_flights:
            print(f"Available flights from {origin} to {destination}: {available_flights}")
        else:
            print(f"No flights found from {origin} to {destination}.")

    def reserveFlight(self, traveler: dataCustomerOrTraveler.Traveler):
        flight_id = input("Enter the flight ID to reserve: ")

        if flight_id in self.keepDatafli:
            self.reservations[traveler.id] = flight_id
            print(f"Traveler {traveler.name} has reserved flight {flight_id}.")
        else:
            print(f"Flight with ID {flight_id} not found.")

    def makePayment(self, traveler: dataCustomerOrTraveler.Traveler):
        flight_id = self.reservations.get(traveler.id)

        if flight_id:
            amount = input(f"Enter payment amount for flight {flight_id}: ")
            self.payments[traveler.id] = {"flight_id": flight_id, "amount": amount}
            print(f"Payment of {amount} made for flight {flight_id} by traveler {traveler.name}.")
        else:
            print(f"No reservation found for traveler {traveler.name}.")

    def cancelFlight(self, traveler: dataCustomerOrTraveler.Traveler):
        flight_id = self.reservations.get(traveler.id)

        if flight_id:
            del self.reservations[traveler.id]
            print(f"Flight {flight_id} reservation for traveler {traveler.name} has been canceled.")
        else:
            print(f"No reservation found for traveler {traveler.name}.")

    def saveData(self):
        # Save reservations and payments to JSON file
        with open("reservations.json", "w", encoding="UTF-8") as fileData:
            json_reservations = json.dumps(self.reservations, indent=3)
            fileData.write(json_reservations)

        with open("payments.json", "w", encoding="UTF-8") as fileData:
            json_payments = json.dumps(self.payments, indent=3)
            fileData.write(json_payments)

        print("Reservations and payments have been saved.")

    def loadData(self):
        # Load reservations and payments from JSON file
        try:
            with open("reservations.json", "r", encoding="UTF-8") as fileData:
                self.reservations = json.load(fileData)
            with open("payments.json", "r", encoding="UTF-8") as fileData:
                self.payments = json.load(fileData)
            print("Reservations and payments have been loaded.")
        except FileNotFoundError:
            print("No reservations or payments found.")
