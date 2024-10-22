import json
from tabulate import tabulate
from colorama import Fore,Style
from rich.console import Console
from rich.table import Table

class DeviceManager:
    def __init__(self):
        self.devices = [] 
        self.consle=Console()

    

    def load_devices(self):
        
        try:
            with open('devices.json', 'r', encoding='UTF-8') as file:
                self.devices = json.load(file)
        except FileNotFoundError:
            self.devices = []
            



    
    
    
    
    def save_devices(self):
        with open('devices.json', 'w', encoding='UTF-8') as file:
            json.dump(self.devices, file, indent=4)

    

    def add_device(self, name, model, daily_price):
        new_device = {
            'name': name,
            'model': model,
            'daily_price': daily_price,
            'available': True
        }
        self.devices.append(new_device)
        print(Fore.GREEN,f"Device {name} added successfully."+Style.RESET_ALL)
    
    def list_devices(self):
       
        if not self.devices:
            print(Fore.RED,"No devices available."+Style.RESET_ALL)
            return
        table = []
        for device in self.devices:
            status = "Available" if device['available'] else "Unavailable"
            table.append([device['name'], device['model'], device['daily_price'], status])

        headers = ["Device Name", "Model", "Daily Price", "Status"]
        print(tabulate(table, headers, tablefmt="grid"))


    def update_availability(self, device_name, available):
       
        for device in self.devices:
            if device['name'] == device_name:
                device['available'] = available
                self.save_devices()
                return
        print(f"Device {device_name} not found.")


        