from datetime import datetime

"""Class Answer represents an answer to a question
"""
class Answer: 

    def __init__(self, question_id, body, author):
        self.question_id = question_id
        self.body = body
        self.author = author
        self.date = str(datetime.now())

    def return_question_id(self):
        return self.question_id

    def return_answer_author(self):
        return self.author

    def return_answer_date(self):
        return self.date

    def return_answer_body(self):
        return self.body