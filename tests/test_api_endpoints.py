import http.client
import pytest
import flaskServer
from app.question import Question
#tests for the api end points

@pytest.fixture
def client():
    flaskServer.app.config['TESTING'] = True
    client = flaskServer.app.test_client()

    yield client

#tests get /questions end point
def test_fetch_all_question(client):
    rv = client.get('/v1/questions')
    assert b'author' in rv.data

#tests post /questions 
def test_add_question(client):
    rv = client.post('/v1/questions', data=dict(
        detail= "big man",
        author = "arty arty"
    ))
    assert b'arty arty' in rv.data

#test get /questions/<question_id>
def test_fetch_single_question(client):
    rv=client.get('/v1/questions/1/')
    assert b'author' in rv.data

#test post /questions/<question_id>/answers
def test_adding_answer_to_question(client):
    rv = client.post('/v1/questions/1/answers', data=dict(
        answer = "this is how to"
    ))
    assert b'this is how to' in rv.data
