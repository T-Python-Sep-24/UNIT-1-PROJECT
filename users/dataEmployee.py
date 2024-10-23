from users.identfyPerson import Person
import json 

class Employee(Person):
    def __init__(self, mainlist, name, employee_id, email, phone, position) -> None:
        super().__init__(name, employee_id, email, phone)
        self.position = position
        self.mainlist = mainlist 

    def add_data(self):
        user_id = input("Enter employee ID to add data for: ")
        employee_dict = self.mainlist[1]

        if user_id not in employee_dict:
            employee_dict[user_id] = {
                "name": self.name,
                "phone": self.phone,
                "email": self.email,
                "position": self.position
            }
            return "Done adding employee data"
        else:
            return f"Employee with ID {user_id} already exists."
    
    def remove_data(self):
        user_id = input("Enter employee ID to remove: ")
        employee_dict = self.mainlist[1]
        if user_id in employee_dict:
            del employee_dict[user_id]
            self.save_data(show_message=False)  # Don't show the save message
            return f"Employee with ID {user_id} has been removed."
        else:
             return f"Employee with ID {user_id} not found."
        
    def search_data(self):
        user_id = input("Enter employee ID to search: ")
        employee_dict = self.mainlist[1]
        if user_id in employee_dict:
            employee_info = employee_dict[user_id]
            return f"Employee found: Name: {employee_info['name']}, Email: {employee_info['email']}, Phone: {employee_info['phone']}, Position: {employee_info['position']}"
        else:
            return f"Employee with ID {user_id} not found."
    
    def display_data(self):
        employee_dict = self.mainlist[1]
        if employee_dict:
            user_id = input("Enter employee ID to display data for: ")
            if user_id in employee_dict:
                employee_info = employee_dict[user_id]
                print(f"ID: {user_id}, Name: {employee_info['name']}, Email: {employee_info['email']}, Phone: {employee_info['phone']}, Position: {employee_info['position']}")
            else:
                 print(f"No employee found with ID {user_id}.")
        else:
            print("No employee data found.")

    def save_data(self,show_message=True):
        with open("information.json", "w", encoding="UTF-8") as file:
            json.dump(self.mainlist, file, indent=4)
        if show_message:
            print("Employee data has been saved to 'information.json'.")

    def load_data(self):
        try:
            with open("information.json","r", encoding="UTF-8") as file:
                self.mainlist = json.load(file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No existing data found.")

    