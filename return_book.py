import menu, file_operation


def return_book():
    term = input("Enter title or ISBN of the book to return: ")
    matching_books = []
    term = term.lower()

    for book in menu.lending_records:
        if term in book.book.title.lower() or term in book.book.isbn.lower():
            matching_books.append(book)

    if matching_books:
        print("Books found:")
        for idx, book in enumerate(matching_books):
            print(
                f"{idx + 1}. Title: {book.book.title}, Authors: {', '.join(book.book.authors)}, ISBN: {book.book.isbn}  , Lend to: {book.lent_to}"
            )

        try:
            choice = int(input("Enter the number of the book you want to return: "))
            if 1 <= choice <= len(matching_books):
                book_to_return = matching_books[idx]

                # Find the lending record to remove
                for record in menu.lending_records:
                    if record.book.isbn == book_to_return.book.isbn:
                        menu.lending_records.remove(record)
                        break

                # Update book quantity
                for book in menu.books:
                    if book.isbn == book_to_return.book.isbn:
                        book.quantity += 1
                        break

                file_operation.save_books()
                file_operation.save_lending_records()
                print("Book returned successfully!")
            else:
                print(
                    "Invalid choice. Please enter a number corresponding to the listed books."
                )
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Book not found.")
