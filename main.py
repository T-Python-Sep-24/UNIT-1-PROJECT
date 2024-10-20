from academy import Academy

def main():
    academy = Academy()  # تحميل البيانات عند بداية البرنامج
    
    while True:
        print("\n--- Academy Management System ---")
        print("1. Add Teacher")
        print("2. Add Student")
        print("3. Add Course")
        print("4. Delete Teacher")
        print("5. Delete Student")
        print("6. Delete Course")
        print("7. Register Student in Course")
        print("8. Assign Teacher to Course")
        print("9. List Teachers")
        print("10. List Students")
        print("11. List Courses")
        print("12. Exit")
        
        choice = input("Enter your choice (1-12): ")

        if choice == '1':
            name = input("Enter teacher name: ")
            specialization = input("Enter teacher specialization: ")
            academy.add_teacher(name, specialization)

        elif choice == '2':
            name = input("Enter student name: ")
            academy.add_student(name)

        elif choice == '3':
            course_name = input("Enter course name: ")
            academy.add_course(course_name)

        elif choice == '4':
            teacher_id = int(input("Enter teacher ID to delete: "))
            academy.delete_teacher(teacher_id)

        elif choice == '5':
            student_id = int(input("Enter student ID to delete: "))
            academy.delete_student(student_id)

        elif choice == '6':
            course_id = int(input("Enter course ID to delete: "))
            academy.delete_course(course_id)

        elif choice == '7':
            student_id = int(input("Enter student ID to register: "))
            course_id = int(input("Enter course ID to register the student in: "))
            academy.register_student_in_course(student_id, course_id)

        elif choice == '8':
            teacher_id = int(input("Enter teacher ID to assign: "))
            course_id = int(input("Enter course ID to assign the teacher to: "))
            academy.assign_teacher_to_course(teacher_id, course_id)

        elif choice == '9':
            academy.list_teachers()

        elif choice == '10':
            academy.list_students()

        elif choice == '11':
            academy.list_courses()

        elif choice == '12':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
