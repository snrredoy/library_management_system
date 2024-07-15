import menu


def view_lending_records():
    for record in menu.lending_records:
        print(
            f"Book: {record.book.title} | Authors : {', '.join(record.book.authors)} | ISBN : {record.book.isbn} | Year : {record.book.year} | Price : {record.book.price} | Lent to: {record.lent_to}"
        )
