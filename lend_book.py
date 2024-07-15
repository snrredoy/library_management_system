import model, file_operation, menu, search_book_by_title_isbn


def lend_book():
    term = input("Enter title or ISBN of the book to lend: ")
    results = search_book_by_title_isbn.search_books(term)
    if results:
        for idx, book in enumerate(results):
            print(
                f"{idx + 1}. Title: {book.title}, Authors: {', '.join(book.authors)}, ISBN: {book.isbn}"
            )

        try:
            choice = int(input("Enter the number of the book you want to lend: "))
            if idx + 1 == choice:
                if results[idx].quantity > 0:
                    lent_to = input("Enter the name of the person lending to: ")
                    results[idx].quantity -= 1
                    lending_record = model.LendingRecord(results[idx], lent_to)
                    menu.lending_records.append(lending_record)
                    file_operation.save_books()
                    file_operation.save_lending_records()
                    print("Book lent successfully!")
            else:
                print("Not enough books available to lend.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    else:
        print("Book not found.")
