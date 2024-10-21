# from datetime import datetime
from users.identfyPerson import Person
import json 

class Employee(Person):
    def __init__(self, name, id, email, phonenum ,position ) -> None:
        super().__init__(name, id, email, phonenum)
        self.position = position
        self.keepData = {}     
    ###
    def add_data(self):
        user_id = input("Enter employee ID to add data for: ")
        if user_id not in self.keepData:
            self.keepData[user_id] = {
                "name": self.name,
                "number": self.phonenum,
                "email": self.email,
                "position":self.position
            }
            return "Done adding data"
        else:
            return f"Employee with ID {user_id} already exists."
       ## 
    def remove_data(self):
        user_id = input("Enter employee ID to remove data for: ")
        if user_id in self.keepData:
            del self.keepData[user_id]
            return f"All data for {user_id} has been deleted"
        else:
            return f"Employee with ID {user_id} not found in the data."

    def search_data(self):
        user_id = input("Enter employee ID to search: ")
        if user_id in self.keepData:
            return f"Employee {self.keepData[user_id]['name']} is at work organization."
        else:
            return f"Employee with ID {user_id} is not at work organization."

    def save_data(self):
        with open("information.josn" , "+a" , encoding="UTF-8") as fileData:
            json_data = json.dumps(self.keepData, indent=3)
            fileData.write(json_data + "\n") 

    def load_data(self):
        with open("information.json", "r", encoding="UTF-8") as fileData:
            loaded_data = json.load(fileData)
        return loaded_data

    def display_data(self, loaded_data):
        for counter, counterData in enumerate(loaded_data, start=1):
            print(f"{counter}: {counterData}")    
    