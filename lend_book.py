import model, file_operation, menu, search_book_by_title_isbn


def lend_book():
    term = input("Enter title or ISBN of the book to lend: ")
    results = search_book_by_title_isbn.search_books(term)
    if results:
        for idx, book in enumerate(results):
            print(
                f"{idx + 1}. Title: {book.title} | Authors: {', '.join(book.authors)} | ISBN: {book.isbn} | Year: {book.year} | Price: {book.price}"
            )

        try:
            choice = int(input("Enter the number of the book you want to lend: "))
            if 1 <= choice <= len(results):
                book_to_lend = results[choice - 1]

                if book_to_lend.quantity > 0:
                    lent_to = input("Enter the name of the person lending to: ")
                    for book in menu.books:
                        if book.isbn == book_to_lend.isbn:
                            book.quantity -= 1
                            break
                    lending_record = model.LendingRecord(book_to_lend, lent_to)
                    menu.lending_records.append(lending_record)
                    file_operation.save_books()
                    file_operation.save_lending_records()
                    print("Book lend successfully!")
                else:
                    print("Not enough books available to lend.")

            else:
                print(
                    "Invalid choice. Please enter a number corresponding to the listed books."
                )

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    else:
        print("Book not found.")
