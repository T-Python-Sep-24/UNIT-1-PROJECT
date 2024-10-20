from event_planning.event import Event
from event_planning.guest import Guest

def main():
    
    print("-------------- Welcom To Your Event Planner --------------")
    print("-" * 60)


    while True:
        print("\nMain Menu:")
        print("1. To Create a New Event")
        print("2. To View All Events")
        print("3. To Search For a Specific Event")
        print("4. To Delete an Event")
        print("5. To Add a Guest To a Specific Event")
        print("6. To List All Guests For a Specific Event")
        print("7. To Search For a Specific Guest")
        print("8. To Remove a Guest From an Event")
        print("9. To Update a Guest's RSVP Status")
        print("10. To Filter Guests by RSVP Status")
        print("11. To Send Reminders to Guests With Pending RSVPs")
        print("12. To View Attendance Count for an Event")
        print("13. To Save Events")
        print("14. To Load Events")
        print("15. To Export The Guest List to a CSV File")
        print("16. To Exit")
        
        user_input = input("Please enter the number corresponding to your choice: ")


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
            Event.search_event(event_name)


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
                guest = Guest(guest_name, guest_phone, guest_email, rsvp_status)
                event.add_guest(guest)


        elif user_input == "6":
            event_name = input("Enter Event Name: ")
            event = Event.search_event(event_name)
            if event:
                event.display_guests()


        elif user_input == "7":
            event_name = input("Enter Event Name: ")
            event = Event.search_event(event_name)
            if event:
                guest_email = input("Enter Guest Email to Search: ")
                event.search_guest(guest_email)


        elif user_input == "8":
            event_name = input("Enter Event Name: ")
            event = Event.search_event(event_name)
            if event:
                guest_email = input("Enter Guest Email to Remove: ")
                event.remove_guest(guest_email)


        elif user_input == "9":
            event_name = input("Enter Event Name: ")
            event = Event.search_event(event_name)
            if event:
                guest_email = input("Enter Guest Email to Update RSVP: ")
                rsvp_status = input("Enter New RSVP Status (Attending / Not Attending / Pending): ")
                event.update_rsvp(guest_email, rsvp_status)


        elif user_input == "10":
            event_name = input("Enter Event Name: ")
            event = Event.search_event(event_name)
            if event:
                rsvp_status = input("Enter RSVP Status to Filter By: ")
                event.filter_by_rsvp(rsvp_status)


        elif user_input == "11":
            event_name = input("Enter Event Name: ")
            event = Event.search_event(event_name)
            if event:
                event.send_reminder()


        elif user_input == "12":
            event_name = input("Enter Event Name: ")
            event = Event.search_event(event_name)
            if event:
                event.attendance_count()


        elif user_input == "13":
            filename = input("Enter File Name to Save Event: ")
            event.save_event(filename)


        elif user_input == "14":
            filename = input("Enter File Name to Load Event: ")
            event.load_event(filename)            


        elif user_input == "15":
            event_name = input("Enter Event Name: ")
            event = Event.search_event(event_name)
            if event:
                filename = input("Enter File Name to Export (guest_list.csv): ")
                event.export_guest_to_csv(filename)


        elif user_input == "16":
            print("Exit Event Planner")
            break


        else:
            print("Invalid, Please Try Again")

if __name__ == "__main__":
    main()            