from datetime import date
import time
from plyer import notification
import json
#change the text to json+ stauts + method check the id ** after that view the menu **  

'''file = "users_borrower.txt"
dict={}
with open(file) as fn:
    for d in fn:
        key, desc=d.strip().split(None,1)
        dict[key]=desc.strip()
otfile=open("users.json","w")
json.dump(dict,otfile)
otfile.close()'''

def main():
    print("==================== Salf Program ===========================")
    print("Users still borrower today ! ") 
    check_pay()
    print (f"Welcome to Salf Program" + "\n" + "Please Choose the below menu" + "\n" + "1. Add user to borrower" + "\n"+ "2. View borrower users" + "\n"+ "3. change users status")
    number = 9
    while number > 0:
        number=int(input("Please choose number "))
        if (number == 1):
            salf_users()
        elif(number == 2):
            displsy()
        elif( number == 3):
            user_status()
        else:
            pass
def check_ID():
    pass
def salf_users():
       while True: 
        name=input("Enter the name of borrower : ")
        today= date.today().strftime("%Y-%m-%d")
        date_str=str(today)
        pay_day=input("Enter the payday : ")
        borrower_value=input("Enter the value :")
        stauts = "Not Pay"
        file = open('users_borrower.txt', "a", encoding="utf-8")
        file.write("Name of borrower : "+ name + " | "+ "The date : "+date_str +" | "+"The value : "+ borrower_value + " SAR"+ "| " +"Payday : "+ pay_day +" Stauts : "+ stauts+"\n")
        file.close()
        #print("User added succefully")
        break
       
def displsy():
    file=open('users_borrower.txt')
    print(file.read())
    file.close()

#change status 
def user_status():
     with open('users_borrower.txt', "r") as file:
        value= input("user name to change the status ")
        lines = ''
        for line in file:
            values=line.split()
            if value == values[4]:
              lines += line.replace("Not Pay", "paid")
              print( "The status has been change "  + "\n" + lines )
            else:
                lines += line
        file.close()
        file_write= open("users_borrower.txt", 'w')
        file_write.write(lines)
        file_write.close()
              
           

#def check for alert , stauts **
def check_pay():
    today= date.today().strftime("%Y-%m-%d")
    with open('users_borrower.txt','r')as file:
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
               pass



#Check the date is val 
'''def valdate(input):
    try:
        dateobject=datetime.strptime(input,"%d/%m/%Y")
        return True
    except ValueError:
        ValueError

input="09/05/2022"
print(valdate(input))'''
