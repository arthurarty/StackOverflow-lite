from datetime import datetime

class Answer: 

    def __init__(self, question_id, body, author):
        self.question_id = question_id
        self.body = body
        self.author = author
        self.date = str(datetime.now())