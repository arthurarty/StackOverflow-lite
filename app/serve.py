from flask import Flask, request, jsonify
from app.question import Question
from app.answer import Answer
from app.stack import Stack

app = Flask(__name__)
"""route /v1/questions allows two methods get and post. 
the post method is used to add a new question
the get method is used to return all questios
"""
new_stack = Stack("stack over")
@app.route('/v1/questions', methods=['GET', 'POST'])
def fetch_all_questions():

    """post method to add new question """
    if request.method == 'POST':

        #check if length of author field
        if request.form['author'] and request.form['detail']:
            new_question = Question(2, request.form['detail'], request.form['author'])
            output = new_stack.add_question(new_question)
            resp = jsonify(output)
            resp.status_code = 201
            return resp

        output = {'message': 'Author field or details field is empty'}
        resp = jsonify(output)
        resp.status_code = 400
        return resp

    output = new_stack.return_questions()
    resp = jsonify(output)
    resp.status_code = 200
    return resp

@app.route('/v1/questions/<int:question_id>/')
def fetch_single_question(question_id):
    """fetch_single_questions method returns single question with input being of the type int. 
    """
    output = new_stack.return_single_question(question_id)
   
    if output == 0:
        output = {
            'message': 'Question Not Found: ' + request.url,
        }
        resp = jsonify(output)
        resp.status_code = 404
        return resp

    resp = jsonify(output)
    resp.status_code = 200
    return resp

#add answer to question
@app.route('/v1/questions/<int:question_id>/answers', methods=['POST'])
def add_answer_to_question(question_id):
    """method to add answer to question"""
    if request.form['author'] and request.form['answer']:
        new_answer = Answer(question_id, request.form['answer'], request.form['author'])
        output = new_stack.add_answer(new_answer)
          
        if output == 0:
            output = {
                'message': 'Question Not Found so cant add comment: ' + request.url,
            }
            resp = jsonify(output)
            resp.status_code = 404
            return resp

        resp = jsonify(output)
        resp.status_code = 200
        return resp

    output = {'message': 'Author field or details field is empty'}
    resp = jsonify(output)
    resp.status_code = 400
    return resp
