from event_planning.event import Event
from event_planning.guest import Guest

def main():
    
    print("-------------- Welcom To Your Event Planner --------------")
    print("-" * 60)


    Event.load_event("events_data.pkl")

#I added a space from No.1 to No.9 to Make the List align in one line
    while True:
        print("\nMain Menu:")
        print("1.  To Create a New Event")
        print("2.  To View All Events")
        print("3.  To Search For a Specific Event")
        print("4.  To Delete an Event")
        print("5.  To Add a Guest To a Specific Event")
        print("6.  To List All The Guests From a Specific Event")
        print("7.  To Search For a Specific Guest")
        print("8.  To Remove a Guest From an Event")
        print("9.  To Update a Guest's RSVP Status")
        print("10. To Filter Guests by RSVP Status")
        print("11. To Send Reminders to Guests With Pending RSVPs")
        print("12. To View Attendance Count for a Specific Event")
        print("13. To Save Events")
        print("14. To Load Events")
        print("15. To Export The Guest List to a CSV File")
        print("16. To Exit")
        
        user_input = input("\nPlease Enter The Number corresponding to your choice: ")#


        if user_input == "1":
            event_name = input("Enter Event Name: ")
            event_date = input("Enter Event Date (YYYY-MM-DD): ")
            description = input("Enter Event Description: ")
            location = input("Enter Event Location: ")
            event = Event(event_name, event_date, description, location)
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
                rsvp_status = input("Enter RSVP Status (Attending / Not Attending / Pending): ")
                event.add_guest(guest_name, guest_phone, guest_email, rsvp_status)


            else:
                print("Event Not Found")    


        elif user_input == "6":
            event_name = input("Enter Event Name: ")
            event = Event.search_event(event_name)
            if event:
                event.display_guests()

            else:
                print("Event Not Found")    


        elif user_input == "7":
            event_name = input("Enter Event Name: ")
            event = Event.search_event(event_name)
            if event:
                guest_email = input("Enter Guest Email to Search: ")
                event.search_guest(guest_email)

            else:
                print("Event Not Found")    


        elif user_input == "8":
            event_name = input("Enter Event Name: ")
            event = Event.search_event(event_name)
            if event:
                guest_email = input("Enter Guest Email to Remove: ")
                if event.remove_guest(guest_email):
                    print("Guest Removed Successfully")

                else:
                    print("Failed To Remove Guest")

            else:
                print("Event Not Found")            


        elif user_input == "9":
            event_name = input("Enter Event Name: ")
            event = Event.search_event(event_name)
            if event:
                guest_email = input("Enter Guest Email to Update RSVP: ")
                rsvp_status = input("Enter New RSVP Status (Attending / Not Attending / Pending): ")
                event.update_rsvp(guest_email, rsvp_status)

            else:
                print("Event Not Found")    


        elif user_input == "10":
            event_name = input("Enter Event Name: ")
            event = Event.search_event(event_name)
            if event:
                rsvp_status = input("Enter RSVP Status to Filter By: ")
                matching_guests = event.filter_by_rsvp(rsvp_status)
                if matching_guests:
                    print(f"Found {len(matching_guests)} Guests With Status '{rsvp_status}'")

                else:
                    print("No Guests Found With That Status")

            else:
                print("Event Not Found")            


        elif user_input == "11":
            event_name = input("Enter Event Name: ")
            event = Event.search_event(event_name)
            if event:
                event.send_reminder()

            else:
                print("Event Not Found")    


        elif user_input == "12":
            event_name = input("Enter Event Name: ")
            event = Event.search_event(event_name)
            if event:
                event.attendance_count()

            else:
                print("Event Not Found")    


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
                print("Event Not Found")    


        elif user_input == "16":
            save_choice = input("Do you want to save changes before exiting? (yes/no): ").strip().lower()
            if save_choice == "yes":
                Event.save_event()

            print("Exiting Event Planner")
            break


        else:
            print("Invalid, Please Try Again")

if __name__ == "__main__":
    main()            