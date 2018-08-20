from app.question import Question, add_answer, add_question, return_questions, return_single_question

def test_empty_dictionary():
    all_questions = return_questions()
    assert b'author' not in all_questions

def test_is_instance_of_question():
    new_question = Question(5, "Hello there", "Nangai")
    assert isinstance(new_question, Question)

def test_has_attribute_id():
    new_question = Question(7, "How to login", "Nangai")
    assert hasattr(new_question, "user_id")

def test_has_attribute_author():
    new_question = Question(7, "How to login", "Nangai")
    assert hasattr(new_question, "author")

def test_has_attribute_date():
    new_question = Question(7, "How to login", "Nangai")
    assert hasattr(new_question, "date")

def test_has_attribute_list():
    new_question = Question(7, "How to login", "Nangai")
    assert hasattr(new_question, "answers")



