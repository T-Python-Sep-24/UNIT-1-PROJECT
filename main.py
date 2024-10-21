from academy import Academy
from colorama import init, Fore, Style

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
            print("Please enter a valid number or '0' to go back.")

def main():
    academy = Academy()
    
    while True:
        print(Fore.CYAN + "\n=== Academy Management System ===")
        print(Fore.CYAN + "1. Add Section")
        print(Fore.CYAN + "2. Delete Section")
        print(Fore.CYAN + "3. List Section")
        print(Fore.CYAN + "4. Register Section")  
        print(Fore.RED + "5. Exit")
        print(Fore.BLUE + "\n=================================\n")
        choice = input(Fore.BLUE + "Enter your choice (1-5): ")
        print(Fore.BLUE + "\n=================================\n")

        #----------------ADD----------------------
        if choice == '1':
            while True:
                print("\n--- Add Menu (Enter 0 to go back) ---")
                print("1. Add Teacher")
                print("2. Add Student")
                print("3. Add Course")
                print(Fore.BLUE + "\n=================================\n")
                sub_choice = input("Enter your choice (1-3): ")
                print(Fore.BLUE + "\n=================================\n")
                if sub_choice == '0':
                    break
                elif sub_choice == '1':
                    name = input("Enter teacher name: ")
                    specialization = input("Enter teacher specialization: ")
                    academy.add_teacher(name, specialization)

                elif sub_choice == '2':
                    name = input("Enter student name: ")
                    academy.add_student(name)

                elif sub_choice == '3':
                    course_name = input("Enter course name: ")
                    academy.add_course(course_name)

                else:
                    print("Invalid choice! Please select a valid option.")

        #>>>>>>>>>>>>>>>>>>> DELETE <<<<<<<<<<<<<<<<<
        elif choice == '2':
            while True:
                print(Fore.RED + "\n--- Delete Menu (Enter 0 to go back) ---")
                print(Fore.RED + "1. Delete Teacher")
                print(Fore.RED + "2. Delete Student")
                print(Fore.RED +"3. Delete Course")
                sub_choice = input("Enter your choice (1-3): ")

                if sub_choice == '0':
                    break
                elif sub_choice == '1':
                    teacher_id = get_int_input("Enter teacher ID to delete: ")
                    if teacher_id == 'back': break
                    academy.delete_teacher(teacher_id)

                elif sub_choice == '2':
                    student_id = get_int_input("Enter student ID to delete: ")
                    if student_id == 'back': break
                    academy.delete_student(student_id)

                elif sub_choice == '3':
                    course_id = get_int_input("Enter course ID to delete: ")
                    if course_id == 'back': break
                    academy.delete_course(course_id)

                else:
                    print("Invalid choice! Please select a valid option.")

        #====================LIST====================
        elif choice == '3':
            while True:
                print("\n--- List Menu (Enter 0 to go back) ---")
                print("1. List Teachers")
                print("2. List Students")
                print("3. List Courses")
                print("4. List Courses with Students and Teachers")
                sub_choice = input("Enter your choice (1-4): ")

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
                    print("Invalid choice! Please select a valid option.")

        #>>>>>>>>>>>>>>>>>>>>>>> REGISTER <<<<<<<<<<<<<<<<<<<<<<<<<<<
        elif choice == '4':
            while True:
                print("\n--- Register Menu (Enter 0 to go back) ---")
                print("1. Register Student in Course")
                print("2. Assign Teacher to Course")
                sub_choice = input("Enter your choice (1-2): ")

                if sub_choice == '0':
                    break
                elif sub_choice == '1':
                    student_id = get_int_input("Enter student ID to register: ")
                    if student_id == 'back': break
                    course_id = get_int_input("Enter course ID to register the student in: ")
                    if course_id == 'back': break
                    academy.register_student_in_course(student_id, course_id)

                elif sub_choice == '2':
                    teacher_id = get_int_input("Enter teacher ID to assign: ")
                    if teacher_id == 'back': break
                    course_id = get_int_input("Enter course ID to assign the teacher to: ")
                    if course_id == 'back': break
                    academy.assign_teacher_to_course(teacher_id, course_id)

                else:
                    print("Invalid choice! Please select a valid option.")

        #>>>>>>>>>>>>>>>>>>>>>>> EXIT <<<<<<<<<<<<<<<<<<<<<<<<<<<
        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice! Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
