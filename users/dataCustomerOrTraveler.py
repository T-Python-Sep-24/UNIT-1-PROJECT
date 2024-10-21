from users.identfyPerson import Person
from datetime import datetime
import json

class Traveler(Person):
    def __init__(self, name, id, email, phonenum, birthDate: datetime) -> None:
        super().__init__(name, id, email, phonenum)
        self.birthDate = birthDate
        self.keepDatatr = {}  

    def addData(self):
        user_id = input("Enter traveler ID to add data for: ")
        if user_id not in self.keepDatatr:
            name = input("Enter name: ")
            phonenum = input("Enter phone number: ")
            email = input("Enter email: ")
            birthDate = datetime.date.today()
           
            self.keepDatatr[user_id] = {
                "name": name,
                "number": phonenum,
                "email": email,
                "birthDate": birthDate
            }
            return "Done adding traveler data"
        else:
            return f"Traveler with ID {user_id} already exists."

    def removeData(self):
        user_id = input("Enter traveler ID to remove data for: ")
        if user_id in self.keepDatatr:
            del self.keepDatatr[user_id]
            return f"All data for Traveler {user_id} has been deleted"
        else:
            return f"Traveler with ID {user_id} not found in the data."

    def searchData(self):
        user_id = input("Enter traveler ID to search for: ")
        if user_id in self.keepDatatr:
            return f"Traveler {self.keepDatatr[user_id]['name']} is a registered traveler."
        else:
            return f"Traveler with ID {user_id} is not registered."


    def saveData(self):
        with open("information.json", "a", encoding="UTF-8") as fileData:
            json_datatr = json.dumps(self.keepDatatr, indent=3)
            fileData.write(json_datatr + "\n")
        return "Traveler data has been saved."

    def loadData(self):
        with open("information.json", "r", encoding="UTF-8") as fileData:
            loaded_data = json.load(fileData)
        return loaded_data

    def displayData(self, loaded_data):
        for count, countData in enumerate(loaded_data, start=1):
            print(f"{count}: {countData}")
