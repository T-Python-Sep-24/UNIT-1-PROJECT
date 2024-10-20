from event_planning.event import Event
from event_planning.guest import Guest

def main():

    event = Event()
    guest = Guest()
    
    print("-------------- Welcom To Your Event Planner --------------")
    print("-" * 30)


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
        print("12. To Export The Guest List to a CSV File")
        print("13. Exit")
        
        user_iput = input("Please enter the number corresponding to your choice: ")


        if user_iput == "1":
            pass

        elif user_iput == "2":
            pass

        elif user_iput == "3":
            pass

        elif user_iput == "4":
            pass

        elif user_iput == "5":
            pass

        elif user_iput == "6":
            pass

        elif user_iput == "7":
            pass

        elif user_iput == "8":
            pass

        elif user_iput == "9":
            pass

        elif user_iput == "10":
            pass

        elif user_iput == "11":
            pass

        elif user_iput == "12":
            pass

        elif user_iput == "13":
            print("Exit Event Planner")
            break

        else:
            print("Invalid, Please Try Again")