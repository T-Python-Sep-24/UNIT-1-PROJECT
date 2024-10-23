import random
import re
from teacher import Teacher
from student import Student
from course import Course
from data_handler import load_data_from_json, save_data_to_json
from colorama import Fore

class Academy:
    def __init__(self):
        self.data = load_data_from_json('academy_data.json')

        if 'teachers' not in self.data:
            self.data['teachers'] = []
        if 'students' not in self.data:
            self.data['students'] = []
        if 'courses' not in self.data:
            self.data['courses'] = []

    def generate_unique_id(self):
        '''Generates a unique 4-digit ID that is not already used.'''
        existing_ids = {t['teacher_id'] for t in self.data['teachers']}
        existing_ids.update(s['student_id'] for s in self.data['students'])
        existing_ids.update(c['course_id'] for c in self.data['courses'])

        new_id = random.randint(1000, 9999)
        while new_id in existing_ids:
            new_id = random.randint(1000, 9999)
        return new_id

    def validate_name(self, name: str) -> bool:
         '''Validates that the name contains only letters (no numbers or symbols).'''
         return bool(re.match("^[A-Za-z\s]+$", name))

    def add_teacher(self, name: str, specialization: str):
        ''' Adds a new teacher to the academy. '''
        if not self.validate_name(name):
            print("Invalid name! Please enter a name with letters only.")
            return

        teacher_id = self.generate_unique_id()
        new_teacher = Teacher(teacher_id, name, specialization)
        self.data['teachers'].append(new_teacher.__dict__)
        self.save()
        print(f"Teacher '{name}' added with specialization '{specialization}' and ID '{teacher_id}'")

    def add_course(self, name: str):
        ''' Adds a new course to the academy. '''
        course_id = self.generate_unique_id()
        new_course = Course(course_id, name)
        self.data['courses'].append(new_course.__dict__)
        self.save()
        print(f"Course '{name}' added with ID '{course_id}'")

    def add_student(self, name: str):
        ''' Adds a new student to the academy. '''
        if not self.validate_name(name):
            print("Invalid name! Please enter a name with letters only.")
            return

        student_id = self.generate_unique_id()
        new_student = Student(student_id, name)
        self.data['students'].append(new_student.__dict__)
        self.save()
        print(f"Student '{name}' added with ID '{student_id}'")


    def register_student_in_course(self, student_id: int, course_id: int):
        '''  Registers a student in a specific course. '''

        student = next((s for s in self.data['students'] if s['student_id'] == student_id), None)
        course = next((c for c in self.data['courses'] if c['course_id'] == course_id), None)

        if student and course:
            if 'students' not in course:
                course['students'] = []
            course['students'].append(student_id)
            self.save()
            print(f"Student with ID {student_id} has been registered in course ID {course_id}.")
        else:
            print("Student or Course not found!")

    def assign_teacher_to_course(self, teacher_id: int, course_id: int):
        ''' Assigns a teacher to a specific course. '''
        teacher = next((t for t in self.data['teachers'] if t['teacher_id'] == teacher_id), None)
        course = next((c for c in self.data['courses'] if c['course_id'] == course_id), None)

        if teacher and course:
            if 'teachers' not in course:
                course['teachers'] = []
            course['teachers'].append(teacher_id)
            self.save()
            print(Fore.GREEN + f"Teacher {teacher['name']} with ID {teacher_id} has been assigned to course {course['name']} ID {course_id}.")
        else:
            print(Fore.RED + "Teacher or Course not found!")


    def list_courses_with_students_and_teacher(self):
        '''Lists all courses along with their assigned students and teachers.'''
        try:
            if not self.data['courses']:
                print("No courses available.")
                return

            for course in self.data['courses']:
                print(f"\nCourse ID: {course['course_id']}, Name: {course['name']}")
                
                # display teachers names
                if 'teachers' in course and course['teachers']:
                    teacher_names = [t['name'] for t in self.data['teachers'] if t['teacher_id'] in course['teachers']]
                    print(f"Teacher(s): {', '.join(teacher_names)}")
                else:
                    print("No teachers assigned to this course.")
                
                # display students nams
                if 'students' in course and course['students']:
                    student_names = [s['name'] for s in self.data['students'] if s['student_id'] in course['students']]
                    print(f"Student(s): {', '.join(student_names)}")
                else:
                    print("No students registered in this course.")
                    
        except Exception as e:
            print(f"Error listing courses with students and teacher: {e}")


    def delete_teacher(self, teacher_id: int):
        '''Deletes a teacher from the academy and removes them from all courses.'''
        
        teacher = next((t for t in self.data['teachers'] if t['teacher_id'] == teacher_id), None)
        if teacher:
            ## Remove teacher from all courses
            for course in self.data['courses']:
                if 'teachers' in course and teacher_id in course['teachers']:
                    course['teachers'].remove(teacher_id)
            
            self.data['teachers'].remove(teacher)
            self.save()
            print(f"Teacher with ID {teacher_id} has been deleted.")
        else:
            print("Teacher not found!")

    def delete_student(self, student_id: int):
        '''Deletes a student from the academy and removes them from all courses.'''
        
        student = next((s for s in self.data['students'] if s['student_id'] == student_id), None)
        if student:
            ### Remove student from all courses
            for course in self.data['courses']:
                if 'students' in course and student_id in course['students']:
                    course['students'].remove(student_id)
            
            self.data['students'].remove(student)
            self.save()
            print(f"Student with ID {student_id} has been deleted.")
        else:
            print("Student not found!")


    def delete_course(self, course_id: int):
        '''  Deletes a course from the academy. '''

        course = next((c for c in self.data['courses'] if c['course_id'] == course_id), None)
        if course:
            self.data['courses'].remove(course)
            self.save()
            print(f"Course with ID {course_id} has been deleted.")
        else:
            print("Course not found!")

    def get_statistics(self):
        '''Prints the total number of teachers, students, and courses.'''
        
        total_teachers = len(self.data['teachers'])
        total_students = len(self.data['students'])
        total_courses = len(self.data['courses'])
        
        print(f"Total Teachers: {total_teachers}")
        print(f"Total Students: {total_students}")
        print(f"Total Courses: {total_courses}")

    def remove_person_from_course(self, person_id: int, course_id: int, person_type: str):
        '''Removes a student or teacher from a specific course.'''
        
        course = next((c for c in self.data['courses'] if c['course_id'] == course_id), None)

        if not course:
            print("Course not found!")
            return
        
        # If the person to be deleted is a student
        if person_type.lower() == 'student':
            student = next((s for s in self.data['students'] if s['student_id'] == person_id), None)
            if not student:
                print(Fore.RED + "Student not found!")
                return
            #> If the student is registered in the course, delete him.
            if 'students' in course and person_id in course['students']:
                course['students'].remove(person_id)
                self.save()
                print(Fore.GREEN + f"Student with ID {person_id} has been removed from course ID {course_id}.")
            else:
                print(Fore.RED + f"Student with ID {person_id} is not registered in course ID {course_id}.")
        ## If the person to be deleted is a teacher
        elif person_type.lower() == 'teacher':
            teacher = next((t for t in self.data['teachers'] if t['teacher_id'] == person_id), None)
            if not teacher:
                print(Fore.RED + "Teacher not found!")
                return
            ##> If the teacher is registered in the course, delete him.
            if 'teachers' in course and person_id in course['teachers']:
                course['teachers'].remove(person_id)
                self.save()
                print(Fore.GREEN + f"Teacher with ID {person_id} has been removed from course ID {course_id}.")
            else:
                print(Fore.RED + f"Teacher with ID {person_id} is not registered in course ID {course_id}.")

        else:
            print(Fore.RED + "Invalid person type! Use 'student' or 'teacher'.")


    def save(self):
        '''Saves the current data to the JSON file.'''
        save_data_to_json('academy_data.json', self.data)

    def list_teachers(self):
        for teacher in self.data['teachers']:
            print(f"ID: {teacher['teacher_id']}, Name: {teacher['name']}, Specialization: {teacher['specialization']}")

    def list_students(self):
        ''' Lists all students in the academy.'''

        for student in self.data['students']:
            print(f"ID: {student['student_id']}, Name: {student['name']}")

    def list_courses(self):
        '''Lists all courses in the academy.'''

        for course in self.data['courses']:
            print(f"ID: {course['course_id']}, Name: {course['name']}")
