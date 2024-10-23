import json
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

class Hotel:
    def __init__(self, name, location, rating, price_per_room, room_availability):
        self.name = name
        self.location = location
        self.rating = rating
        self.price_per_room = price_per_room
        self.room_availability = room_availability

    def __repr__(self):
        return f"{self.name} - {self.location} | Rating: {self.rating} | Price: ${self.price_per_room} | Rooms Available: {self.room_availability}"

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "rating": self.rating,
            "price_per_room": self.price_per_room,
            "room_availability": self.room_availability
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

class User:
    def __init__(self, username):
        self.username = username

class Customer(User):
    def __init__(self, username):
        super().__init__(username)
        self.bookings = []

    def add_booking(self, hotel):
        self.bookings.append(hotel)

    def remove_booking(self, hotel):
        if hotel in self.bookings:
            self.bookings.remove(hotel)

    def view_bookings(self):
        return self.bookings

class Manager(User):
    def __init__(self, username):
        super().__init__(username)

    def add_hotel(self, hms, hotel):
        hms.add_hotel(hotel)

class HotelManagementSystem:
    def __init__(self):
        self.hotels = []
        self.users = {}
        self.manager_username = "manager"
        self.manager_password = "password123"
        self.load_hotels()  # Load existing hotels on initialization

    def add_hotel(self, hotel):
        self.hotels.append(hotel)
        self.save_hotels()  # Save after adding a hotel

    def view_hotels(self):
        for hotel in self.hotels:
            print(hotel)

    def search_hotel(self, name=None, location=None):
        found = False
        for hotel in self.hotels:
            if (name and name.lower() in hotel.name.lower()) or (location and location.lower() in hotel.location.lower()):
                print(hotel)
                found = True
        if not found:
            print("No hotels found.")

    def recommend_hotels(self, username):
        user = self.users.get(username)
        if user and user.view_bookings():
            booked_locations = {hotel.location for hotel in user.view_bookings()}
            recommendations = [hotel for hotel in self.hotels if hotel.location in booked_locations and hotel not in user.view_bookings()]
            if recommendations:
                print("\nRecommended Hotels based on your booking history:")
                for hotel in recommendations:
                    print(hotel)
            else:
                print("No recommendations available based on your booking history.")
        else:
            print("No booking history to base recommendations on.")

    def book_hotel(self, username, hotel_name):
        user = self.users.get(username, Customer(username))
        if username not in self.users:
            self.users[username] = user

        hotel = next((h for h in self.hotels if h.name == hotel_name), None)
        if hotel:
            if hotel.room_availability > 0:
                user.add_booking(hotel)
                hotel.room_availability -= 1
                print(f"Booking confirmed for {hotel.name}!")
                self.save_hotels()  # Save after booking
            else:
                print(f"Sorry, no rooms available for {hotel.name}.")
        else:
            print("Hotel not found.")

    def remove_booking(self, username, hotel_name):
        user = self.users.get(username)
        if user:
            hotel = next((h for h in self.hotels if h.name == hotel_name), None)
            if hotel:
                user.remove_booking(hotel)
                hotel.room_availability += 1
                print(f"Booking for {hotel.name} has been removed.")
                self.save_hotels()  # Save after removing booking
            else:
                print("Hotel not found.")

    def list_user_bookings(self, username):
        user = self.users.get(username)
        if user:
            bookings = user.view_bookings()
            if bookings:
                print(f"{username}'s Bookings:")
                for booking in bookings:
                    print(booking)
            else:
                print(f"No bookings for {username}.")

    def checkout(self, username):
        user = self.users.get(username)
        if user:
            total_cost = sum(hotel.price_per_room for hotel in user.view_bookings())
            booked_hotels = user.view_bookings()

            print(f"Total cost for {username}: ${total_cost}.")
            address = input("Enter your address: ")

            # Generating the receipt
            receipt_content = f"Receipt for {username}\n"
            receipt_content += f"Address: {address}\n"
            receipt_content += "Booked Hotels:\n"
            for hotel in booked_hotels:
                receipt_content += f"- {hotel.name} at {hotel.location}: ${hotel.price_per_room} each\n"
            receipt_content += f"Total Cost: ${total_cost}\n"
            receipt_content += "Thank you for your booking!\n"

            # Print receipt to console
            print("\nReceipt:")
            print(receipt_content)

            # Save receipt to a text file
            try:
                with open(f"{username}_receipt.txt", "w") as file:
                    file.write(receipt_content)
                print(f"Receipt saved as {username}_receipt.txt")
            except IOError:
                print("Error saving the receipt. Please try again.")

            # Clear bookings after checkout
            user.bookings.clear()
            self.save_hotels()  # Save after checkout
        else:
            print("User not found.")

    def load_hotels(self):
        try:
            with open("hotels.json", "r") as file:
                hotel_data = json.load(file)
                self.hotels = [Hotel.from_dict(data) for data in hotel_data]
                print("Hotels loaded successfully.")
        except (FileNotFoundError, json.JSONDecodeError):
            print("No hotel data found or error in data. Starting fresh.")
            # Add sample hotels if no data exists
            self.hotels = [
                Hotel("Hotel A", "New York", 4.5, 150, 10),
                Hotel("Hotel B", "Los Angeles", 4.0, 200, 5),
                Hotel("Hotel C", "Chicago", 3.5, 100, 8),
                Hotel("Hotel D", "New York", 4.2, 180, 6),
                Hotel("Hotel E", "Los Angeles", 4.3, 220, 4),
            ]

    def save_hotels(self):
        try:
            with open("hotels.json", "w") as file:
                json.dump([hotel.to_dict() for hotel in self.hotels], file, indent=4)
            print("Hotels saved successfully.")
        except IOError:
            print("Error saving hotel data. Please try again.")

    def get_float(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Please enter a valid number.")

    def get_int(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Please enter a valid integer.")

