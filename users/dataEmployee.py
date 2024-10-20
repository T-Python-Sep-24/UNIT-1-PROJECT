from datetime import datetime
from identfyPerson  import Person
import json 



class Employee(Person):
    def __init__(self, name, id, email, phonenum ,position ) -> None:
        super().__init__(name, id, email, phonenum)
        self.position = position
        self.keepData = {}     
    
    def add_data(self):
        # Check if id is already in keepData
        if self.id not in self.keepData:
            # Add employee data to the keepData dictionary
            self.keepData[self.id] = {
                "name": self.name,
                "number": self.phonenum,
                "email": self.email,
                "position": self.position
            }
            return "Done adding data"
        else:
            return f"Employee with ID {self.id} already exists."
            
            # return data
        

    def remove_data(self):
        if self.id in self.keepData:
            del self.keepData[self.id]
            return f"All data for {self.id} has been deleted"
        else:
            return f"{self.id} not found in the data."


    def search_data(self):
        if self.id  in self.keepData :
            return f" This is person at work organization "

        else:
            return f" is not at work organization "

    
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
    