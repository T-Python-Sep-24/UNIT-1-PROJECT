class Hotel:
    def __init__(self, name, location, rating, price_per_room, room_availability):
        self.name = name
        self.location = location
        self.rating = rating
        self.price_per_room = price_per_room
        self.room_availability = room_availability

    def __repr__(self):
        return f"{self.name} - {self.location} | Rating: {self.rating} | Price: ${self.price_per_room} | Rooms Available: {self.room_availability}"


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


class HotelManagementSystem:
    def __init__(self):
        self.hotels = []
        self.users = {}

    def add_hotel(self, hotel):
        self.hotels.append(hotel)

    def view_hotels(self):
        for hotel in self.hotels:
            print(hotel)

    def search_hotel(self, name=None, location=None):
        found = False
        for hotel in self.hotels:
            if (name and name.lower() in hotel.name.lower()) or (
                    location and location.lower() in hotel.location.lower()):
                print(hotel)
                found = True
        if not found:
            print("No hotels found.")

    def recommend_hotels(self, username):
        user = self.users.get(username)
        if user and user.view_bookings():
            booked_locations = {hotel.location for hotel in user.view_bookings()}
            recommendations = [hotel for hotel in self.hotels if
                               hotel.location in booked_locations and hotel not in user.view_bookings()]
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
        if hotel and hotel.room_availability > 0:
            user.add_booking(hotel)
            hotel.room_availability -= 1
            print(f"Booking confirmed for {hotel.name}!")
        else:
            print("Hotel not found or no rooms available.")

    def remove_booking(self, username, hotel_name):
        user = self.users.get(username)
        if user:
            hotel = next((h for h in self.hotels if h.name == hotel_name), None)
            if hotel:
                user.remove_booking(hotel)
                hotel.room_availability += 1
                print(f"Booking for {hotel.name} has been removed.")
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
            print(f"Total cost for {username}: ${total_cost}.")
            address = input("Enter your address: ")
            print(
                f"Receipt for {username}:\nTotal Cost: ${total_cost}\nAddress: {address}\nThank you for your booking!")
        else:
            print("User not found.")


# Sample Usage with Menu
if __name__ == "__main__":
    hms = HotelManagementSystem()

    # Add sample hotels
    hms.add_hotel(Hotel("Hotel A", "New York", 4.5, 150, 10))
    hms.add_hotel(Hotel("Hotel B", "Los Angeles", 4.0, 200, 5))
    hms.add_hotel(Hotel("Hotel C", "Chicago", 3.5, 100, 8))
    hms.add_hotel(Hotel("Hotel D", "New York", 4.2, 180, 6))
    hms.add_hotel(Hotel("Hotel E", "Los Angeles", 4.3, 220, 4))

    print("Welcome to the Hotel Management System!")
    customer_name = input("Please enter your username: ")
    customer = Customer(customer_name)
    hms.users[customer_name] = customer

    while True:
        print("\nMenu:")
        print("1. View Available Hotels")
        print("2. Search for a Hotel")
        print("3. Get Recommendations for My Next Booking")
        print("4. Book a Hotel")
        print("5. Remove a Booking")
        print("6. List My Bookings")
        print("7. Checkout")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            print("\nAvailable Hotels:")
            hms.view_hotels()

        elif choice == '2':
            hotel_name = input("Enter hotel name to search: ")
            hms.search_hotel(name=hotel_name)

        elif choice == '3':
            hms.recommend_hotels(customer_name)

        elif choice == '4':
            hotel_name = input("Enter the name of the hotel you want to book: ")
            hms.book_hotel(customer_name, hotel_name)

        elif choice == '5':
            hotel_name = input("Enter the name of the hotel you want to remove booking: ")
            hms.remove_booking(customer_name, hotel_name)

        elif choice == '6':
            hms.list_user_bookings(customer_name)

        elif choice == '7':
            hms.checkout(customer_name)

        elif choice == '8':
            print("Thank you for using the Hotel Management System!")
            break

        else:
            print("Invalid choice. Please try again.")

