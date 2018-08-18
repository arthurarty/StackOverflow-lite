from datetime import datetime

class Question:

    def __init__(self, user_id, detail, author):
        self.user_id = user_id
        self.detail = detail
        self.author = author
        self.answers = list() 
        self.date = str(datetime.now())
