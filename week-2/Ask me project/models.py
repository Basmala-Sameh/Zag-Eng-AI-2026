import secrets
import random

class User():

    def __init__(self , name , password, email , allow_anonymous ):
        self.name = name

        display_id = random.randint(100 , 1000)
        system_id = secrets.token_urlsafe(8)

        self.system_id = system_id
        self.display_id = display_id

        self.__password = password
        self.email = email
        self.allow_anonymous = allow_anonymous

