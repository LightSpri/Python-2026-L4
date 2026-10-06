class Student:
    def __init__(self, studentID, name, dob):
        self.__id = studentID
        self.__name = name
        self.__dob = dob
        self.__marks = {}
        
    def get_studentID(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_dob(self):
        return self.__dob
    
    def get_mark(self, courseID, mark):
        self.__marks[courseID] = mark
    
    def get_marks(self):
        return self.__marks

    def set_gpa(self, gpa):
        self.__gpa = gpa

    def get_gpa(self):
        return self.__gpa