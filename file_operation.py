import json
import menu
import model


def save_books():
    with open("books.json", "w") as f:
        json.dump([book.__dict__ for book in menu.books], f, indent=4)


def load_books():
    try:
        with open("books.json", "r") as f:
            books_data = json.load(f)
            menu.books = [model.Book(**data) for data in books_data]
    except FileNotFoundError:
        menu.books = []


def save_lending_records():
    with open("lending_records.json", "w") as f:
        json.dump(
            [
                {"book": record.book.__dict__, "lent_to": record.lent_to}
                for record in menu.lending_records
            ],
            f,
            indent=4,
        )


def load_lending_records():
    try:
        with open("lending_records.json", "r") as f:
            records_data = json.load(f)
            menu.lending_records = [
                model.LendingRecord(model.Book(**record["book"]), record["lent_to"])
                for record in records_data
            ]
    except FileNotFoundError:
        menu.lending_records = []
