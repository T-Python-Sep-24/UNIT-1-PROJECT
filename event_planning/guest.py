## Created a class called Guest that will include guest name, guest phone, guest email, and guest RSVP

import re
from termcolor import colored

class Guest:
    def __init__(self, guest_name:str, guest_phone:int, guest_email:str, rsvp_status:str = "Pending"):
        self.guest_name = guest_name
        self.rsvp_status = rsvp_status #Will include "Attending", "Not Attending", "Pending"
        
        #Convert guest_phone to a string for validation
        guest_phone = str(guest_phone)
        
        #Phone Number Validation: Must be digits only and 10 characters long
        if not re.fullmatch(r"\d{10}", guest_phone):
            raise ValueError(colored(f"Invalid Phone Number '{guest_phone}'. It Should Contain Exactly 10 Digits.", "red"))
        
        else:
            self.guest_phone = guest_phone
            
        

        #Email Validation: Must End With "gmail", "hotmail" or "Outlook"
        if re.fullmatch(r".+@(gmail|hotmail|outlook)\.com$", guest_email):
            self.guest_email = guest_email
        
        else:
            raise ValueError(colored(f"Invalid Email Address. The '{guest_email}' Should End with 'gmail.com', 'hotmail.com', or 'outlook.com'.", "red"))


    def __str__(self):
        return (
            f"Guest Name: {self.guest_name}\n"
            f"Phone: {self.guest_phone}\n"
            f"Email: {self.guest_email}\n"
            f"RSVP: {self.rsvp_status}\n"
            + "=" * 30 
        )    