from flask import Flask, request, jsonify
from app.question import Question
app = Flask(__name__)

questions = {}

question1 = Question(1, "how to log", "arthur nangai")
no_of_questions = len(questions) + 1
questions[no_of_questions] = question1.__dict__

question2 = Question(2, "how to bog", "arthur bark")
no_of_questions = no_of_questions + 1
questions[no_of_questions] = question2.__dict__

#fetch all questsion
@app.route('/v1/questions', methods=['GET', 'POST'])
def fetch_all_questions():
    if request.method == 'POST':
        new_question = Question(2, request.form['detail'], request.form['author'])
        no_of_question = len(questions) + 1
        questions[no_of_question] = new_question.__dict__
        return jsonify(questions[no_of_question])
    return jsonify(questions)

#get single question
@app.route('/v1/questions/<int:question_id>/')
def fetch_single_question(question_id):
    return jsonify(questions[question_id])

#add answer to question
@app.route('/v1/questions/<int:question_id>/answers', methods=['POST'])
def add_answer(question_id):
    question = questions[question_id]
    question['answers'].append(request.form['answer'])
    return jsonify(question['answers'])

if __name__ == "__main__":
    app.run()

