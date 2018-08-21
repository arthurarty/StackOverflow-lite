from app.answer import Answer

#each question must be an instance of the question class
def test_is_instance_of_question():
    new_answer = Answer(5, "Hello there", "Nangai")
    assert isinstance(new_answer, Answer)

def test_has_attribute_id():
    new_answer = Answer(7, "Login in by", "Nangai")
    assert hasattr(new_answer, "question_id")

def test_has_attribute_author():
    new_answer = Answer(7, "Login in by", "Nangai")
    assert hasattr(new_answer, "author")

def test_has_attribute_date():
    new_answer = Answer(7, "Log in by", "Nangai")
    assert hasattr(new_answer, "date")