from flask import Flask, jsonify, json
from app.question import Question
app = Flask(__name__)

questions = {}

question1 = Question(1, "how to log", "arthur nangai")
no = len(questions) + 1
questions[no] = question1

question2 = Question(2, "how to bog", "arthur bark")
no = len(questions) + 1
questions[no] = question2

@app.route('/')
def hello_world():
    question = Question(8, "Hello there", "arthur")
    return str(question.id)
    #return 'Hello, World!'

@app.route('/v1/questions')
def fetch_all_questions():
    text = ""
    for x in questions:
        text = text + ("author is %s date is %s \n" % (questions[x].author, questions[x].date)) 
    
    return text
    #return 'Hello, World!'

@app.route('/v1/questions/<int:question_id>/')
def fetch_single_question(question_id):
    text = ""
    text = text + ("author is %s date is %s \n" % (questions[question_id].author, questions[question_id].date)) 
    return text

if __name__ == "__main__":
    app.run()

