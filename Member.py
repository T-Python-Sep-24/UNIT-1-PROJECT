from Player import Player
import pickle
import os
import colorama
#clear function
def clear_screen():
    # Clear the terminal screen for Windows or Unix/Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

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
            print(colorama.Fore.RED+"The name is taken. Choose another name.")
            input(colorama.Fore.WHITE+'Press Enter to continue >>>\n')
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
        print(colorama.Fore.RED+"Your are not a member. Check from your name or password")
        input(colorama.Fore.WHITE+'Press Enter to continue >>>\n')
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
            print(colorama.Fore.RED+f"Error saving data to file: {e}")        

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
                print(f"Hi {colorama.Fore.MAGENTA+self.get_member_name().capitalize()+colorama.Fore.RESET}, Welcome to Our Galaxy 🌌\n")
                print(colorama.Back.WHITE+colorama.Fore.BLACK+"HOME PAGE"+colorama.Back.RESET,"\n")

                
                #show his score
                self.display_member_score()
                print(colorama.Fore.BLUE+"1- Games")
                print(colorama.Fore.BLUE+"2- Community")
                print(colorama.Fore.BLUE+"3- Update my information")
                print(colorama.Fore.BLUE+"4- Delete my membership")
                print(colorama.Fore.RED+"0- Exit")
                
                global player_choice2
                player_choice2=input(colorama.Fore.WHITE+"Your Choice: ")
                if player_choice2=="1":
                    #show games list
                    self.games_list()
                    clear_screen()
                elif player_choice2=="2":
                    #display the community (can write)
                    self.write_chat_community()
                    clear_screen()
                elif player_choice2=="3":
                    #update info
                    clear_screen()
                    self.update_info(member_name)

                elif player_choice2=="4":
                    #delete info
                    clear_screen()
                    member_state=self.delete_member()
                    if  member_state:
                        break    
                elif player_choice2=="0":
                    break        
                else:
                    print(colorama.Fore.RED+"Invalid choice. Please try again.")
                    input(colorama.Fore.WHITE+'Press Enter to continue >>>\n') 
    
    def update_info(self,name:str):
        
        print("What you want to update?")
        print(colorama.Fore.BLUE+"1- Name\n2- Password")
        updated_info=input(colorama.Fore.WHITE+"Your Choice:")
        if updated_info=="1":
            member_list= self.__load_from_file('members.pkl')
            print(f"Current Name: {self.get_member_name().capitalize()}")
            new_name=input(colorama.Fore.BLUE+"Please enter your new name:"+colorama.Fore.RESET)
            if self.is_name_taken(new_name):
                print(colorama.Fore.RED+"The name is taken. Choose another name.")
                input(colorama.Fore.WHITE+'Press Enter to continue >>>\n')
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
            print(colorama.Fore.GREEN+"Awesome! Your name's been updated! 🎉",colorama.Fore.RESET)
            print(colorama.Fore.BLUE+f"Updated Name: {self.get_member_name().capitalize()}")
            input(colorama.Fore.WHITE+'Press Enter to continue >>>\n')
        elif updated_info=="2": 
            member_list= self.__load_from_file('members.pkl')
            #check pass
            print(f"Current Password: {self.get_member_password()}")
            new_pass=input(colorama.Fore.BLUE+"Enter your new password (6 digits):"+colorama.Fore.RESET)
            if  new_pass.isdigit() and len(new_pass)==6:   
            
                self.set_member_password(new_pass)
                for item in member_list:
                    if item['name']==name:
                        item['password']=new_pass
                        print(item['password'])
                        break
                self.__memberData = member_list    
                self.__save_to_file('members.pkl')
                print(colorama.Fore.GREEN+"Awesome! Your passwrod's been updated! 🎉")
                print(colorama.Fore.BLUE+f"Updated Name: {self.get_member_password()}")
                input(colorama.Fore.WHITE+'Press Enter to continue >>>')
            else:
                print(colorama.Fore.RED+"Invalid password format.\nPlease enter password as 6 digits\n--------------------")
                input(colorama.Fore.WHITE+'Press Enter to continue >>>')   
    
   
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
        print(colorama.Fore.BLUE+"1- Yes\n2- No")
        player_choice=input(colorama.Fore.WHITE+"Your Choice: ")
        if player_choice=="1":
            member_list= self.__load_from_file('members.pkl')
            member_to_remove = self.get_member_name() 

            for item in member_list:
                if item['name'] == member_to_remove:  
                    member_list.remove(item)
                    break 

            self.__memberData = member_list[:]
            self.__save_to_file('members.pkl')
            print(colorama.Fore.GREEN+"Membership deleted successfully")
            member_state=True
            return member_state
        elif player_choice=="2":
            print(colorama.Fore.BLUE+"We are happy to continue with us...")
            input(colorama.Fore.WHITE+'Press Enter to continue >>>')
            return member_state
        else:
            print(colorama.Fore.RED+"Invalid choice. Please try again.")
            input(colorama.Fore.WHITE+'Press Enter to continue >>>')
            return member_state
    
    def display_member_score(self):
        member_list= self.__load_from_file('members.pkl')
        for item in member_list:
                if item['name'] == self.get_member_name():  
                    print(colorama.Fore.WHITE+f"Your Score: ({colorama.Fore.WHITE+str(item['score'])})")
                    break 

    def display_best_players(self):
       try:
            best_scores=[]
            members=self.__memberData
            members.sort(key=lambda x: x["score"],reverse=True)
            for r in range(0,min(3, len(members))):  
                best_scores.append(members[r])    
            return colorama.Fore.RESET+f"Best Players  🌟: {colorama.Fore.YELLOW+(best_scores[0]["name"]).capitalize()} : {best_scores[0]["score"]}, \
    {(best_scores[1]["name"]).capitalize()}: {best_scores[1]["score"]}, \
    {(best_scores[2]["name"]).capitalize()} : {str(best_scores[2]["score"])+colorama.Fore.RESET}"
       except IndexError :
           print(colorama.Fore.RED +"There is no enough players")
           input(colorama.Fore.WHITE+'Press Enter to continue >>>')
    
    


        


        

