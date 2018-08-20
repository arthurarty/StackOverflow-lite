from datetime import datetime

class Question:

    def __init__(self, user_id, detail, author):
        self.user_id = user_id
        self.detail = detail
        self.author = author
        self.answers = list() 
        self.date = str(datetime.now())

#dictionary to store all questions
questions = {}

#method to add question to dictonary
def add_question(Question):
    no_of_question = len(questions) + 1
    questions[no_of_question] = Question.__dict__
    return questions[no_of_question]

#method to return all questions
def return_questions():
    return questions

#method to return a single question.
def return_single_question(id):
    if id in questions:
        return questions[id]
    return 0

#add answer
def add_answer(id, answer):
    question = questions[id]
    question['answers'].append(answer)
    return questions[id]