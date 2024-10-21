import json
import os
from datetime import datetime , date
import time


# Def user add
def add_user():
    try:
        with open('users.json', 'r') as f:
            users= json.load(f)
    except FileExistsError:
            users= []
    exitee = True
    while exitee:
        userid= int(input("Enter user ID: "))
        user_found = False
        user_doesnot_exit=False
        for user in users:
            if user["ID"] == userid and user["status"] == True:
                    user_found= True
                    username= user["name"]
                    useramount=user["aoment"]
                    statuss= False
                    user_doesnot_exit=True
                    break
            elif user["ID"] == userid and user["status"] == False:
                    print(" You did not paied! We can't lend you money untill you paied !! ")
                    user_doesnot_exit = False
                    break
            elif user["ID"] != userid:
                    user_doesnot_exit = True
        
        if user_doesnot_exit :
                for user in users:
                    if user_found:
                        today=date.today().strftime("%Y-%m-%d")
                        pay_date=input("When the user will be pay Date: ")
                        new_user={
                                "ID": userid,
                                "name": username,
                                "aoment": useramount,
                                "today": today,
                                "pay_date":pay_date,
                                "status":statuss
                            }
                        users.append(new_user)
                        with open('users.json', 'w') as f:
                                json.dump(users, f, indent=4)
                                print("Users added")
                                break
                    else:
                        name= input("Enter user name: ")
                        aoment=int(input("Enter user amount: "))
                        today=date.today().strftime("%Y-%m-%d")
                        pay_date=input("When the user will be pay Date: ")
                        status= False
                        new_user={
                                "ID": userid,
                                "name": name,
                                "aoment": aoment,
                                "today": today,
                                "pay_date":pay_date,
                                "status":status
                            }
                            
                        users.append(new_user)
                        with open('users.json', 'w') as f:
                            json.dump(users, f, indent=4)
                            print("Users added")
                            break

        exite=int(input("Enter another user or exite by enter 0: "))
        if exite == 0:
            break
        

#User add: 
#add_user()
#display users    
def display_users():
     with open('users.json')as file:
          data=json.loads(file.read())
          print(json.dumps(data, indent=4))
#display_users()



#def change stauts ===================
def change_user_status(user_id):
     try:
        with open('users.json', 'r') as f:
            users= json.load(f)
     except FileExistsError:
            users= []
     user_id_not_found= True
     user_new = []
     for user in users: 
          if user["ID"] == user_id:
               user["status"] = True
               user_id_not_found= False
               name_user=user["name"] 
               user_new.append(user)
          else:
               user_new.append(user)

     with open('users.json', 'w') as f:
         json.dump(user_new, f, indent=4)
     print(f"User ID {user_id}'s and Users {name_user}'s status updated to paied ")
               
          
     if user_id_not_found:
        print(f"User ID {user_id}'s not found")
        
userid= int(input("Enter user ID: "))
change_user_status(userid)


#def check pay alert ***
'''def check_pay():
    today= date.today().strftime("%Y-%m-%d")
    with open('users.json','r')as file:
       data=json.load(file)
       for line in file:
           values=line.split()
           if today >= values[18]:
               notification.notify(
                title = 'ALERT!!!',
                message = f'Today {values[4]} should be paying',
                timeout= 10
                )
               time.sleep(5)
               print("Today " + values[4] + " should be paying !")
           else:
               pass'''