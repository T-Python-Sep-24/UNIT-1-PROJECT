from classes import *

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

