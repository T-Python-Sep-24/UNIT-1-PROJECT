## Created a class called Event that will include name, event date, description, location, and a list of guests

from datetime import datetime
from .guest import Guest
import pickle
import csv
from termcolor import colored

#To Send a real email to pending guests:
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

events_dict = {}

class Event:
    def __init__(self, name:str, event_date:str, event_time:str, description:str, location:str):

        self.name = name
        self.description = description
        self.location = location
        self.guests = {} #Empty dictionary to store guests for this specific event, with email as key


        # Convert event_date to a datetime object
        try:
            self.event_date = datetime.strptime(event_date, "%Y-%m-%d")
        except ValueError:
            print(colored(f"Invalid Date Format For '{event_date}'. Use 'YYYY-MM-DD'.", "red"))
            self.event_date = None

        # Convert event_time to 12-hour format
        try:
            event_time_format = datetime.strptime(event_time, "%I:%M %p")
            self.event_time = event_time_format.strftime("%I:%M %p")  # Store in 12-hour format
        except ValueError:
            print(colored(f"Invalid Time Format For '{event_time}'. Use 'HH:MM AM/PM'.", "red"))
            self.event_time = None

    


    def __str__(self):
        # Check if event_date and event_time are None before formatting
        event_date_str = self.event_date.strftime('%Y-%m-%d') if self.event_date else "N/A"
        event_time_str = self.event_time if self.event_time else "N/A"
        
        return (
            f"Event Name: {self.name}\n"
            f"Date: {event_date_str}\n"
            f"Time: {event_time_str}\n"
            f"Location: {self.location}\n"
            f"Description: {self.description}\n"
            + "-" * 60
        ) #If event is an instance of Event its will print(event). This method controls how the event is displayed when it is printed or converted to a string.           


#Methods

#1. Functions For Events

#Create Event
    def create_event(self):
        try:
            # Check if the event already exists by name
            if self.name in events_dict:
                print(colored("Event Already Exists", "yellow"))
                return   
                
            events_dict[self.name] = self
            print(colored(f"Event '{self.name}' Created Successfully", "green"))
            Event.save_event()


        except Exception as e:
            print(colored(f"The Event Could Not be Created. Error: {e}", "red"))
                                



#Display all Events By Name
    @classmethod
    def display_events(cls):
        if not events_dict:
            print(colored("No Events Found", "red"))
            return
        
        for index,(event_name, event) in enumerate(events_dict.items(), start=1):
            print(colored(f"{index}. {event}", "yellow"))
            
            
            


#Search for Event By Name
    @classmethod
    def search_event(cls, event_name:str):
        if event_name in events_dict:
            event = events_dict[event_name]
            print(event) #Uses the __str__ method of the Event class to print the event details
            return event
            
        else:
            print(colored("Event is Not Found", "red"))
            return None    



#Delete an Event By Name
    @classmethod
    def delete_event(cls, event_name):
        if event_name in events_dict:
            del events_dict[event_name]
            print(colored(f"Event '{event_name}' Deleted Successfully", "green"))
            cls.save_event()

        else:
            print(colored("The Event Could Not be Deleted", "red"))




#2. Functions For Guests

#Add guest managment within event
#Add Guest to a Specific Event
    def add_guest(self, guest_name:str, guest_phone:int, guest_email:str, rsvp_status:str = "Pending"):

        if guest_email in self.guests:
            print(colored(f"The Guest with Email '{guest_email}' Already Exists in The Event", "yellow"))
            return
        
        try:
            new_guest = Guest(
                guest_name = guest_name,
                guest_phone = guest_phone,
                guest_email = guest_email,
                rsvp_status = rsvp_status
                )
            
            self.guests[guest_email] = new_guest
            print(colored(f"The Guest '{guest_name}' Added to Event '{self.name}'", "green"))
            Event.save_event()
            

        except Exception as e:
            print(colored(f"Error Adding Guest: {e}", "red"))    



#Display All the Guests in Specific Event
    def display_guests(self):
        if not self.guests:
            print(colored("No Guests Added Yet to This Event", "red"))
            return
        
        print(f"Guest List for The Event '{self.name}': \n" + ":" * 60) 
        for index, (guest_email, guest) in enumerate (self.guests.items(), start = 1):
            print(colored(f"{index}. {guest_email} - {guest}", "yellow"))



#Search For a Guest By Email
    def search_guest(self, guest_email: str):
        if guest_email in self.guests:
            guest = self.guests[guest_email]
            print(guest)  # Uses the __str__ method of the Guest class to print guest details
            return guest

        print(colored("Guest Not Found", "red"))
        return None        
                


#Remove a Guest By Email
    def remove_guest(self, guest_email):
        if guest_email in self.guests:
            del self.guests [guest_email]
            print(colored(f"Guest With Email '{guest_email}' Removed From Event '{self.name}'", "green"))
            Event.save_event()
            return True

        else:
            print(colored(f"No Guest Found With Email '{guest_email}' in This Event", "red"))
            return False



#Updates the RSVP Status of a Specific Guest in an Event
    def update_rsvp(self, guest_email, rsvp_status):
        if guest_email in self.guests:
            guest = self.guests[guest_email]
            guest.rsvp_status = rsvp_status   
            print(colored(f"RSVP Status for '{guest.guest_name}' Updated to '{rsvp_status}'", "green"))

        else:
            print(colored(f"No Guest Found With Email'{guest_email}' in This Event", "red"))



#Filter Guests by RSVP Status
    def filter_by_rsvp(self, rsvp_status:str):
        filtered_guests = [guest for guest in self.guests.values() if guest.rsvp_status == rsvp_status]

        if not filtered_guests:
            print(f"No Guests Found With This RSVP Status '{rsvp_status}'")
            return []

        print(f"Guests With RSVP Status '{rsvp_status}': \n" + ":" * 60)
        for index, (guest) in enumerate (filtered_guests, start = 1):
            print(colored(f"{index}. {guest}", "yellow")) 

        return filtered_guests    



#Send Reminders Based on RSVP Status to The Guests with Pending RSVP
    def send_reminder(self, sender_email, sender_password):
        pending_guests = [guest for guest in self.guests.values() if guest.rsvp_status == "Pending"]

        if not pending_guests:
            print(colored("No Pending Guests to Send Reminders to", "red"))
            return


        #Gmail SMTP server setting
        smtp_server = "smtp.gmail.com"
        port = 587 #For TLS


        try:
            #Set up the SMTP server
            server = smtplib.SMTP(smtp_server, port)
            server.starttls() #Start TLS encryption 
            server.login(sender_email, sender_password) #Login to the server

            

            print("Sending a Reminders to The Following Guests: \n" + ":" * 60)
            for index, guest in enumerate (pending_guests, start = 1):
                #Email content
                subject = f"Reminder: RSVP for The Event '{self.name}'"
                body = (
                    f"Hi {guest.guest_name},\n\n"
                    f"This is a reminder to RSVP for the Event '{self.name}'. Scheduled on {self.event_date.strftime('%Y-%m-%d')}, {self.event_time}.\n" 
                    f"Please let me know your response.\n\nThank You!"
                )


                #Set up the MIME message
                message = MIMEMultipart()
                message["From"] = sender_email
                message["To"] = guest.guest_email
                message["Subject"] = subject
                message.attach(MIMEText(body, "plain"))


                #send the email
                server.sendmail(sender_email, guest.guest_email, message.as_string())
                print(colored(f"{index}. Reminder sent to: {guest.guest_name} - ({guest.guest_email})", "yellow"))

            #close the server connection
            server.quit()

        except Exception as e:
            print(colored(f"Error Sending Email: {e}", "red"))   


        #Old print sentance for ending a message to guests with pending RSVP
        # print("Sending a Reminders to The Following Guests: \n" + ":" * 60) 
        # for index, (guest) in enumerate (pending_guests, start = 1): 
        #     print(f"{index}. Reminder Sent to: {guest.guest_name} - ({guest.guest_email})") 



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
                print(colored(f"Events Successfully Saved to '{filename}'", "green"))
        
        except Exception as e:
            print(colored(f"Error Saving File: {e}", "red"))



#Load Events with Pickle
    @classmethod
    def load_event(cls, filename: str = "events_data.pkl"):
        global events_dict
        try:
            with open(filename, 'rb') as file:
                events_dict = pickle.load(file)
                print(colored(f"Events Successfully Loaded From '{filename}'", "green"))
                
        except FileNotFoundError:
            print(colored(f"File '{filename}' Not Found. No Data Loaded.", "yellow"))
            
        except Exception as e:
            print(colored(f"Error Loading File: {e}", "red"))



#Exporting Guest List as CSV File, so User Can Share or Print it
    def export_guest_to_csv(self, filename = "Guest_List.csv"):
        if not self.guests:
            print(colored("No Guests to Export", "yellow"))
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

                print(colored(f"Guest List Successfully Exported to '{filename}'", "green"))

        except Exception as e:
            print(colored(f"Error Exporting Guest to CSV: {e}", "red"))