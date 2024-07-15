class Book:
    def __init__(self, title, authors, isbn, year, price, quantity):
        self.title = title
        self.authors = authors
        self.isbn = isbn
        self.year = year
        self.price = price
        self.quantity = quantity


class LendingRecord:
    def __init__(self, book, lent_to):
        self.book = book
        self.lent_to = lent_to
