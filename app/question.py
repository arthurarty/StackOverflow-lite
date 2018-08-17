from datetime import datetime

class Question:

    def __init__(self, id, detail, author):
        self.id = id
        self.detail = detail
        self.author = author
        self.answers = list() 
        self.date = datetime.now()

questions = {}
question1 = Question(1, "how to log", "arthur nangai")
no = len(questions) + 1
questions[no] = question1

question2 = Question(2, "how to bog", "arthur bark")
no = len(questions) + 1
questions[no] = question2

for x in questions:
    print("author is %s date is %s" % (questions[x].author, questions[x].date))
