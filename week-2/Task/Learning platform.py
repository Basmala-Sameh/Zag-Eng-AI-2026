class User:
    def __init__(self ,name , email ,password ):
        self.name = name
        self.email = email
        self.__password = password

    def Show_info(self):
        return {
            "Name" : self.name , 
            "Email" : self.email
        }

    def check_password(self , old_p ):
        if self.__password == old_p :
            return True

    def set_password(self , old_p ,new_p ):
        if self.check_password(old_p) == True :
            self.__password = new_p

    def get_password(self):
        return self.__password



class Student(User):
    def __init__(self ,name , email ,password , level , specialization ):
        super().__init__(self ,name , email ,password)
        self.level = level
        self.specialization = specialization

    def Show_info(self):
        super().Show_info()
        return{
            "Level ": self.level ,
            "Specialization ": self.specialization ,
        }


