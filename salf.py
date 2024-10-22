import json
from datetime import date
import time
from plyer import notification 
from rich.console import Console 
from rich.table import Table
from rich import box
# check stauts + check menu ****
def main():
    console=Console()
    console.print("================================================================================" , style="bold cadet_blue" , justify="center")
    console.print("================================ Salf Reminder =================================" , style="bold cadet_blue" , justify="center")
    console.print("================================================================================" , style="bold cadet_blue" , justify="center")
    console.print("Users must repay the borrowed amounts today ! " , style="bold white" , justify="center") 
    check_pay()
    console.print (f"Welcome to Salf Program"  , style="bold cadet_blue" , justify="center")
    number = 9
    while number > 0:
        console=Console()
        console.print (f"Please Choose the below menu: " + "\n" + "1. Add user to the borrower list" + "\n"+ "2. View borrower users" + "\n"+ "3. Change user status to paid" , style="bold cadet_blue" , justify="center")
        try:
          number=int(input("Please choose number from the menu or enter 0 to exist:  "))
        except ValueError:
          print("Enter integer number !")
        if (number == 1):
             add_user()
        elif(number == 2):
             display_users()
        elif( number == 3):
            userid= int(input("Enter user ID: "))
            change_user_status(userid)
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
                    statuss= False
                    user_doesnot_exit=True
                    
            elif user["ID"] == userid and user["status"] == False:
                    print(" You did not paied! We can't lend you money untill you paied !! ")
                    user_doesnot_exit = False
                    break

            elif user["ID"] != userid:
                    user_doesnot_exit = True
        
        if user_doesnot_exit:
                for user in users:
                    if user_found:
                        today=date.today().strftime("%Y-%m-%d")
                        pay_date=input("When the user will be pay Date: ")
                        aoment=int(input("Enter user amount: "))
                        new_user={
                                "ID": userid,
                                "name": username,
                                "aoment": aoment,
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


#display users    
def display_users():
  try:
        with open('users.json', 'r') as f:
            users= json.load(f)
            table= Table(title="[bold #d7d7ff]Lender Table[/]" , style="grey78" , box=box.MINIMAL_DOUBLE_HEAD )
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
          if user["ID"] == user_id :
               user["status"] = True
               user_id_not_found= False
               name_user=user["name"] 
               user_new.append(user)
          else:
               user_new.append(user)
     
     console=Console()
     if user_id_not_found:
        return console.print(f"User ID {user_id}'s not found" , style=" bold red" , justify="center") 
     else:
        with open('users.json', 'w') as f:
            json.dump(user_new, f, indent=4)
        print(f"User ID {user_id}'s and Users {name_user}'s status updated to paied ")         
          


#def check pay alert ***
def check_pay():
    try:
        with open('users.json', 'r') as f:
            users= json.load(f)
    except FileExistsError:
            users= []
    console=Console()
    today= date.today().strftime("%Y-%m-%d")
    for pay in users:
              if today >= pay["pay_date"] and pay["status"] != True:
                   notification.notify(
                        title = 'Salf Reminder',
                        message = f'Today {pay["name"]} should be paying',
                        timeout= 10
                        )
                   time.sleep(5)
                   console.print(f"! Today {pay["name"]} should be paying !" , style=" bold red" , justify="center")
              else:
                   pass
