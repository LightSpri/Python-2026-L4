import numpy as np

def calculate_gpa(student, courses):
    marks = student.get_marks()
    if not marks:
        return 0.0
    score_list = []
    credit_list = []
    for course in courses:
        cid = course.get_id()
        if cid in marks:
            score_list.append(marks[cid])
            credit_list.append(course.get_credits())
    if not credit_list:
        return 0.0

    scores = np.array(score_list, dtype=float)
    credits = np.array(credit_list, dtype=float)

    total_credits = np.sum(credits)
    if total_credits == 0:
        return 0.0
    gpa = np.sum(scores * credits) / total_credits
    gpa = np.floor(gpa * 10) / 10
    return gpa 
    
def sort_students_by_gpa(students, courses):
    for s in students:
        s.set_gpa(calculate_gpa(s, courses))

    sorted_students = sorted(students, key=lambda x: x.get_gpa(), reverse=True)
    return sorted_students
def display_sorted_students(students, courses):
    sorted_list = sort_students_by_gpa(students, courses)
    print("=== Students Sorted by GPA ===")
    for s in sorted_list:
        print(f"Student ID: {s.get_studentID()} Name: {s.get_name()} GPA: {s.get_gpa()}")
    
