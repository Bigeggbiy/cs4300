# test_task5.py
from task5 import favorite_books, student_database

def test_favorite_books():
    books = favorite_books()
    assert len(books) == 3

def test_student_database():
    db = student_database()
    assert db["Alice"] == 1001