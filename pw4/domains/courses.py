class Courses:
    def __init__(self, courseID, name, credits):
        self.__id = courseID
        self.__name = name
        self.__credits = credits
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_credits(self):
        return self.__credits