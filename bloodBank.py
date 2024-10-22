# import libraries 
import json   # to save and load donor information.
import os     # checking if a file exists

class BloodBank:          # Defines a new class
    def __init__(self):   # Defines the constructor method
        self.donors = {}  # Dictionary to store donor information
        self.load_data()  # load existing donor data from a JSON file

    def add_donor(self, name, age, gender, email, phone, blood_type, quantity):
        # Check eligibility based on age and other conditions
        if age < 18 or age > 65:
            print("Donor must be between 18 and 65 years old.")
            return
        if quantity < 0:
            print("Quantity cannot be negative.")
            return

        donor_id = len(self.donors) + 1
        self.donors[donor_id] = {
            'name': name,
            'age': age,
            'gender': gender,
            'email': email,
            'phone': phone,
            'blood_type': blood_type,
            'quantity': quantity
        }
        self.save_data()
        print(f"Donor {name} added successfully!")

    def view_donors(self):
        if not self.donors:
            print("No donors found.")
        else:
            for donor_id, details in self.donors.items():
                print(f"ID: {donor_id}, Name: {details['name']}, Age: {details['age']}, Gender: {details['gender']}, "
                      f"Email: {details['email']}, Phone: {details['phone']}, Blood Type: {details['blood_type']}, "
                      f"Quantity: {details['quantity']}")

    def search_donor(self, donor_id):
        if donor_id in self.donors:
            details = self.donors[donor_id]
            print(f"ID: {donor_id}, Name: {details['name']}, Age: {details['age']}, Gender: {details['gender']}, "
                  f"Email: {details['email']}, Phone: {details['phone']}, Blood Type: {details['blood_type']}, "
                  f"Quantity: {details['quantity']}")
        else:
            print("Donor not found.")

    def total_blood_quantity(self):
        total = sum(details['quantity'] for details in self.donors.values())
        return total

    def save_data(self):
        with open('donors.json', 'w') as file:
            json.dump(self.donors, file)            #saves the current donor information to a JSON file

    def load_data(self):
        if os.path.exists('donors.json'):
            with open('donors.json', 'r') as file:
                self.donors = json.load(file)
