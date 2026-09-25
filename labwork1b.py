class Student:
    def __init__(self, studentID, name, dob):
        self.studentID = studentID
        self.name = name
        self.dob = dob

class Courses:
    def __init__(self, courseID, name):
        self.courseID = courseID
        self.name = name

def main():
    student = []
    courses = []
    marks = {}
    while True:
        print("1. Add Student")
        print("2. Add Course")
        print("3. Input Marks")
        print("4. Show Students")
        print("5. Show Courses")
        print("6. Show Marks")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            studentID = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth: ")
            student.append(Student(studentID, name, dob))
        elif choice == "2":
            courseID = input("Enter course ID: ")
            name = input("Enter course name: ")
            courses.append(Courses(courseID, name))
        elif choice == "3":
            studentID = input("Enter student ID: ")
            courseID = input("Enter course ID: ")
            mark = float(input("Enter mark: "))
            marks[(studentID, courseID)] = mark
        elif choice == "4":
            for student in student:
                print(f"Student ID: {student.studentID}, Name: {student.name}, Date of Birth: {student.dob}")
        elif choice == "5":
            for course in courses:
                print(f"Course ID: {course.courseID}, Name: {course.name}")
        elif choice == "6":
            for (studentID, courseID), mark in marks.items():
                print(f"Student ID: {studentID}, Course ID: {courseID}, Mark: {mark}")
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()