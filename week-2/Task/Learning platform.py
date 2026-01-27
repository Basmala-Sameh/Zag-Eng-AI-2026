class User:
    def __init__(self ,name , email ,password ):
        self.name = name
        self.email = email
        self.__password = password

    def Show_info(self):
        return {
            f"Name : {self.name}"
            f"Email : {self.email}"
        }