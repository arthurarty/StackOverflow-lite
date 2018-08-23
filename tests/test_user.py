from app.user import User

#each question must be an instance of the question class
def test_is_instance_of_user():
    new_user = User("arthur.nangai@gmail.com", "Arthur Nangai", "Nangai")
    assert isinstance(new_user, User)