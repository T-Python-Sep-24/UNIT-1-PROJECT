import os
import pickle

class Employee:
    def __init__(self, name:str, username:str, password:str):
        self.name = name
        self.username = username
        self.__password = password
        
    def get_password(self):
        return self.__password


class RegisterLoginEmploee:
    def __init__(self):
        self.emploees = self.load_from_file()
        if not isinstance(self.emploees, dict):
            self.emploees = {}
        
    def register_emploee(self, emploee: Employee, secretCode:str):
        if secretCode != 'carfixer':
            if isinstance(emploee, Employee):
                if emploee.username not in self.emploees:
                    self.emploees[emploee.username] = emploee
                    print(f"{emploee.name} your registered successfully!")
                    self.save_to_file()
                    return True
                else:
                    print("Username already exists!")
                    return False
                
            print('Employee data has some mistake!')
            return False
        
        print('Employees secret code is incorrect!')
        return False
        
    def login_emploee(self, username: str, password: str):
        if username in self.emploees:
            if password == self.emploees[username].get_password():
                return self.emploees[username]
        return None
    
    def get_emploee(self, username: str):
        return self.emploees.get(username)
    
    def save_to_file(self):
        with open("emploees_data", 'wb') as file:
            pickle.dump(self.emploees, file)

    def load_from_file(self):
        if not os.path.exists("emploees_data"):
            return {}  
        
        with open("emploees_data", 'rb') as file:
            try:
                data = pickle.load(file)
                if not isinstance(data, dict):
                    return {}
                return data
            except Exception as e:
                print(f"Error loading emploees data: {e.__cause__}")
                return {}

