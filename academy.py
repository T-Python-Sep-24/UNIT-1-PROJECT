from teacher import Teacher
from student import Student
from course import Course
from data_handler import load_data_from_json, save_data_to_json

class Academy:
    def __init__(self):
        self.data = load_data_from_json('academy_data.json')

        if 'teachers' not in self.data:
            self.data['teachers'] = []
        if 'students' not in self.data:
            self.data['students'] = []
        if 'courses' not in self.data:
            self.data['courses'] = []

    def add_teacher(self, name: str, specialization: str):
        ''' Adds a new teacher to the academy. '''

        teacher_id = len(self.data['teachers']) + 1
        new_teacher = Teacher(teacher_id, name, specialization)
        self.data['teachers'].append(new_teacher.__dict__)
        self.save()
        print(f"Teacher '{name}' added with specialization '{specialization}' and ID '{teacher_id}'")

    def add_student(self, name: str):
        ''' Adds a new student to the academy. '''

        student_id = len(self.data['students']) + 1
        new_student = Student(student_id, name)
        self.data['students'].append(new_student.__dict__)
        self.save()
        print(f"Student '{name}' added with ID '{student_id}'")

    def add_course(self, name: str):
        ''' Adds a new course to the academy. '''
        course_id = len(self.data['courses']) + 1
        new_course = Course(course_id, name)
        self.data['courses'].append(new_course.__dict__)
        self.save()
        print(f"Course '{name}' added with ID '{course_id}'")

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
            print(f"Teacher with ID {teacher_id} has been assigned to course ID {course_id}.")
        else:
            print("Teacher or Course not found!")

    def delete_teacher(self, teacher_id: int):
        '''  Deletes a teacher from the academy. '''
        teacher = next((t for t in self.data['teachers'] if t['teacher_id'] == teacher_id), None)
        if teacher:
            self.data['teachers'].remove(teacher)
            self.save()
            print(f"Teacher with ID {teacher_id} has been deleted.")
        else:
            print("Teacher not found!")

    def delete_student(self, student_id: int):
        '''  Deletes a student from the academy. '''

        student = next((s for s in self.data['students'] if s['student_id'] == student_id), None)
        if student:
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
            print(f"ID: {course['course_id']}, Name: {course['name']}, Students: {course.get('students', [])}, Teachers: {course.get('teachers', [])}")
