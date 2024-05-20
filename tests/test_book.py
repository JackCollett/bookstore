from lib.book import *

"""
Given our ID,author, title   
we construct the fields 
"""
def test_construct_book_object():
    book = Book(1, "J.K Rowling", "The Philosopher's Stone")
    assert book._id == 1
    assert book._author == "J.K Rowling"
    assert book._title == "The Philosopher's Stone"

