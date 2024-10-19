
#I will create a class called Event that will include name, date, discreption,location, and geust

from datetime import datetime
import re
from guest import Guest
import pickle

events_dict = {}

class Event:
    def __init__(self, name:str, event_date, description:str, location:str):
        self.name = name
        self.event_date = event_date
        self.description = description
        self.location = location
        self.guests = {} # Empty dictionary to store guests for this specific event, with email as key


    def __str__(self):
        return f"Event Name: {self.name}, Date: {self.event_date}, Location: {self.location}, Description: {self.description}"
    #If event is an instance of Event its will print(event). This method controls how the event is displayed when it is printed or converted to a string.           


#Methods

#1. Functions For Evants

#Create event
    def create_event(self):
        try:
            # Check if the event already exists by name
            if self.name in events_dict:
                print("Event Already Exists")
                return   
                
            events_dict[self.name] = self
            print(f"Event '{self.name}' created successfully")


        except Exception as e:
            print(f"The Event Could not be created. Error: {e}")                    


#Display all events
    def display_events(self):
        if not events_dict:
            print("No Events Found")
            return
        
        for event_name, event in events_dict.items():
            print(event)
            

#Search for event
    def search_event(self, name):
        if name in events_dict:
            event = events_dict[name]
            print(event) #Uses the __str__ method of the Event class to print the event details
            return event
            
        else:
            print("Event is Not Found")
            return None    


#Delete an event
    def delete_event(self, name):
        if name in events_dict:
            del events_dict[name]
            print("Event Deleted Successfully")

        else:
            print("The Event Could not be Deleted")



#2. Functions For Guests

#Add guest managment within event
#Add guest to event
    def add_guest(self, guest_name:str, guest_phone:int, guest_email:str, rsvp_status:str = "Pending"):

        guest_phone = str(guest_phone)

        # Phone number validation: Must be digits only and 10 characters long
        if not re.fullmatch(r"\d{10}", guest_phone):
            print(f"Invalid phone number '{guest_phone}'. It should contain exactly 10 digits.")
            return

        if guest_email in self.guests:
            print(f"The Guest with Email '{guest_email}' Already Exists in The Event")
            return
        
        else:
            new_guest = Guest(guest_name = guest_name, guest_phone = int(guest_phone), guest_email = guest_email, rsvp_status = rsvp_status)
            self.guests[guest_email] = new_guest
            print(f"The Guest '{guest_name}' Added to Event '{self.name}'")



#Display all the guests in event
    def display_guests(self):
        if not self.guests:
            print("No Guests Added to This Event")
            return
        
        print(f"Guest List for The Event '{self.name}': ")
        for guest_email, guest in self.guests.items():
            print(guest)



#Search for a guest by email
    def search_guest(self, guest_email: str):
        if guest_email in self.guests:
            guest = self.guests[guest_email]
            print(guest)  # Uses the __str__ method of the Guest class to print guest details
            return guest

        print("Guest Not Found")
        return None        
                


#Remove a guest
    def remove_guest(self, guest_email):
        if guest_email in self.guests:
            del self.guests [guest_email]
            print(f"Guest With Email '{guest_email}' Removed From Event '{self.name}'")

        else:
            print(f"No Guest Found With Email '{guest_email}' in This Event")



#Updates the RSVP status of a specific guest in an event
    def update_rsvp(self, guest_email, rsvp_status):
        if guest_email in self.guests:
            guest = self.guests[guest_email]
            guest.rsvp_status = rsvp_status   
            print(f"RSVP status for '{guest.guest_name}' updated to '{rsvp_status}'") 

        else:
            print(f"No Guest found with '{guest_email}' in this event")



#Filter Guests by RSVP Status
    def filter_by_rsvp(self, revp_status:str):
        filtered_guests = [guest for guest in self.guests.values() if guest.rsvp_status == revp_status]

        if not filtered_guests:
            print(f"No Guests Found With RSVP Status '{revp_status}'")
            return

        print(f"Guests With RSVP Status '{revp_status}':")
        for guest in filtered_guests:
            print(guest)



#Send Reminders to Guests by RSVP Status to whomes are Pending
    def send_reminder(self):
        pending_guests = [guest for guest in self.guests.values() if guest.rsvp_status == "Pending"]

        if not pending_guests:
            print("No Pending Guests to Send Reminders to")

        print("Sending Reminders to The Following Guests:")
        for guest in pending_guests:
            print(f"Reminder Sent to: {guest.guest_name} ({guest.guest_email})")



#Print Guests Count based on RSVP Status
    def attendance_count(self):
        attending = sum(1 for guest in self.guests.values() if guest.rsvp == "Attending")
        not_attending = sum(1 for guest in self.guests.values() if guest.rsvp == "Not Attending")
        pending = sum(1 for guest in self.guests.values() if guest.rsvp == "Pending")

        print(f"Attendance Count for Event '{self.name}': ")
        print(f"Attending: {attending}")
        print(f"Not Attending: {not_attending}")
        print(f"Pending: {pending}")                                                    
                           