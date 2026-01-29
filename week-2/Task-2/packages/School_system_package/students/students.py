from __init__ import person

class students(person):
    def __init__(self,id ,name , course = None):
        super().__init__(id ,name)
        self.course = course
        pass

    def enroll(self,course):
        self.course = course