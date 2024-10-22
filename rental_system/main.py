from device import DeviceManager
from user import UserManager
from rental import RentalManager
from billing import BillingManager
from colorama import Fore, Style
from rich.console import Console

from rich.prompt import Prompt

console = Console()

def main():
    
    device_manager = DeviceManager()
    user_manager = UserManager()
    rental_manager = RentalManager(device_manager)
    billing_manager = BillingManager(rental_manager)

    
    device_manager.load_devices()
    user_manager.load_users()
    rental_manager.load_rentals()

    console.print("[cyan]Welcome to the Electronic Device Rental Management System![/cyan]")

    logged_in_role = None

    while True:
        if logged_in_role is None:
           
            console.print("\n1. [green]Add User[/green]")
            console.print("2. [green]Login[/green]")
            console.print("3. [red]Exit[/red]")
            
            choice = Prompt.ask("Select an option")

            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                role = input("Enter role (User/Admin): ")
                user_manager.add_user(username, password, role)

            elif choice == '2':
                username = input("Enter username: ")
                password = input("Enter password: ")
                logged_in_role = user_manager.authenticate_user(username, password)

            elif choice == '3':
                console.print("[yellow]Exiting the system...[/yellow]")
                break

            else:
                console.print(Fore.RED + "Invalid option! Please try again." + Style.RESET_ALL)

        else:
            if logged_in_role == "Admin":
               
                console.print("\n1. [green]Add Device[/green]")
                console.print("2. [green]List Devices[/green]")
                console.print("3. [green]Rent Device[/green]")
                console.print("4. [green]Return Device[/green]")
                console.print("5. [green]Generate Bill[/green]")
                console.print("6.[green] Check Approaching Returns[/green]")
                console.print("7. [green]Delete User[/green]")
                console.print("8. [red]Logout[/red]")
              

                choice = Prompt.ask("Select an option")

                if choice == '1':
                    name = input("Enter device name: ")
                    model = input("Enter device model: ")
                    daily_price = float(input("Enter daily rental price: "))
                    device_manager.add_device(name, model, daily_price)

                elif choice == '2':
                    device_manager.list_devices()

                elif choice == '3':
                    device_name = input("Enter device name: ")
                    renter_name = input("Enter your name: ")
                    start_date = input("Enter start date (YYYY-MM-DD): ")
                    end_date = input("Enter end date (YYYY-MM-DD): ")
                    rental_manager.rent_device(device_name, renter_name, start_date, end_date)

                elif choice == '4':
                    device_name = input("Enter device name: ")
                    rental_manager.return_device(device_name)

                elif choice == '5':
                    rental_id = input("Enter rental ID: ")
                    billing_manager.generate_bill(rental_id)

                elif choice == '6':
                    rental_manager.check_approaching_returns()
                
                elif choice == '7':  
                    username = input("Enter username to delete: ")
                    user_manager.delete_user(username)

                elif choice == '8':
                    logged_in_role = None  
                    console.print("[yellow]You have logged out.[/yellow]")
                else:
                    console.print(Fore.RED + "Invalid option! Please try again." + Style.RESET_ALL)

            elif logged_in_role == "User":
               
                console.print("\n1. [green]List Devices[/green]")
                console.print("2. [green]Rent Device[/green]")
                console.print("3. [green]Return Device[/green]")
                console.print("4. [green]Generate Bill[/green]")
                console.print("5. [red]Logout[/red]")

                choice = Prompt.ask("Select an option")

                if choice == '1':
                    device_manager.list_devices()

                elif choice == '2':
                    device_name = input("Enter device name: ")
                    renter_name = input("Enter your name: ")
                    start_date = input("Enter start date (YYYY-MM-DD): ")
                    end_date = input("Enter end date (YYYY-MM-DD): ")
                    rental_manager.rent_device(device_name, renter_name, start_date, end_date)

                elif choice == '3':
                    device_name = input("Enter device name: ")
                    rental_manager.return_device(device_name)

                elif choice == '4':
                    rental_id = input("Enter rental ID: ")
                    billing_manager.generate_bill(rental_id)

                elif choice == '5':
                    logged_in_role = None  
                    console.print("[yellow]You have logged out.[/yellow]")
                else:
                    console.print(Fore.RED + "Invalid option! Please try again." + Style.RESET_ALL)

        
        device_manager.save_devices()
        user_manager.save_users()
        rental_manager.save_rentals()

if __name__ == "__main__":
    main()
