import math

from numpy import append
from domains.student import Student
from domains.courses import Courses

def input_students():
    n = int(input("Enter number of students: "))
    students = []
    for i in range(n):
        name = input("Enter student name: ")
        sid = input("Enter student ID: ")
        dob = input("Enter student date of birth: ")
        students.append(Student(sid, name, dob))
    return students

def input_courses():
    n = int(input("Enter number of courses: "))
    courses = []
    for i in range(n):
        name = input("Enter course name: ")
        cid = input("Enter course ID: ")
        credits = int(input("Enter course credits: "))
        courses.append(Courses(cid, name, credits))
    return courses

def input_marks(students, courses):
    marks = {}
    for course in courses:
        print(f"Input marks for course {course.get_name()} (ID: {course.get_id()})")
        for student in students:
            raw_mark = input(f"Enter mark for student {student.get_name()} (ID: {student.get_studentID()}): ")
            mark = float(math.floor(float(raw_mark * 10) / 10))
            student.get_mark(course.get_id(), mark)
