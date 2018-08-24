"""The module contains the Stack class and the logic to add questions"""
from app.answer import Answer
from app.question import Question

class Stack:
    def __init__(self, name):
        self.name = name
        self.questions = {}

    def return_name(self):
        return self.name
    
    def return_questions(self):
        return self.questions   

    def add_question(self, new_question):
        if isinstance(new_question, Question):
            no_of_question = len(self.questions) + 1
            self.questions[no_of_question] = new_question.__dict__
            return self.questions[no_of_question]
        raise TypeError('Not an instance of Question')

    #method to return a single question.
    def return_single_question(self, question_id):
        if question_id in self.questions:
            return self.questions[question_id]
        return 0

    #add answer
    def add_answer(self, new_answer):
        if not isinstance(new_answer, Answer):
            raise TypeError('Not an instance of Answer')

        if new_answer.question_id in self.questions:
            question = self.questions[new_answer.question_id]
            question['answers'].append(new_answer.__dict__)
            return self.questions[new_answer.question_id]

        return 0


