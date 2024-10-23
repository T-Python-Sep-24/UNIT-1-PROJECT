import json
from datetime import datetime
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

class Hotel:
    def __init__(self, name, location, rating, price_per_room, room_availability, room_type):
        self.name = name
        self.location = location
        self.rating = rating
        self.price_per_room = price_per_room
        self.room_availability = room_availability
        self.room_type = room_type  # e.g., "single", "double"

    def __repr__(self):
        return (f"{self.name} - {self.location} | Rating: {self.rating} | "
                f"Price: ${self.price_per_room} | Rooms Available: {self.room_availability} | "
                f"Type: {self.room_type}")

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "rating": self.rating,
            "price_per_room": self.price_per_room,
            "room_availability": self.room_availability,
            "room_type": self.room_type
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

    def add_booking(self, hotel, start_date, end_date):
        self.bookings.append((hotel, start_date, end_date))

    def remove_booking(self, hotel):
        self.bookings = [(h, start, end) for h, start, end in self.bookings if h != hotel]

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
            booked_locations = {hotel[0].location for hotel in user.view_bookings()}
            recommendations = [hotel for hotel in self.hotels if hotel.location in booked_locations and hotel not in [b[0] for b in user.view_bookings()]]
            if recommendations:
                print("\nRecommended Hotels based on your booking history:")
                for hotel in recommendations:
                    print(hotel)
            else:
                print("No recommendations available based on your booking history.")
        else:
            print("No booking history to base recommendations on.")

    def book_hotel(self, username, hotel_name, room_type, start_date, end_date):
        user = self.users.get(username, Customer(username))
        if username not in self.users:
            self.users[username] = user

        hotel = next((h for h in self.hotels if h.name == hotel_name and h.room_type == room_type), None)
        if hotel:
            if hotel.room_availability > 0:
                user.add_booking(hotel, start_date, end_date)
                hotel.room_availability -= 1
                print(f"Booking confirmed for {hotel.name} from {start_date} to {end_date}!")
                self.save_hotels()  # Save after booking
            else:
                print(f"Sorry, no rooms available for {hotel.name}.")
        else:
            print("Hotel not found or room type not available.")

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
                for hotel, start, end in bookings:
                    print(f"{hotel} from {start} to {end}")
            else:
                print(f"No bookings for {username}.")

    def checkout(self, username):
        user = self.users.get(username)
        if user:
            total_cost = 0
            booked_hotels = user.view_bookings()

            for hotel, start, end in booked_hotels:
                num_days = (datetime.strptime(end, "%Y-%m-%d") - datetime.strptime(start, "%Y-%m-%d")).days
                total_cost += hotel.price_per_room * num_days

            print(f"Total cost for {username}: ${total_cost}.")
            address = input("Enter your address: ")

            # Generating the receipt
            receipt_content = f"Receipt for {username}\n"
            receipt_content += f"Address: {address}\n"
            receipt_content += "Booked Hotels:\n"
            for hotel, start, end in booked_hotels:
                num_days = (datetime.strptime(end, "%Y-%m-%d") - datetime.strptime(start, "%Y-%m-%d")).days
                receipt_content += f"- {hotel.name} at {hotel.location} from {start} to {end}: ${hotel.price_per_room * num_days} total\n"
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
                Hotel("Hotel A", "New York", 4.5, 150, 10, "single"),
                Hotel("Hotel B", "Los Angeles", 4.0, 200, 5, "double"),
                Hotel("Hotel C", "Chicago", 3.5, 100, 8, "single"),
                Hotel("Hotel D", "New York", 4.2, 6, "double"),
                Hotel("Hotel E", "Los Angeles", 4.3, 4, "single"),
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

# Sample Usage with Menu
if __name__ == "__main__":
    hms = HotelManagementSystem()

    print("Welcome to the Hotel Management System!")
    username = input("Please enter your username: ").strip()

    # Check if user is a manager
    if username == hms.manager_username:
        password = input("Please enter your password: ")
        if password == hms.manager_password:
            manager = Manager(username)
            hms.users[username] = manager

            while True:
                print(Fore.CYAN + "\nManager Menu:")
                print(Fore.GREEN + "1. View Available Hotels")
                print(Fore.GREEN + "2. Add a Hotel")
                print(Fore.GREEN + "3. Edit a Hotel")
                print(Fore.RED + "4. Exit")

                choice = input(Fore.YELLOW + "Enter your choice (1-4): ")

                if choice == '1':
                    print("\nAvailable Hotels:")
                    hms.view_hotels()

                elif choice == '2':
                    name = input("Enter hotel name: ")
                    location = input("Enter location: ")
                    rating = hms.get_float("Enter rating: ")
                    price_per_room = hms.get_float("Enter price per room: ")
                    room_availability = hms.get_int("Enter number of available rooms: ")
                    room_type = input("Enter room type (e.g., single, double): ")
                    manager.add_hotel(hms, Hotel(name, location, rating, price_per_room, room_availability, room_type))
                    print("Hotel added successfully.")

                elif choice == '3':
                    hotel_name = input("Enter the name of the hotel to edit: ")
                    hotel = next((h for h in hms.hotels if h.name == hotel_name), None)
                    if hotel:
                        new_rating = input("Enter new rating (or press Enter to keep current): ")
                        new_price = input("Enter new price per room (or press Enter to keep current): ")
                        new_availability = input("Enter new number of available rooms (or press Enter to keep current): ")
                        new_room_type = input("Enter new room type (or press Enter to keep current): ")

                        if new_rating:
                            hotel.rating = hms.get_float("Enter new rating: ")
                        if new_price:
                            hotel.price_per_room = hms.get_float("Enter new price per room: ")
                        if new_availability:
                            hotel.room_availability = hms.get_int("Enter new number of available rooms: ")
                        if new_room_type:
                            hotel.room_type = new_room_type

                        print("Hotel updated successfully.")
                    else:
                        print("Hotel not found.")

                elif choice == '4':
                    print("Thank you for using the Hotel Management System!")
                    break

        else:
            print("Invalid password. Access denied.")

    else:
        # Treat as a customer
        customer = Customer(username)
        hms.users[username] = customer

        while True:
            print(Fore.CYAN + "\nCustomer Menu:")
            print(Fore.GREEN + "1. View Available Hotels")
            print(Fore.GREEN + "2. Search for a Hotel")
            print(Fore.GREEN + "3. Get Recommendations for My Next Booking")
            print(Fore.GREEN + "4. Book a Hotel")
            print(Fore.GREEN + "5. Remove a Booking")
            print(Fore.GREEN + "6. List My Bookings")
            print(Fore.GREEN + "7. Checkout")
            print(Fore.RED + "8. Exit")

            choice = input(Fore.YELLOW + "Enter your choice (1-8): ")

            if choice == '1':
                print("\nAvailable Hotels:")
                hms.view_hotels()

            elif choice == '2':
                name = input("Enter hotel name to search (or press Enter to skip): ")
                location = input("Enter location to search (or press Enter to skip): ")
                hms.search_hotel(name if name else None, location if location else None)

            elif choice == '3':
                hms.recommend_hotels(username)

            elif choice == '4':
                hotel_name = input("Enter the name of the hotel to book: ")
                room_type = input("Enter the room type you wish to book: ")
                start_date = input("Enter your booking start date (YYYY-MM-DD): ")
                end_date = input("Enter your booking end date (YYYY-MM-DD): ")
                # Validate date format
                try:
                    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
                    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
                    if start_date_obj >= end_date_obj:
                        print("End date must be after start date.")
                        continue
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
                    continue

                hms.book_hotel(username, hotel_name, room_type, start_date, end_date)

            elif choice == '5':
                hotel_name = input("Enter the name of the hotel to remove booking: ")
                hms.remove_booking(username, hotel_name)

            elif choice == '6':
                hms.list_user_bookings(username)

            elif choice == '7':
                hms.checkout(username)
                # After checkout, allow the user to get recommendations
                hms.recommend_hotels(username)

            elif choice == '8':
                print("Thank you for using the Hotel Management System!")
                break

            else:
                print("Invalid choice. Please select a valid option.")
