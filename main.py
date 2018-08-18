from flask import Flask, request, jsonify
from app.question import Question
app = Flask(__name__)

questions = {}

question1 = Question(1, "how to log", "arthur nangai")
no = len(questions) + 1
questions[no] = question1.__dict__

question2 = Question(2, "how to bog", "arthur bark")
no = len(questions) + 1
questions[no] = question2.__dict__


@app.route('/v1/questions' ,methods=['GET', 'POST'])
def fetch_all_questions():
    if request.method == 'POST':
        newQuestion = Question(2, request.form['detail'], request.form['author'])
        no = len(questions) + 1
        questions[no] = newQuestion.__dict__
        return jsonify(questions[no])
    else: 
        return jsonify(questions)

@app.route('/v1/questions/<int:question_id>/')
def fetch_single_question(question_id):
    return jsonify(questions[question_id])

if __name__ == "__main__":
    app.run()

