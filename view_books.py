import menu


def view_books():
    for book in menu.books:
        print(
            f"Title: {book.title} | Authors: {', '.join(book.authors)} | ISBN: {book.isbn} | Year: {book.year} | Price: {book.price} | Quantity: {book.quantity}"
        )
