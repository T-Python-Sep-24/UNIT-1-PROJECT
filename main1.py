from class1 import *
from colorama import init, Fore, Style
init(autoreset=True)
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
                    manager.add_hotel(hms, Hotel(name, location, rating, price_per_room, room_availability))
                    print("Hotel added successfully.")

                elif choice == '3':
                    hotel_name = input("Enter the name of the hotel to edit: ")
                    hotel = next((h for h in hms.hotels if h.name == hotel_name), None)
                    if hotel:
                        new_rating = input("Enter new rating (or press Enter to keep current): ")
                        new_price = input("Enter new price per room (or press Enter to keep current): ")
                        new_availability = input("Enter new number of available rooms (or press Enter to keep current): ")

                        if new_rating:
                            hotel.rating = hms.get_float("Enter new rating: ")
                        if new_price:
                            hotel.price_per_room = hms.get_float("Enter new price per room: ")
                        if new_availability:
                            hotel.room_availability = hms.get_int("Enter new number of available rooms: ")

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
                hms.book_hotel(username, hotel_name)

            elif choice == '5':
                hotel_name = input("Enter the name of the hotel to remove booking: ")
                hms.remove_booking(username, hotel_name)

            elif choice == '6':
                hms.list_user_bookings(username)

            elif choice == '7':
                hms.checkout(username)

            elif choice == '8':
                print("Thank you for using the Hotel Management System!")
                break

            else:
                print("Invalid choice. Please select a valid option.")
