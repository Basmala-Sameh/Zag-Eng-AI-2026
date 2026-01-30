import secrets

class User():
    def __init__(self , name , password, email , allow_anonymous ):
        self.name = name
        id = secrets.token_urlsafe(8)
        self.id = id
        self.__password = password
        self.email = email
        self.allow_anonymous = allow_anonymous