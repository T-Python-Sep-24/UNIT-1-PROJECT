## Created a class called Event that will include name, event date, description, location, and a list of guests

from datetime import datetime
from .guest import Guest
import pickle
import csv

events_dict = {}

class Event:
    def __init__(self, name:str, event_date:str, description:str, location:str):

        self.name = name
        self.description = description
        self.location = location
        self.guests = {} #Empty dictionary to store guests for this specific event, with email as key

        #Convert event_date to a datetime object
        try:
            self.event_date = datetime.strptime(event_date, "%Y-%m-%d")
            
        except ValueError:
            print(f"Invalid Date Format For '{event_date}'. Use 'YYYY-MM-DD'.")
            return 
    


    def __str__(self):
        return(
            f"Event Name: {self.name}\n"
            f"Date: {self.event_date}\n"
            f"Location: {self.location}\n"
            f"Description: {self.description}\n"
            + "-" * 60 #Check
               
        ) #If event is an instance of Event its will print(event). This method controls how the event is displayed when it is printed or converted to a string.           


#Methods

#1. Functions For Events

#Create Event
    def create_event(self):
        try:
            # Check if the event already exists by name
            if self.name in events_dict:
                print("Event Already Exists")
                return   
                
            events_dict[self.name] = self
            print(f"Event '{self.name}' Created Successfully")
            Event.save_event()


        except Exception as e:
            print(f"The Event Could Not be Created. Error: {e}")
                                



#Display all Events By Name
    @classmethod
    def display_events(cls):
        if not events_dict:
            print("No Events Found")
            return
        
        for index, (event_name, event) in enumerate (events_dict.items(), start = 1):
            print(f"{index}. {event_name} - {event}")
            


#Search for Event By Name
    @classmethod
    def search_event(cls, event_name:str):
        if event_name in events_dict:
            event = events_dict[event_name]
            print(event) #Uses the __str__ method of the Event class to print the event details
            return event
            
        else:
            print("Event is Not Found")
            return None    



#Delete an Event By Name
    @classmethod
    def delete_event(cls, event_name):
        if event_name in events_dict:
            del events_dict[event_name]
            print(f"Event '{event_name}' Deleted Successfully")
            cls.save_event()

        else:
            print("The Event Could Not be Deleted")




#2. Functions For Guests

#Add guest managment within event
#Add Guest to a Specific Event
    def add_guest(self, guest_name:str, guest_phone:int, guest_email:str, rsvp_status:str = "Pending"):

        if guest_email in self.guests:
            print(f"The Guest with Email '{guest_email}' Already Exists in The Event")
            return
        
        try:
            new_guest = Guest(
                guest_name = guest_name,
                guest_phone = guest_phone,
                guest_email = guest_email,
                rsvp_status = rsvp_status
                )
            
            self.guests[guest_email] = new_guest
            print(f"The Guest '{guest_name}' Added to Event '{self.name}'")
            Event.save_event()
            

        except Exception as e:
            print(f"Error Adding Guest: {e}")    



#Display All the Guests in Specific Event
    def display_guests(self):
        if not self.guests:
            print("No Guests Added Yet to This Event")
            return
        
        print(f"Guest List for The Event '{self.name}': \n" + ":" * 60) 
        for index, (guest_email, guest) in enumerate (self.guests.items(), start = 1):
            print(f"{index}. {guest_email} - {guest}")



#Search For a Guest By Email
    def search_guest(self, guest_email: str):
        if guest_email in self.guests:
            guest = self.guests[guest_email]
            print(guest)  # Uses the __str__ method of the Guest class to print guest details
            return guest

        print("Guest Not Found")
        return None        
                


#Remove a Guest By Email
    def remove_guest(self, guest_email):
        if guest_email in self.guests:
            del self.guests [guest_email]
            print(f"Guest With Email '{guest_email}' Removed From Event '{self.name}'")
            Event.save_event()
            return True

        else:
            print(f"No Guest Found With Email '{guest_email}' in This Event")
            return False



#Updates the RSVP Status of a Specific Guest in an Event
    def update_rsvp(self, guest_email, rsvp_status):
        if guest_email in self.guests:
            guest = self.guests[guest_email]
            guest.rsvp_status = rsvp_status   
            print(f"RSVP Status for '{guest.guest_name}' Updated to '{rsvp_status}'") 

        else:
            print(f"No Guest Found With Email'{guest_email}' in This Event")



#Filter Guests by RSVP Status
    def filter_by_rsvp(self, rsvp_status:str):
        filtered_guests = [guest for guest in self.guests.values() if guest.rsvp_status == rsvp_status]

        if not filtered_guests:
            print(f"No Guests Found With This RSVP Status '{rsvp_status}'")
            return []

        print(f"Guests With RSVP Status '{rsvp_status}': \n" + ":" * 60)
        for index, (guest) in enumerate (filtered_guests, start = 1):
            print(f"{index}. {guest}") 

        return filtered_guests    



#Send Reminders Based on RSVP Status to The Guests who are Pending
    def send_reminder(self):
        pending_guests = [guest for guest in self.guests.values() if guest.rsvp_status == "Pending"]

        if not pending_guests:
            print("No Pending Guests to Send Reminders to")
            return

        print("Sending a Reminders to The Following Guests: \n" + ":" * 60) 
        for index, (guest) in enumerate (pending_guests, start = 1): 
            print(f"{index}. Reminder Sent to: {guest.guest_name} - ({guest.guest_email})") 



#Print Guests Count based on RSVP Status
    def attendance_count(self):
        attending = sum(1 for guest in self.guests.values() if guest.rsvp_status == "Attending")
        not_attending = sum(1 for guest in self.guests.values() if guest.rsvp_status == "Not Attending")
        pending = sum(1 for guest in self.guests.values() if guest.rsvp_status == "Pending")

        print(f"Attendance Count for Event '{self.name}': ")
        print(f"Attending: {attending}")
        print(f"Not Attending: {not_attending}")
        print(f"Pending: {pending}")



#Save Event with Pickle
    @classmethod
    def save_event(cls, filename:str = "events_data.pkl"):
        global events_dict
        try:
            with open(filename, 'wb') as file:
                pickle.dump(events_dict, file)
                print(f"Events Successfully Saved to '{filename}'")
        
        except Exception as e:
            print(f"Error Saving File: {e}")



#Load Events with Pickle
    @classmethod
    def load_event(cls, filename: str = "events_data.pkl"):
        global events_dict
        try:
            with open(filename, 'rb') as file:
                events_dict = pickle.load(file)
                print(f"Events Successfully Loaded From '{filename}'")
                
        except FileNotFoundError:
            print(f"File '{filename}' Not Found. No Data Loaded.")
            
        except Exception as e:
            print(f"Error Loading File: {e}")



#Exporting Guest List as CSV File, so User Can Share or Print it
    def export_guest_to_csv(self, filename = "Guest_List.csv"):
        if not self.guests:
            print("No Guests to Export")
            return

        try:
            with open(filename, mode = 'w', newline='', encoding = 'utf-8') as file:
                writer = csv.writer(file)

                #Write The Header Row
                writer.writerow([
                    "Guests Name",
                    "Phone Number",
                    "Email",
                    "RSVP Status"
                ])

                #Write Each Guest's Details
                for guest in self.guests.values():
                    writer.writerow([
                        guest.guest_name,
                        guest.guest_phone,
                        guest.guest_email,
                        guest.rsvp_status,
                    ])

                print(f"Guest List Successfully Exported to '{filename}'") 

        except Exception as e:
            print(f"Error Exporting Guest to CSV: {e}")