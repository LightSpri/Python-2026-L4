import math
import numpy
# def floor (a):
#     print(math.floor(a))
# def GPA (marks, credits):

#     total_credits = sum(credits)
#     weighted_sum = sum(m * c for m, c in zip(marks, credits))
#     gpa = weighted_sum / total_credits
#     GPA = 
# def sortStudentByGPA (students):
#     sorted_students = sorted(students, key=lambda x: x['GPA'], reverse=True)
#     for student in sorted_students:
#         print(f"Student ID: {student['studentID']}, Name: {student['name']}, GPA: {student['GPA']:.2f}")
class student:
    def __init_(self, name, id):
        self,name = name
        self.id = id
class course:
    def __init__(sel, name,credits):
        self,name = name
        self.credits = credits
def info():
    students = []
    courses = []
    marks = {}
    while True:
        print("1. Add student")
        print("2. Add course")
        print("3. Input marks")
        choice = input("Enter your choice: ")
        if(choice == 1):
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            students.append(student(name, student_id))
        if(choice == 2):
            name = input("Enter course name: ")
            credits = int(input("Enter course credits: "))
            courses.append(course(name, credits))
            