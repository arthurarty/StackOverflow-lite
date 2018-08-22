"""The module contains the Question class and the logic to add questions to a dictionary for 
storage"""
from datetime import datetime
from app.answer import Answer

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

