from datetime import datetime
import json

class Question:

    def __init__(self, user_id, detail, author):
        self.user_id = user_id
        self.detail = detail
        self.author = author
        self.answers = list() 
        self.date = str(datetime.now())

questions = {}
question1 = Question(1, "how to log", "arthur nangai")
no = len(questions) + 1
questions[no] = question1.__dict__

question2 = Question(2, "how to bog", "arthur bark")
no = len(questions) + 1
questions[no] = question2.__dict__

print(questions)
output = json.dumps(questions)
print(output)
##   print("author is %s date is %s" % (questions[x].author, questions[x].date))
