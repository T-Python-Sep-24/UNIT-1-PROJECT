from users import dataEmployee  

# requirements : 
# use venv for project 
# use color background  purple and text white  | text : Tuwaiq Airport 
# use nested loop  (while True) 
#  use main list inside has two dictinarys [{} , {} ]


#mainData = [{"employees": {}}, {"travelers": {}}]

# n = input("Enter name:")
# i = int(input("Enter id: "))
# num = int(input("enter number: "))
# em = input("Enter email:")
# po = input("Enter position: ")
# in1 =dataEmployee.Employee(n,i, num , em, po )



# print(in1.add_data())


# from users import dataEmployee, dataCustomerOrTraveler


# mainData = [{"employees": {}}, {"travelers": {}}]


# def add_employee_data():
#     n = input("Enter name: ")
#     i = int(input("Enter id: "))
#     num = int(input("Enter number: "))
#     em = input("Enter email: ")
#     po = input("Enter position: ")

#     employee = dataEmployee.Employee(n, i, num, em, po)
#     print(employee.add_data()) 

    
#     mainData[0]["employees"][i] = employee.keepData[i]
#     print("Employee data added to mainData.")


# def add_traveler_data():

#     t_name = input("Enter traveler's name: ")
#     t_id = int(input("Enter traveler's id: "))
#     t_email = input("Enter traveler's email: ")

#     traveler = dataCustomerOrTraveler.Traveler(t_name, t_id, t_email)
#     print(traveler.add_data()) 
    

#     mainData[1]["travelers"][t_id] = traveler.keepData[t_id]
#     print("Traveler data added to mainData.")


# def save_main_data():
#     with open("information.json", "w", encoding="UTF-8") as fileData:
#         json_data = json.dumps(mainData, indent=3)
#         fileData.write(json_data)
#     print("Data saved to information.json.")


# while True:
#     choice = input("Do you want to add an employee or traveler? (employee/traveler/exit): ").lower()
    
#     if choice == "employee":
#         add_employee_data()
#     elif choice == "traveler":
#         add_traveler_data()
#     elif choice == "exit":
#         save_main_data()
#         break
#     else:
#         print("Invalid choice, please try again.")
