from identfyPerson import Person
from datetime import date
import json

class Traveler(Person):
    def __init__(self, name, id, email, phonenum, birthDate: date) -> None:
        super().__init__(name, id, email, phonenum)
        self.birthDate = birthDate
        self.keepDatatr = {}  # Dictionary to hold traveler data


    def addData(self):
        # Check if travelerId is already in keepDatatr
        if self.id not in self.keepDatatr:
            # Add traveler data to the keepDatatr dictionary
            self.keepDatatr[self.id] = {
                "name": self.name,
                "number": self.phonenum,
                "email": self.email,
                "birthDate": self.birthDate
            }
            return "Done adding traveler data"
        else:
            return f"Traveler with ID {self.id} already exists."


    def removeData(self):
        # Remove traveler data by travelerId
        if self.id in self.keepDatatr:
            del self.keepDatatr[self.id]
            return f"All data for Traveler {self.id} has been deleted"
        else:
            return f"Traveler with ID {self.id} not found in the data."


    def searchData(self):
        # Search for a traveler by travelerId
        if self.id in self.keepDatatr:
            return f"This person is a registered traveler."
        else:
            return f"Traveler with ID {self.id} is not registered."


    def saveData(self):
        # Save the 'keepDatatr' dictionary to the JSON file
        with open("information.json", "a", encoding="UTF-8") as fileData:
            json_datatr = json.dumps(self.keepDatatr, indent=3)
            fileData.write(json_datatr + "\n")
        return "Traveler data has been saved."


    def loadData(self):
        # Load data from the JSON file
        with open("information.json", "r", encoding="UTF-8") as fileData:
            loaded_data = json.load(fileData)
        return loaded_data


    def displayData(self, loaded_data):
        # Display loaded traveler data with an index
        for count, countData in enumerate(loaded_data, start=1):
            print(f"{count}: {countData}")
