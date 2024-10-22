from event_planning.event import Event
from event_planning.guest import Guest
from termcolor import colored

def main():
    
    print("-------------- Welcom To Your Event Planner --------------")
    print("-" * 60)


    Event.load_event("events_data.pkl")

#I added a space from No.1 to No.9 to Make the List align in one line
    while True:
        print("\nMain Menu:")
        print("1.  Create a New Event")
        print("2.  View All Events")
        print("3.  Search For a Specific Event")
        print("4.  Delete an Event")
        print("5.  Add a Guest to a Specific Event")
        print("6.  List All Guests for a Specific Event")
        print("7.  Search for a Specific Guest")
        print("8.  Remove a Guest from an Event")
        print("9.  Update a Guest's RSVP Status")
        print("10. Filter Guests by RSVP Status")
        print("11. Send Reminders to Guests with Pending RSVPs")
        print("12. View Attendance Count for a Specific Event")
        print("13. Save Events")
        print("14. Load Events")
        print("15. Export Guest List to a CSV File")
        print("16. Exit")
        
        user_input = input("\nReady to Manage Your Events? Type the Number of the Option You'd Like to Explore: ")


        if user_input == "1":
            event_name = input("Enter Event Name: ")
            event_date = input("Enter Event Date (YYYY-MM-DD): ")
            event_time = input("Enter Event Time (HH:MM) AM/PM: ")
            description = input("Enter Event Description: ")
            location = input("Enter Event Location: ")
            event = Event(event_name, event_date, event_time, description, location)
            event.create_event()


        elif user_input == "2":
            Event.display_events()


        elif user_input == "3":
            event_name = input("Enter Event Name to Search: ")
            event = Event.search_event(event_name)
            #For testing reason
            #if event:
                #print(event)

            #else:
                #print("No Event Found With That Name")    


        elif user_input == "4":
            event_name = input("Enter Event Name to Delete: ")
            Event.delete_event(event_name)


        elif user_input == "5":
            event_name = input("Enter Event Name: ")
            event = Event.search_event(event_name)
            if event:
                guest_name = input("Enter Guest Name: ")
                guest_phone = input("Enter Guest Phone Number (10 Digit): ")
                guest_email = input("Enter Guest Email: ")
                rsvp_status = input("Enter RSVP Status (Attending/ Not Attending/ Pending): ")
                event.add_guest(guest_name, guest_phone, guest_email, rsvp_status)


            else:
                print(colored("Event Not Found", "red"))    



        elif user_input == "6":
            event_name = input("Enter Event Name: ")
            event = Event.search_event(event_name)
            if event:
                event.display_guests()

            else:
                print(colored("Event Not Found", "red"))    



        elif user_input == "7":
            event_name = input("Enter Event Name: ")
            event = Event.search_event(event_name)
            if event:
                guest_email = input("Enter Guest Email to Search: ")
                event.search_guest(guest_email)

            else:
                print(colored("Event Not Found", "red"))    



        elif user_input == "8":
            event_name = input("Enter Event Name: ")
            event = Event.search_event(event_name)
            if event:
                guest_email = input("Enter Guest Email to Remove: ")
                if event.remove_guest(guest_email):
                    print(colored("Guest Removed Successfully", "green"))

                else:
                    print(colored("Failed To Remove Guest", "red"))

            else:
                print(colored("Event Not Found", "red"))            



        elif user_input == "9":
            event_name = input("Enter Event Name: ")
            event = Event.search_event(event_name)
            if event:
                guest_email = input("Enter Guest Email to Update RSVP: ")
                rsvp_status = input("Enter New RSVP Status (Attending/ Not Attending/ Pending): ")
                event.update_rsvp(guest_email, rsvp_status)

            else:
                print(colored("Event Not Found", "red"))    



        elif user_input == "10":
            event_name = input("Enter Event Name: ")
            event = Event.search_event(event_name)
            if event:
                rsvp_status = input("Enter RSVP Status to Filter By: ")
                matching_guests = event.filter_by_rsvp(rsvp_status)
                if matching_guests:
                    print(colored(f"Found {len(matching_guests)} Guests With Status '{rsvp_status}'","yellow"))

                else:
                    print(colored("No Guests Found With That Status", "red"))

            else:
                print(colored("Event Not Found", "red"))            


        elif user_input == "11":
            event_name = input("Enter Event Name: ")
            event = Event.search_event(event_name)
            if event:
                sender_email = input("Enter Your Gmail Address: ")
                sender_password = input("Enter Your Gmail App Password: ")
                event.send_reminder(sender_email, sender_password)

            else:
                print(colored("Event Not Found", "red"))    


        elif user_input == "12":
            event_name = input("Enter Event Name: ")
            event = Event.search_event(event_name)
            if event:
                event.attendance_count()

            else:
                print(colored("Event Not Found", "red"))    


        elif user_input == "13":
            filename = input("Enter File Name to Save Event: ")
            Event.save_event(filename)


        elif user_input == "14":
            filename = input("Enter File Name to Load Event: ")
            Event.load_event(filename)            


        elif user_input == "15":
            event_name = input("Enter Event Name: ")
            event = Event.search_event(event_name)
            if event:
                filename = input("Enter File Name to Export (guest_list.csv): ")
                event.export_guest_to_csv(filename)

            else:
                print(colored("Event Not Found", "red"))    


        elif user_input == "16":
            save_choice = input(colored("Do you want to save changes before exiting? (yes/no): ", "magenta")).strip().lower()
            if save_choice == "yes":
                Event.save_event()

            print("Exiting Event Planner")
            break


        else:
            print("Invalid, Please Try Again")

if __name__ == "__main__":
    main()            