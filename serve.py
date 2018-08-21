from flask import Flask, request, jsonify
from app.question import Question, return_questions, add_question, return_single_question, add_answer
from app.answer import Answer

app = Flask(__name__)

#fetch all questsions and add new question
@app.route('/v1/questions', methods=['GET', 'POST'])
def fetch_all_questions():

    #check method used to send data
    if request.method == 'POST':

        #check if length of author field
        if len(request.form['author']) > 0 and len(request.form['detail']) > 0:
            new_question = Question(2, request.form['detail'], request.form['author'])
            output = add_question(new_question)
            resp = jsonify(output)
            resp.status_code = 201
            return resp

        else:
            output = {
                'message': 'Author field or details field is empty'
            }
            resp = jsonify(output)
            resp.status_code = 400
            return resp

    output = return_questions()
    resp = jsonify(output)
    resp.status_code = 200
    return resp


#get single question
@app.route('/v1/questions/<int:question_id>/')
def fetch_single_question(question_id):
    output = return_single_question(question_id)
   
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
    
    if len(request.form['author']) > 0 and len(request.form['answer']) > 0:
        new_answer = Answer(question_id, request.form['answer'], request.form['author'])
        output = add_answer(new_answer)
          
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

    output = {
                'message': 'Author field or details field is empty'
            }
    resp = jsonify(output)
    resp.status_code = 400
    return resp

if __name__ == "__main__":
    app.run()

