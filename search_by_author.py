import menu


def search_books_by_author(author):

    author = author.lower()
    matching_books = []

    for book in menu.books:
        for auth in book.authors:
            if author in auth.lower():
                matching_books.append(book)
                break

    return matching_books
