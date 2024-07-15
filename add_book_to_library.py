import model
import file_operation
import menu


def add_book():
    try:
        title = input("Enter title: ")
        authors = input("Enter authors (comma-separated): ").split(",")
        isbn = input("Enter ISBN: ")
        year = input("Enter publishing year: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        book = model.Book(title, authors, isbn, year, price, quantity)
        menu.books.append(book)
        file_operation.save_books()
        print("Book added successfully!")
    except ValueError:
        print("Invalid input. Please enter the correct data types.")
