"""
Decorator!

Problem
	* Uncertainties in types of objects
	* Decisions to be made at runtime regarding what class to use
"""


class Book(object):
    """docstring for Book"""

    def __init__(self, author, title):
        self.author = author
        self.title = title


class BookDecorator(Book):
    book = None

    def __init__(self, book):
        self.book = book

    def author_title(self):
        return self.book.author + ' - ' + self.book.title

decorator = BookDecorator(Book('The Hobbit', 'Tolkien'))
print(decorator.authorTitle())
