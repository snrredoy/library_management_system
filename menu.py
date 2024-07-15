import add_book_to_library, view_books, file_operation, search_book_by_title_isbn, search_by_author, remove_book, lend_book, view_lending_records, return_book


books = []
lending_records = []


def show_menu():
    print("Library Management System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Books By Title or ISBN")
    print("4. Search Books by Author")
    print("5. Remove Book")
    print("6. Lend Book")
    print("7. View Lending Records")
    print("8. Return Book")
    print("0. Exit")
    print("\n")


def main():
    file_operation.load_books()
    file_operation.load_lending_records()

    while True:
        show_menu()
        choice = input("Enter your choice: ")
        print("\n")

        if choice == "1":
            add_book_to_library.add_book()
            print("\n")

        elif choice == "2":
            view_books.view_books()
            print("\n")

        elif choice == "3":
            term = input("Enter search term (title or ISBN): ")
            results = search_book_by_title_isbn.search_books(term)
            if results:
                for book in results:
                    print(
                        f"Title: {book.title} | Authors: {', '.join(book.authors)} | ISBN: {book.isbn} | Year: {book.year} | Price: {book.price} | Quantity: {book.quantity}"
                    )
            else:
                print("No books found matching the search term.")
            print("\n")

        elif choice == "4":
            author = input("Enter author name: ")
            results = search_by_author.search_books_by_author(author)
            if results:
                for book in results:
                    print(
                        f"Title: {book.title} | Authors: {', '.join(book.authors)} | ISBN: {book.isbn} | Year: {book.year} | Price: {book.price}"
                    )
            else:
                print("No books found matching the author name.")
            print("\n")

        elif choice == "5":
            remove_book.remove_book()
            print("\n")

        elif choice == "6":
            lend_book.lend_book()
            print("\n")

        elif choice == "7":
            view_lending_records.view_lending_records()
            print("\n")

        elif choice == "8":
            return_book.return_book()
            print("\n")

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
