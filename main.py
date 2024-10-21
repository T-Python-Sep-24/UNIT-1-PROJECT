from bloodBank import BloodBank



def main():
    blood_bank = BloodBank()
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        try:
            if choice == '1':
                name = input("Enter donor name: ")
                blood_type = input("Enter blood type (A, B, AB, O): ")
                quantity = float(input("Enter quantity of blood (in liters): "))
                if quantity < 0:
                    raise ValueError("Quantity cannot be negative.")
                blood_bank.add_donor(name, blood_type, quantity)
            elif choice == '2':
                blood_bank.view_donors()
            elif choice == '3':
                donor_id = int(input("Enter donor ID to search: "))
                blood_bank.search_donor(donor_id)
            elif choice == '4':
                total_quantity = blood_bank.total_blood_quantity()
                print(f"Total blood quantity in the bank: {total_quantity} liters")
            elif choice == '5':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()