from __init__ import person

class teachers(person):
    def __init__(self,id,name,speciality):
        super().__init__(id ,name)
        self.speciality = speciality
        pass