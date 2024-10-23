from academy import Academy
from colorama import init, Fore, Style
from admin import Admin
# Initialize Colorama
init(autoreset=True)
print(Style.BRIGHT + Fore.BLUE + r"""
                     _ 
                  _ |_|_
                 |_|  |_|_
                |_|     |_|  
              Tuwaiq Academy
    """)

def get_int_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input == '0':
            return 'back'
        try:
            return int(user_input)
        except ValueError:
            print(Fore.YELLOW + ' ' * 10 + "Please enter a valid number or '0' to go back.")

def main():
    admin = Admin(name="admin", password="1234")  
    
    # Admin login
    while True:
        print(Fore.GREEN + "Admin Login")
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        
        if username == admin.get_name() and admin.verify_password(password):
            print(Fore.GREEN + "Login successful!")
            break
        else:
            print(Fore.RED + "Invalid credentials! Please try again.")
            

    academy = Academy()
    
    while True:
        print(Fore.BLUE + "\n*** Academy Management System ***")
        print(Fore.BLUE + "1. Add Section")
        print(Fore.BLUE + "2. List Section")
        print(Fore.BLUE + "3. Delete Section")
        print(Fore.BLUE + "4. Register Section")
        print(Fore.BLUE + "5. Remove Person from Course")
        print(Fore.RED + "6. Exit")
        print(Fore.BLUE + '\n' + '*' * 30)
        choice = input(Fore.BLUE + "Enter your choice (1-6): ")
        print(Fore.BLUE + '\n' + '*' * 30)

        #>>>>>>>>>>>>>>>>> ADD <<<<<<<<<<<<<<<<<<<<
        if choice == '1':
            while True:
                print(Fore.GREEN + "\n*** Add Menu (Enter 0 to go back) ***")
                print(Fore.GREEN + "1. Add Teacher")
                print(Fore.GREEN + "2. Add Student")
                print(Fore.GREEN + "3. Add Course")
                print(Fore.GREEN + '\n' + '*' * 30)
                sub_choice = input(Fore.GREEN + "Enter your choice (0 or 1-3): ")
                print(Fore.GREEN + '\n' + '*' * 30)
                
                if sub_choice == '0':
                    break
                elif sub_choice == '1':
                    name = input(Fore.GREEN + "Enter teacher name: ")
                    specialization = input(Fore.GREEN + "Enter teacher specialization: ")
                    print(Fore.GREEN + '\n' + '*' * 30)
                    academy.add_teacher(name, specialization)

                elif sub_choice == '2':
                    name = input(Fore.GREEN + "Enter student name: ")
                    print(Fore.GREEN + '\n' + '*' * 30)
                    academy.add_student(name)

                elif sub_choice == '3':
                    course_name = input(Fore.GREEN + "Enter course name: ")
                    print(Fore.GREEN + '\n' + '*' * 30)
                    academy.add_course(course_name)

                else:
                    print(Fore.RED + ' ' * 10 +  "Invalid choice! Please select a valid option.")

        #>>>>>>>>>>>>>>>>>>>> LIST <<<<<<<<<<<<<<<<
        elif choice == '2':
            while True:
                print(Fore.BLUE + "\n*** List Menu (Enter 0 to go back) ***")
                print(Fore.BLUE + "1. List Teachers")
                print(Fore.BLUE + "2. List Students")
                print(Fore.BLUE + "3. List Courses")
                print(Fore.BLUE + "4. List Courses with Students and Teachers")
                print(Fore.BLUE + '\n' + '*' * 30)
                sub_choice = input(Fore.BLUE + "Enter your choice (0 or 1-4): ")
                print(Fore.BLUE + '\n' + '*' * 30)

                if sub_choice == '0':
                    break
                elif sub_choice == '1':
                    academy.list_teachers()

                elif sub_choice == '2':
                    academy.list_students()

                elif sub_choice == '3':
                    academy.list_courses()

                elif sub_choice == '4':
                    academy.list_courses_with_students_and_teacher()

                else:
                    print(Fore.RED + ' ' * 10 + "Invalid choice! Please select a valid option.")

        #>>>>>>>>>>>>>>>>>>> DELETE <<<<<<<<<<<<<<<<<
        elif choice == '3':
            while True:
                print(Fore.RED + "\n*** Delete Menu (Enter 0 to go back) ***")
                print(Fore.RED + "1. Delete Teacher")
                print(Fore.RED + "2. Delete Student")
                print(Fore.RED + "3. Delete Course")
                print(Fore.RED + '\n' + '*' * 30)
                sub_choice = input(Fore.RED + "Enter your choice (0 or 1-3): ")
                print(Fore.RED + '\n' + '*' * 30)

                if sub_choice == '0':
                    break
                elif sub_choice == '1':
                    teacher_id = get_int_input( Fore.RED + "Enter teacher ID to delete: ")
                    print(Fore.RED + '\n' + '*' * 30)
                    if teacher_id == 'back': break
                    academy.delete_teacher(teacher_id)

                elif sub_choice == '2':
                    student_id = get_int_input(Fore.RED + "Enter student ID to delete: ")
                    print(Fore.RED + '\n' + '*' * 30)
                    if student_id == 'back': break
                    academy.delete_student(student_id)

                elif sub_choice == '3':
                    course_id = get_int_input(Fore.RED + "Enter course ID to delete: ")
                    print(Fore.RED + '\n' + '*' * 30)
                    if course_id == 'back': break
                    academy.delete_course(course_id)

                else:
                    print(Fore.RED + ' ' * 10 + "Invalid choice! Please select a valid option.")

        #>>>>>>>>>>>>>>>>>>>>>>> REGISTER <<<<<<<<<<<<<<<<<<<<<<<<<<<
        elif choice == '4':
            while True:
                print(Fore.BLUE + "\n*** Register Menu (Enter 0 to go back) ***")
                print(Fore.BLUE + "1. Register Student in Course")
                print(Fore.BLUE + "2. Assign Teacher to Course")
                print(Fore.BLUE + '\n' + '*' * 30)
                sub_choice = input(Fore.BLUE + "Enter your choice (0 or 1-2): ")
                print(Fore.BLUE + '\n' + '*' * 30)

                if sub_choice == '0':
                    break
                elif sub_choice == '1':
                    student_id = get_int_input(Fore.BLUE + "Enter student ID to register: ")
                    if student_id == 'back': break
                    course_id = get_int_input(Fore.BLUE + "Enter course ID to register the student in: ")
                    print(Fore.BLUE + '\n' + '*' * 30)
                    if course_id == 'back': break
                    academy.register_student_in_course(student_id, course_id)

                elif sub_choice == '2':
                    teacher_id = get_int_input(Fore.BLUE + "Enter teacher ID to assign: ")
                    if teacher_id == 'back': break
                    course_id = get_int_input(Fore.BLUE + "Enter course ID to assign the teacher to: ")
                    print(Fore.BLUE + '\n' + '*' * 30)
                    if course_id == 'back': break
                    academy.assign_teacher_to_course(teacher_id, course_id)

                else:
                    print(Fore.RED + ' ' * 10 + "Invalid choice! Please select a valid option.")



        #>>>>>>>>>>>>>>>>>>>>>>> REMOVE PERSON FROM COURSE <<<<<<<<<<<<<<<<<<<<<<<<<<<
        elif choice == '5':
            while True:
                print(Fore.BLUE + "\n*** Remove Person from Course Menu (Enter 0 to go back) ***")
                print(Fore.BLUE + "1. Remove Student from Course")
                print(Fore.BLUE + "2. Remove Teacher from Course")
                print(Fore.BLUE + '\n' + '*' * 30)
                sub_choice = input(Fore.BLUE + "Enter your choice (0 or 1-2): ")
                print(Fore.BLUE + '\n' + '*' * 30)

                if sub_choice == '0':
                    break
                elif sub_choice == '1':
                    student_id = get_int_input(Fore.BLUE + "Enter student ID to remove: ")
                    if student_id == 'back': break
                    course_id = get_int_input(Fore.BLUE + "Enter course ID to remove the student from: ")
                    if course_id == 'back': break
                    academy.remove_person_from_course(student_id, course_id, "student")

                elif sub_choice == '2':
                    teacher_id = get_int_input(Fore.BLUE + "Enter teacher ID to remove: ")
                    if teacher_id == 'back': break
                    course_id = get_int_input(Fore.BLUE + "Enter course ID to remove the teacher from: ")
                    if course_id == 'back': break
                    academy.remove_person_from_course(teacher_id, course_id, "teacher")

                else:
                    print(Fore.RED + ' ' * 10 + "Invalid choice! Please select a valid option.")

        #>>>>>>>>>>>>>>>>>>>>>>> EXIT <<<<<<<<<<<<<<<<<<<<<<<<<<<
        elif choice == '6':
            print(Fore.YELLOW +  ' ' * 5 + "Exiting the system :)")
            break

        else:
            print(Fore.RED + ' ' *10 + "Invalid choice! Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()
