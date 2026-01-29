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
        super().__init__(name , email ,password)
        self.level = level
        self.specialization = specialization

    def Show_info(self):
        info = super().Show_info()
        info["Level"] = self.level
        info["Specialization"] = self.specialization
        return info

class Instructor(User):
    def __init__(self, name, email, password ,specialization ):
        super().__init__(name, email, password)
        self.specialization = specialization

    def Show_info(self):
        info = super().Show_info()
        info["Specialization"] = self.specialization
        return info
    

s1 = Student("Basmala" , "basmala@gmail.com" , "456" , 3 , "AI")
s2 = Student("Mostafa" , "mostafa@gmail.com" , "666" , 1 , "IT")

I1 = Instructor("D.Hefny" , "Hefny@gmail" , "999" , "CS")

print(I1.Show_info())
print(s1.Show_info())

print(f"{s2.name} password is {s2.get_password()}")
s2.set_password("666" ,"111")
print(f"{s2.name} updated password is {s2.get_password()}")