from app.question import Question

def test_is_instance_of_question():
    question1 = Question(5, "Hello there")
    assert isinstance(question1, Question)

def test_has_attribute_id():
    question1 = Question(7, "How to login")
    assert hasattr(question1, "id")