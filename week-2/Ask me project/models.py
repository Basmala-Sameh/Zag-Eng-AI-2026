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

class Question():
    counter = 1
    def __init__(self  , from_user_id , to_user_id , Q_value):

        self.parent_id = Question.counter
        Question.counter +=1

        self.from_user_id = from_user_id
        self.to_user_id = to_user_id

        self.answered = False
        self.Q_value = Q_value

class Anonymous(Question):
    def __init__(self, from_user_id , to_user_id , Q_value):
        super().__init__(from_user_id, to_user_id , Q_value)
        self.from_user_id = "AQ"

class Thread(Question):
    def __init__(self, from_user_id, to_user_id, Q_value):
        super().__init__(from_user_id, to_user_id, Q_value)
        self.Q_id = Question.counter
