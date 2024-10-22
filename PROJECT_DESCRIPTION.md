# Electronic Device Rental Management System

## Overview:
This project is a CLI-based system for managing the rental of electronic devices. It supports two types of users: customers and managers. Customers can browse available devices, rent them, and return them,  The system uses JSON for data storage and aims to be efficient, user-friendly, and well-organized.

## Features:

### As a Customer:
- Browse available electronic devices.
- View detailed information about devices (name, brand, specs, price, and availability).
- Search for devices based on brand or type.
- Proceed to checkout to rent selected devices.
- Return rented devices.
- View the rental history and device availability.

### As a Manager:
- Add new devices to the inventory.
- Remove user 

## Usage:
- Type `list_devices` to see all available devices..
- Type `rent` to proceed with the rental of selected devices.
- Type `return device_name` to return a rented device.
- Type `log` to view the activity log (for managers).

## Technology:
- The project is developed using Python.
- Data storage is managed using JSON files.
- The `tabulate` library is used for table formatting.
- A virtual environment is set up for managing dependencies.
- Color formatting is used to enhance user interaction.
