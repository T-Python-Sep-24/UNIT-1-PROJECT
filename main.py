from Car_files.car import Car, CarStorage
from Car_files.customer import Customer
from Car_files.manager import Manager


# Initialize car storage
car_storage = CarStorage()
car_storage.load_file()

# admin login info
manager_name = "fahad"
manager_password = "123"


manager = Manager(manager_name, manager_password, car_storage)

def manager_menu():
    while True:
        print("\nManager Menu:")
        print("1. Add a Car")
        print("2. Remove a Car")
        print("3. List All Cars")
        print("4. Search for a Car")
        print("5. Rental history")
        print("6. Logout")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                cname = input("Enter car name: ")
                year = int(input("Enter car year: "))
                price = float(input("Enter car price: "))
                manager.add_car(cname, year, price)
            elif choice == "2":
                cname = input("Enter car name: ")
                year = int(input("Enter car year: "))
                manager.remove_car(cname, year)
            elif choice == "3":
                manager.list_all_cars()
            elif choice == "4":
                cname = input("Enter car name: ")
                year = int(input("Enter car year: "))
                manager.search_car(cname, year)
            elif choice == "5":
                manager.rental_history()
            elif choice == "6":
                print("Logging out...")
                break
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Invalid input!")

def customer_menu():
    customer_name = input("Enter your name: ")
    while True:
        try:
            customer_id = int(input("Enter your ID: "))
            break  
        except ValueError:
            print("Invalid input, Please enter a valid number!")

    customer = Customer(customer_name, customer_id, car_storage, manager)
    customer.save_customer_file()
    customer.load_customer_file()
    while True:
        print("\nCustomer Menu:")
        print("1. Rent a Car")
        print("2. Return a Car")
        print("3. Search for a Car")
        print("4. List Available Cars")
        print("5. My Rented Cars")
        print("6. Logout")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                cname = input("Enter car name: ")
                year = int(input("Enter car year: "))
                customer.rent_car(cname, year)
            elif choice == "2":
                cname = input("Enter car name: ")
                year = int(input("Enter car year: "))
                customer.return_car(cname, year)
            elif choice == "3":
                cname = input("Enter car name: ")
                year = int(input("Enter car year: "))
                customer.search_for_car(cname, year, car_storage)
            elif choice == "4":
                customer.list_available_cars(car_storage)
            elif choice == "5":
                customer.my_rented_cars()
            elif choice == "6":
                print("Logging out...")
                customer.save_customer_file()
                return
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Invalid input! Please enter number 1-6.")
def main():
    while True:
        print("\nWelcome to the Car Rental Program!")
        print("1. Customer")
        print("2. Manager")
        print("3. Exit")
        user_type = input("Are you a customer or manager? ")

        if user_type == "1":
            customer_menu()
        elif user_type == "2":
            print("Please log in as manager.")
            name = input("Enter manager name: ")
            password = input("Enter manager password: ")
            if manager.login(name, password):
                manager_menu()
            else:
                print("Login failed, try again.")
        elif user_type == "3":
            print("Thank you for using the Car Rental program.")
            break
        else:
            print("Invalid choice, please select 1, 2, or 3.")
try:
    main()

except Exception as e:
    print(f"unexpected error: {e}")
