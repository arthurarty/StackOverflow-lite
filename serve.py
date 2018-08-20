from flask import Flask, request, jsonify
from app.question import Question, return_questions, add_question, return_single_question, add_answer
app = Flask(__name__)

#fetch all questsions and add new question
@app.route('/v1/questions', methods=['GET', 'POST'])
def fetch_all_questions():

    if request.method == 'POST':
        new_question = Question(2, request.form['detail'], request.form['author'])
        add_question(new_question)

    output = return_questions()
    return jsonify(output)

#get single question
@app.route('/v1/questions/<int:question_id>/')
def fetch_single_question(question_id):
    output = return_single_question(question_id)
    return jsonify(output)

#add answer to question
@app.route('/v1/questions/<int:question_id>/answers', methods=['POST'])
def add_answer_to_question(question_id):
    answer = request.form['answer']
    output = add_answer(question_id, answer)
    return jsonify(output)

if __name__ == "__main__":
    app.run()

