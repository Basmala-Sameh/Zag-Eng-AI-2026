from models import User
from models import Question
from models import Thread
from models import Anonymous


class UserServices():
    counter = 0

    def __init__(self):
        self.users_dict = {}

    def add_user(self ,name , password, email , allow_anonymous):
        u = User(name , password, email , allow_anonymous)
        each_user_info = [name , password, email , allow_anonymous]
        self.users_dict[u.getId()] = each_user_info
        UserServices.counter +=1

        pass




