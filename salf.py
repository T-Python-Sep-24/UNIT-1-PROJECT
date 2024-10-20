from datetime import date
import time
from plyer import notification

def salf_users():
       while True: 
        name=input("Enter the name of borrower :")
        today= date.today().strftime("%Y-%m-%d")
        date_str=str(today)
        pay_day=input("Enter the payday : ")
        borrower_value=input("Enter the value :")
        stauts=input("Enter the stauts")
        file = open('users_borrower.txt', "a", encoding="utf-8")
        file.write("Name of borrower : "+ name + " | "+ "The date : "+date_str +" | "+"The value : "+ borrower_value + " SAR"+ "| " +"Payday : "+ pay_day +" Stauts : "+ stauts+"\n")
        file.close()
        file=open('users_borrower.txt')
        print(file.read())
        file.close()
        return salf_users
#def check for alert
def check_pay(today , pay_day , name):
    if today in pay_day:
        notification.notify(
            title = 'ALERT!!!',
            message = f'Today {name} paying',
            timeout= 10
            )
        time.sleep(10)
    else:
        print("not found")
#check error
def remove_users(stauts):
    #global salf_users
    if stauts !='Not pay':
        del stauts
    else:
        print("Not found")
        

#Check the date is val
'''def valdate(input):
    try:
        dateobject=datetime.strptime(input,"%d/%m/%Y")
        return True
    except ValueError:
        ValueError

input="09/05/2022"
print(valdate(input))'''
