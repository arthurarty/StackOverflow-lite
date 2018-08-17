from app.question import Question

def test_is_instance_of_question():
    question1 = Question(5, "Hello there", "Nangai")
    assert isinstance(question1, Question)

def test_has_attribute_id():
    question1 = Question(7, "How to login", "Nangai")
    assert hasattr(question1, "id")

def test_has_attribute_author():
    question1 = Question(7, "How to login", "Nangai")
    assert hasattr(question1, "author")

def test_has_attribute_date():
    question1 = Question(7, "How to login", "Nangai")
    assert hasattr(question1, "date")

def test_has_attribute_list():
    question1 = Question(7, "How to login", "Nangai")
    assert hasattr(question1, "answers")
