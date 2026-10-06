from input import input_students, input_courses, input_marks
from output import display_sorted_students

def main():
    print("=== Student Management System ===")
    students = input_students()
    courses = input_courses()

    input_marks(students, courses)

    display_sorted_students(students, courses)

if __name__ == "__main__":
    main()