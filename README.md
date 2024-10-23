# Hotel Management System

## Overview
The Hotel Management System is a Python application designed to facilitate the management of hotel bookings. It allows managers to add, edit, and manage hotel listings while providing customers with a user-friendly interface to search, book, and manage their hotel reservations. The system utilizes JSON for data persistence, ensuring that hotel information is saved and loaded effectively.

## User Stories
1. **As a Manager**, I want to:
   - Add new hotels with details such as name, location, rating, price per room, and availability.
   - Edit existing hotel details.
   - View a list of all available hotels.

2. **As a Customer**, I want to:
   - View all available hotels.
   - Search for hotels by name or location.
   - Book a hotel if rooms are available.
   - Remove a booking if I no longer need it.
   - View my booking history and checkout to receive a receipt.

3. **As a User**, I want to:
   - Receive hotel recommendations based on my booking history.

## Usage
1. **Installation**:
   - Ensure you have Python installed on your machine.
   - Clone this repository to your local machine.
   - Navigate to the project directory and install any required dependencies.

2. **Running the Application**:
   - Run the application using the command:
     ```bash
     python hotel_management_system.py
     ```
   - Follow the prompts to interact with the system as either a manager or a customer.

3. **Data Persistence**:
   - Hotel data is saved in a `hotels.json` file. The application will load this file upon startup and save changes after each operation.

4. **User Authentication**:
   - The manager's credentials are set to a predefined username and password (`manager` / `password123`). 

Feel free to modify or expand this README to include any additional details specific to your project!
