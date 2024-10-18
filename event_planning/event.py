
#I will create a class called Event that will include name, date, discreption,location, and geust

from datetime import datetime
from guest import Guest

events_list = []

class Event:
    def __init__(self, name:str, event_date, description:str, location:str):
        self.name = name
        self.event_date = event_date
        self.description = description
        self.location = location
        self.guests = [] # Empty list to store guests for this specific event


    def __str__(self):
        return f"Event Name: {self.name}, Date: {self.event_date}, Location: {self.location}, Description: {self.description}"
    #If event is an instance of Event its will print(event). This method controls how the event is displayed when it is printed or converted to a string.           


#Methods

#Create event
    def create_event(self):
        try:
            # Check if the event already exists by name
            for event in events_list:
                if event.name == self.name:
                    print("Event Already Exists")
                    return   
                
            events_list.append(self)
            print(f"Event '{self.name}' created successfully")


        except Exception as e:
            print(f"The Event Could not be created. Error: {e}")                    


#Display all events
    def display_events(self):
        if not events_list:
            print("No Events Found.")
            return
        
        for event in events_list:
            print(event)
            

#Search for event
    def search_event(self, name):
        for event in events_list:
            if event.name == name:
                print(event) # Uses the __str__ method of the Event class to print the event details
                return event
            
        else:
            print("Event is Not Found")
            return None    


#Delete an event
    def delete_event(self, name):
        event = self.search_event(name)
        if event:
            events_list.remove(event)
            print("Event Deleted Successfully")

        else:
            print("The Event Could not be Deleted")       