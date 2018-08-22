from app.stack import Stack
import pytest

#application has to start with empty dictionary
def test_empty_dictionary():
    new_stack = Stack("this this")
    all_questions = new_stack.return_questions()
    assert b'author' not in all_questions

def test_type_error_question():
    with pytest.raises(TypeError):
        new_stack = Stack("this is this")
        other_question = "object"
        new_stack.add_question(other_question)

def test_type_error_answer():
    with pytest.raises(TypeError):
        new_stack = Stack("this is this")
        other_answer = "object"
        new_stack.add_answer(other_answer)