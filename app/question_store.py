from app.question import Question
from app.answer import Answer

#dictionary to store all questions
questions = {}

"""method add a new question to the dictionary"""
def add_question(new_question):
    if isinstance(new_question, Question):
        no_of_question = len(questions) + 1
        questions[no_of_question] = new_question.__dict__
        return questions[no_of_question]
    raise TypeError('Not an instance of Question')

def return_questions():
    return questions

#method to return a single question.
def return_single_question(question_id):
    if question_id in questions:
        return questions[question_id]
    return 0

#add answer
def add_answer(new_answer):
    if not isinstance(new_answer, Answer):
        raise TypeError('Not an instance of Answer')

    if new_answer.question_id in questions:
        question = questions[new_answer.question_id]
        question['answers'].append(new_answer.__dict__)
        return questions[new_answer.question_id]

    return 0