from Player import Player
import pickle
import os
class Member(Player):
    def __init__(self,style: str,name:str,password:str) -> None:
        super().__init__(style)
        self.set_player_style('member')
        self.__memberData=self.__load_from_file('members.pkl')
        self.__name = name
        self.__password = password
        

              
    def record_new_member(self,name):
        #check names
        if self.is_name_taken(name):
            print("The name is taken. Choose another name.")
            input('Press Enter to continue >>>\n')
            return False
        if not self.is_name_taken(name):
            self.add_member()
            return True
        
    def sign_in_member(self,name):
        #check names and pass
        member_found=False 
        member_list= self.__load_from_file('members.pkl')
        for item in member_list:
            if item['name']==name and item['password']==self.get_member_password():
                member_found=True
                return member_found
        print("Your are not a member. Check from your name or password")
        input('Press Enter to continue >>>\n')
        return member_found
    # Setter & Getter    
    def set_member_name(self,name):
        self.__name = name

    def get_member_name(self):
        return self.__name 
    
    def set_member_password(self,password):
        self.__password = password

    def get_member_password(self):
        return self.__password 

    def get_memberData_list(self):
        return self.__memberData 

    def set_memberData_list(self,memberData):
        self.__memberData =  memberData
        self.__save_to_file("members.pkl")
    
    def __save_to_file(self, filename: str):
        try:
            with open(filename,'wb') as file:
                pickle.dump(self.__memberData,file)
        except Exception as e:
            print(f"Error saving data to file: {e}")        

    def __load_from_file(self, filename: str):
        try:
            with open(filename,'rb') as file:
                return pickle.load(file) 
        except (FileNotFoundError, EOFError):
            return []
        
    def is_name_taken(self,name):
        self.__memberData = self.__load_from_file('members.pkl') or []
        return any(member['name'] == name for member in self.__memberData)

    #Home page member function
    def home_page_member(self):

        members_list = self.__load_from_file('members.pkl')
        global member_name
        for part in members_list:
            if part['name']==self.get_member_name():
                member_name=part['name']
                break

        while True:
                os.system('cls')
                 # Welcoming the user by its name
                print(f"Hi {self.get_member_name().capitalize()}, Welcome to Our Galaxy 🌌")
                print(self.get_player_type())
                print("Home page (member)")
                
                #show his score
                self.display_member_score()
                print("1- Games")
                print("2- Community")
                #print("3- Achievements and badges (money)")
                #print("4- My purchases")
                print("5- Update my information")#Done
                print("6- Delete my membership")#Done
                print("0- Exit")#Done
                
                global player_choice2
                player_choice2=input("Your Choice: ")
                print()
                if player_choice2=="1":
                    #show games list
                    self.games_list()
                    os.system('cls')
                elif player_choice2=="2":
                    #display the community (can write)
                    self.write_chat_community()
                    pass
                elif player_choice2=="3":
                    #display Achievements and badges (money)
                    pass 
                elif player_choice2=="4":
                    #display the purchases (hints&adds)
                    pass
                elif player_choice2=="5":
                    #update info
                    os.system('cls')
                    self.update_info(member_name)

                elif player_choice2=="6":
                    #delete info
                    os.system('cls')
                    member_state=self.delete_member()
                    if  member_state:
                        break    
                elif player_choice2=="0":
                    break        
                else:
                    print("Invalid choice. Please try again.")
    
    def update_info(self,name:str):
        
        print("What you want to update?")
        print("1- Name\n2- Password")
        updated_info=input("Your Choice:")
        if updated_info=="1":
            member_list= self.__load_from_file('members.pkl')
            print(f"Current Name: {self.get_member_name().capitalize()}")
            new_name=input("Please enter your new name:")
            if self.is_name_taken(new_name):
                print(name)
                print(self.is_name_taken(new_name))
                print("The name is taken. Choose another name.")
                input('Press Enter to continue >>>\n')
                return
            self.set_member_name(new_name)
            for item in member_list:
                if item['name']==name:
                    print(item['name'])
                    item['name']=new_name
                    print(item['name'])
                    break
            self.__memberData = member_list   
            self.__save_to_file('members.pkl')    
            print("Awesome! Your name's been updated! 🎉")
            print(f"Updated Name: {self.get_member_name().capitalize()}")
            input('Press Enter to continue >>>\n')
        elif updated_info=="2": 
            member_list= self.__load_from_file('members.pkl')
            #check pass
            print(f"Current Password: {self.get_member_password()}")
            new_pass=input("Enter your new password (6 digits):")
            if  new_pass.isdigit() and len(new_pass)==6:   
            
                self.set_member_password(new_pass)
                for item in member_list:
                    if item['name']==name:
                        item['password']=new_pass
                        print(item['password'])
                        break
                self.__memberData = member_list    
                self.__save_to_file('members.pkl')
                print("Awesome! Your passwrod's been updated! 🎉")
                print(f"Updated Name: {self.get_member_password()}")
                input('Press Enter to continue >>>')
            else:
                print("Invalid password format.\nPlease enter password as 6 digits\n--------------------")
                input('Press Enter to continue >>>')   
    
   
    def add_member(self):
        member={
            "name":self.get_member_name(),
            "password":self.get_member_password(),
            "score":0
        }
        self.__memberData.append(member)
        self.__save_to_file('members.pkl')
        
             
    def delete_member(self):
        member_state=False
        print("Are you sure you want to delete your membership?")
        print("1- Yes\n2- No")
        player_choice=input("Your Choice: ")
        if player_choice=="1":
            member_list= self.__load_from_file('members.pkl')
            member_to_remove = self.get_member_name() 

            for item in member_list:
                if item['name'] == member_to_remove:  
                    member_list.remove(item)
                    break 

            self.__memberData = member_list[:]
            self.__save_to_file('members.pkl')
            print("Membership deleted successfully")
            member_state=True
            return member_state
        elif player_choice=="2":
            print("We are happy to continue with us...")
            input('Press Enter to continue >>>')
            return member_state
        else:
            print("Invalid choice. Please try again.")
            input('Press Enter to continue >>>')
            return member_state
    
    def display_member_score(self):
        member_list= self.__load_from_file('members.pkl')
        for item in member_list:
                if item['name'] == self.get_member_name():  
                    print(f"Your Score: ({item['score']})")
                    break 
        pass    
    
    


        


        

