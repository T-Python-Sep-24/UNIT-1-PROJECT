

class Guest:
    def __init__(self, guest_name:str, guest_phone:int, guest_email:str, rsvp_status:str = "Pending"):
        self.guest_name = guest_name
        self.guest_phone = guest_phone
        self.guest_email = guest_email
        self.rsvp = rsvp_status #will include "Attending", "Not Attending", "Pending"


    def __str__(self):
        return f"Guest Name: {self.guest_name}, Phone: {self.guest_phone}, Email: {self.guest_email}, RSVP: {self.rsvp}"    