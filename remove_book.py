import menu
import file_operation


def remove_book():
    term = input("Enter title of the book to remove: ")
    matching_books = []
    term = term.lower()

    for book in menu.books:
        if term in book.title.lower():
            matching_books.append(book)

    if matching_books:
        for idx, book in enumerate(matching_books):
            print(
                f"{idx + 1}. Title: {book.title}, Authors: {', '.join(book.authors)}, ISBN: {book.isbn}"
            )

        try:
            choice = int(input("Enter the number of the book you want to remove: "))
            if idx + 1 == choice:
                menu.books.remove(matching_books[choice - 1])
                file_operation.save_books()
                print("Book removed successfully!")
            else:
                print(
                    "Invalid choice. Please enter a number corresponding to the listed books."
                )
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Book not found.")
