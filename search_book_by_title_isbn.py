import menu


def search_books(term):

    matching_books = []
    term = term.lower()

    for book in menu.books:
        if term in book.title.lower() or term in book.isbn.lower():
            matching_books.append(book)

    return matching_books
