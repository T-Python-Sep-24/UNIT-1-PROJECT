from datetime import datetime, timedelta
from rich.console import Console
from rich.text import Text
import json
console = Console()

class RentalManager:
    def __init__(self, device_manager):
        """Initialize the rental manager and load rentals from JSON."""
        self.rentals = []
        self.device_manager = device_manager

    def load_rentals(self):
        """Load rentals from a JSON file."""
        try:
            with open('rentals.json', 'r', encoding="UTF-8") as file:
                self.rentals = json.load(file)
        except FileNotFoundError:
            self.rentals = []

    def save_rentals(self):
        """Save rentals to a JSON file."""
        with open('rentals.json', 'w') as file:
            json.dump(self.rentals, file, indent=4)

    def rent_device(self, device_name, renter_name, start_date, end_date):
        """Rent a device to a user."""
        for device in self.device_manager.devices:
            if device['name'] == device_name and device['available']:
                new_rental = {
                    "device_name": device_name,
                    "renter_name": renter_name,
                    "start_date": start_date,
                    "end_date": end_date
                }
                self.rentals.append(new_rental)
                self.device_manager.update_availability(device_name, False)
                self.save_rentals()
                console.print(f"Device {device_name} rented successfully to {renter_name}.", style="bold green")
                return
        console.print(f"Device {device_name} is not available for rent.", style="bold red")

    def check_approaching_returns(self, days_before=2):
        """Check for rentals that are approaching their return date."""
        current_date = datetime.now().date()

        # Iterate through rentals and check the return date
        for rental in self.rentals:
            end_date = datetime.strptime(rental['end_date'], "%Y-%m-%d").date()
            days_until_due = (end_date - current_date).days

            if 0 < days_until_due <= days_before:
                alert_text = Text(f"Reminder: Device '{rental['device_name']}' rented by {rental['renter_name']} is due in {days_until_due} day(s).", style="bold yellow")
                console.print(alert_text)
            elif days_until_due == 0:
                console.print(f"Device '{rental['device_name']}' rented by {rental['renter_name']}' is due TODAY!", style="bold red")

    def return_device(self, device_name):
        """Return a rented device and update its availability."""
        for rental in self.rentals:
            if rental['device_name'] == device_name:
                self.rentals.remove(rental)
                self.device_manager.update_availability(device_name, True)
                self.save_rentals()
                console.print(f"Device {device_name} returned successfully.", style="bold green")
                return
        console.print(f"No rental found for device {device_name}.", style="bold red")
