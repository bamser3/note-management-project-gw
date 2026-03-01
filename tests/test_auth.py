import pytest
from notes_cli.auth.user_class import User

def test_user_creation():
    user = User("Peter", "peter@gmail.com", "password123")
    assert user.name == "Peter"
    assert user.email == "peter@gmail.com"
    assert user.role == "user"

def test_password_verification():
    user = User("Peter", "peter@gmail.com", "password123")
    assert user.verify_password("password123") == True
    assert user.verify_password("wrongpassword") == False

def test_user_to_dict():
    user = User("Peter", "peter@gmail.com", "password123")
    data = user.to_dict()
    assert data["name"] == "Peter"
    assert data["email"] == "peter@gmail.com"
    assert data["role"] == "user"

def test_user_to_dict():
    user = User("Peter", "peter@gmail.com", "password123")
    data = user.to_dict()
    user2 = User.to_dict(data)
    assert user2.name == "Peter"
    assert user2.email == "peter@gmail.com"





