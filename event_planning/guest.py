
import re

class Guest:
    def __init__(self, guest_name:str, guest_phone:int, guest_email:str, rsvp_status:str = "Pending"):
        self.guest_name = guest_name
        self.rsvp_status = rsvp_status #Will include "Attending", "Not Attending", "Pending"
        
        #Phone Number Validation: Must Be Digits Only and 10 Characters Long
        self.guest_phone = str(guest_phone)
        
        if not re.fullmatch(r"\d{10}", guest_phone):
            raise ValueError(f"Invalid phone number '{guest_phone}'. It should contain exactly 10 digits.")
            
        
        #Email Validation: Must End With "gmail", "hotmail" or "Outlook"
        if re.fullmatch(r".+@(gmail|hotmail| outlook)\\.com$", guest_email):
            self.guest_email = guest_email
        
        else:
            raise ValueError(f"Invalid Email Address. The '{guest_email}' Should End With 'gmail', 'hotmail', or 'outlook'.")


    def __str__(self):
        return (
            f"Guest Name: {self.guest_name}\n"
            f"Phone: {self.guest_phone}\n"
            f"Email: {self.guest_email}\n"
            f"RSVP: {self.rsvp_status}\n"
            + "=" * 30 #Check 
        )    