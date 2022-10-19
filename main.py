from booklover import BookLover

book = BookLover("brook", "emails", "action")

book.add_book("new book", 5)
book.add_book("NEW BOOK", 3.1)
book.add_book("NEW BOOKs", 5)
# book.add_book("new book", 3)
# book.add_book("new books", 3)
# book.add_book(1.2, 3)

# book.has_read(2)
# book.has_read("New book")
# book.has_read("  new book  ")
# print(book.has_read("new book"))

# print(book.num_books_read())

book.fav_books()
