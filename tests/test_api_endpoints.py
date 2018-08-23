import http.client
import pytest
import app.views as serve
from app.question import Question
#tests for the api end points

@pytest.fixture
def client():
    serve.app.config['TESTING'] = True
    client = serve.app.test_client()

    yield client

#tests get /questions end point
def test_fetch_all_question(client):
    resp = client.get('/v1/questions')
    assert b'author' not in resp.data

#tests post /questions 
def test_add_question(client):
    resp = client.post('/v1/questions', data=dict(
        detail= "big man",
        author = "arty arty"
    ))
    assert b'arty arty' in resp.data
    assert resp.status_code == 201

#test empty post to /v1/questions
def test_empty_input(client):
    resp = client.post('/v1/questions')
    assert resp.status_code == 400

#test empty author sent to /v1/questions
def test_empty_author(client):
    resp = client.post('/v1/questions', data=dict(
        detail= "big man",
        author = ""
    ))
    assert resp.status_code == 400

#test empty detail field sent to /v1/questions
def test_empty_detail(client):
    resp = client.post('/v1/questions', data=dict(
        detail= "",
        author = "arthur"
    ))
    assert resp.status_code == 400

#test get /questions/<question_id>
def test_fetch_single_question(client):
    resp=client.get('/v1/questions/1/')
    assert b'author' in resp.data

#test post /questions/<question_id>/answers
def test_adding_answer_to_question(client):
    resp = client.post('/v1/questions/1/answers', data=dict(
        answer = "this is how to",
        author = "arty"
    ))
    assert b'this is how to' in resp.data

#test for response 404
def test_status_not_found(client):
    resp=client.get('/v1/questions/4/')
    assert resp.status_code == 404

#test status code 404 on /questions/<id>/answer
def test_adding_answer_to_non_existent_question(client):
    resp = client.post('/v1/questions/4/answers', data=dict(
        answer = "this is how to",
        author = "arty"
    ))
    assert resp.status_code == 404

#post to /v1/questions/<question_id>/answer without body
def test_adding_empty_answer(client):
    resp = client.post('/v1/questions/4/answers')
    assert resp.status_code == 400

#test empty author sent to /v1/questions/<questions_id>/answers
def test_empty_post_author_answer(client):

    resp = client.post('/v1/questions/1/answers', data=dict(
        detail= "big man",
        author = ""
    ))
    assert resp.status_code == 400

#test empty detail field sent to /v1/questions/1/answers
def test_empty_post_detail_answer(client):
    resp = client.post('/v1/questions/1/answers', data=dict(
        detail= "",
        author = "arthur"
    ))
    assert resp.status_code == 400

def test_user_creation(client):
    resp = client.post('/auth/signup', data=dict(
        email = "test@test.com",
        name = "test test", 
        password = "test"
    ))
    assert b'test@test.com' in resp.data
    

    