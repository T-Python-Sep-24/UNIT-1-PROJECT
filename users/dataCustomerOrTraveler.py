from users.identfyPerson import Person
from datetime import datetime
import json

class Traveler(Person):
    def __init__(self, mainlist, name, traveler_id, email, phone, birthDate) -> None:
        super().__init__(name, traveler_id, email, phone)
        self.birthDate = birthDate
        self.mainlist = mainlist  

    def addDatatra(self):
        user_id = input("Enter traveler ID to add data for: ")
        traveler_dict = self.mainlist[3]
        if user_id not in traveler_dict:
            traveler_dict[user_id] = {
                "name": self.name,
                "phone": self.phone,
                "email": self.email,
                "birth_date": self.birthDate
            }
            self.saveDatatra()
            return "Done adding traveler data"
        else:
            return f"Traveler with ID {user_id} already exists."

    def removeDdatatra(self):
        user_id = input("Enter traveler ID to remove: ")
        traveler_dict = self.mainlist[3]
        if user_id in traveler_dict:
            del traveler_dict[user_id]
            self.saveDatatra(show_message=False)  # Silent save
            return f"Traveler with ID {user_id} has been removed."
        else:
            return f"Traveler with ID {user_id} not found."

    def searchDatatra(self):
        user_id = input("Enter traveler ID to search: ")
        traveler_dict = self.mainlist[3]
        if user_id in traveler_dict:
            traveler_info = traveler_dict[user_id]
            return f"Traveler found: Name: {traveler_info['name']}, Email: {traveler_info['email']}, Phone: {traveler_info['phone']}, Birth Date: {traveler_info['birth_date']}"
        else:
            return f"Traveler with ID {user_id} not found."
    
    def displayDatatra(self):
        traveler_dict = self.mainlist[3]
        if traveler_dict:
            for traveler_id, traveler_info in traveler_dict.items():
                print(f"ID: {traveler_id}, Name: {traveler_info['name']}, Email: {traveler_info['email']}, Phone: {traveler_info['phone']}, Birth Date: {traveler_info['birth_date']}")
        else:
            print("No traveler data found.")

    def saveDatatra(self, show_message=True):
        with open("information.json", "w", encoding="UTF-8") as file:
            json.dump(self.mainlist, file, indent=4)
        if show_message:
            print("Traveler data has been saved to 'information.json'.")

    def load_datatra(self):
        try:
            with open("information.json", "r", encoding="UTF-8") as file:
                self.mainlist = json.load(file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No existing data found.")
