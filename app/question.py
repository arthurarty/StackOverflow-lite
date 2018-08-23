"""The module contains the Question class"""
from datetime import datetime

class Question:

    def __init__(self, user_id, detail, author):
        self.user_id = user_id
        self.detail = detail
        self.author = author
        self.answers = list() 
        self.date = str(datetime.now())

    """return_answers returns answers to a question"""
    def return_answers(self):
        return self.answers

    """returns user id"""
    def return_user_id(self):
        return self.author


