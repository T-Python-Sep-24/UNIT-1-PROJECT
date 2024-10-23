# UNIT-1-PROJECT

Tuwaiq Airport Management System
Overview
The Tuwaiq Airport Management System is a Python-based application designed to manage employees, travelers, and flights efficiently. The system allows users to manage employee records, handle traveler reservations, and organize flight schedules with permissions tailored to different roles, such as managers and employees.

Features
Employee Management:
Add, remove, search, and display employee data.
Employees can have attributes such as name, ID, email, phone number, and position.
Employee data is saved and loaded from the information.json file.
Permissions are handled to ensure only managers can modify certain flight data.

Traveler Management:
Add, remove, search, and display traveler data.
Travelers can make reservations, cancel them, and search for flights.
The system ensures smooth handling of traveler data, which is saved in information.json.


Traveler Management:
Add, remove, search, and display traveler data.
Travelers can make reservations and search for flights.
The system ensures smooth handling of traveler data, which is saved in information.json.


Folder Structure:
main.py: The main entry point for the application. This script handles the system's navigation, allowing users to manage employees, travelers, and flights.

users/:
dataEmployee.py: Handles all employee-related operations like adding, removing, searching, and displaying employee records.
dataCustomerOrTraveler.py: Manages traveler data, including reservations and flight interactions.
identfyPerson.py: Base class for both employees and travelers, providing shared attributes such as name, ID, and email.

flightServices/:
flights.py: Manages traveler interactions with flights, including flight reservation.
flightsM.py: Manages flight data for the system, such as adding, removing, and searching flights.
Technologies
Python: The project is built using Python, making use of Python's object-oriented programming (OOP) features.
JSON: For data storage and retrieval using the information.json file to persist information about employees, travelers, and flights.