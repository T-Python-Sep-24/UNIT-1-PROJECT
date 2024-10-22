import json
import os
from datetime import datetime , date
import time
from plyer import notification 
from rich.console import Console
from rich.table import Table
from rich import box
# check stauts + check menu ****
def main():
    print("==================== Salf Program ===========================")
    print("Users still borrower today ! ") 
    check_pay()
    print (f"Welcome to Salf Program" + "\n" + "Please Choose the below menu" + "\n" + "1. Add user to borrower" + "\n"+ "2. View borrower users" + "\n"+ "3. change users status")
    number = 9
    while number > 0:
        number=int(input("Please choose number "))
        if (number == 1):
            add_user()
        elif(number == 2):
            display_users()
        elif( number == 3):
            change_user_status()
        else:
            pass
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
  try:
        with open('users.json', 'r') as f:
            users= json.load(f)
            table= Table(title="[bold #d7d7ff]Lender Table[/]" , style="grey78" , box=box.MINIMAL_DOUBLE_HEAD)
            table.add_column("[#d7d7ff]ID[/]",justify="center",style="bold cadet_blue" , width=13)
            table.add_column("[#d7d7ff]name[/]",justify="center",style=" bold wheat1"  , width=13)
            table.add_column("[#d7d7ff]aoment[/]",justify="center",style=" bold cadet_blue" , width=13)
            table.add_column("[#d7d7ff]today[/]",justify="center",style="bold dark_sea_green2" , width=13)
            table.add_column("[#d7d7ff]pay_date[/]",justify="center",style=" bold dark_red" , width=13)
            table.add_column("[#d7d7ff]status[/]",justify="center",style=" bold wheat1" , width=13)
            for user in users:
                 table.add_row(str(user["ID"]),user["name"],str(user["aoment"]), str(user["today"]),str(user["pay_date"]),str(user["status"]))
            console=Console()
            console.print(table)
  except FileExistsError:
            users= []
#add count how many borrower
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
def check_pay():
    try:
        with open('users.json', 'r') as f:
            users= json.load(f)
    except FileExistsError:
            users= []

    today= date.today().strftime("%Y-%m-%d")
    for pay in users:
              if today >= pay["pay_date"] and pay["status"] != True:
                   notification.notify(
                        title = 'ALERT!!!',
                        message = f'Today {pay["name"]} should be paying',
                        timeout= 10
                        )
                   time.sleep(5)
                   print(f"Today {pay["name"]} should be paying !")
              else:
                   pass
#check_pay()
