# Blood Bank Management System

class BloodBank:
    def __init__(self):
        self.donors = {}  # Dictionary to store donor information

    def add_donor(self, name, blood_type, quantity):
        donor_id = len(self.donors) + 1
        self.donors[donor_id] = {
            'name': name,
            'blood_type': blood_type,
            'quantity': quantity
        }
        print(f"Donor {name} added successfully!")

    

def display_menu():
    print("\n--- Blood Bank Management System ---")
    print("1. Add Donor")
    print("2. View Donors")
    print("3. Search Donor")
    print("4. Total Blood Quantity")
    print("5. Exit")

