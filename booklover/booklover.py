#########################
# File name booklover.py#
#########################
import pandas as pd
import re

"""
Student Info 
Name: Brook Tarekegn Assefa
Net UD: rnc3mm
URL of this file in GitHub:  https://github.com/brooksideas/DS5100-2022-08-rnc3mm/tree/main/lessons/M08
"""


class BookLover:
    """
    PURPOSE:
    A class to identify a Book Lover.

    ATTRIBUTES:
    name: The name of the person (type:string)
    email: The person’s email, serving as a unique identifier (type:string)
    fav_genre: The person’s favorite book genre (e.g., mystery, fantasy, or historical fiction). (type:string)
    num_books: Keeps track of the number of books the person has read (type:int)
    book_list: a dataframe with the columns ['book_name', 'book_rating']

    METHODS:
    __init__ : Initialize with the three required attributes (name, email, and fav_genre) and two optional ones
    (num_books and book_list).
    add_book: Takes two arguments book_name and rating and add the book to the user list if it does not exist
    has_read:  This function takes book_name (string) as input and determines if the person has read the book.
    num_books_read:  This function takes no parameters and just returns the total number of books the person has read.
    fav_books: This function takes no parameters and returns the filtered dataframe of the person’s most favorite books.
    -------------------------------------------------------------------------
    """

    name = ""
    email = ""
    fav_genre = ""
    num_books = 0
    book_list = pd.DataFrame({'book_name': [], 'book_rating': []})

    def __init__(self, name, email, fav_genre, num_books=num_books, book_list=book_list):
        # Check book name is a string
        if not isinstance(name, str):
            raise TypeError("Book name should be a string.")

        # Check that email is correct
        # for validating an Email
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z.-]+\.[A-Z|a-z]{2,}\b'
        if not (re.fullmatch(regex, email)):
            raise TypeError("The email passed is Invalid.")

        # Check book favorite genre is a string
        if not isinstance(fav_genre, str):
            raise TypeError("Book favorite genre should be a string.")

        # Number of books should be Int
        if not isinstance(num_books, int):
            raise TypeError("The number of Books passed should be an integer.")
        # Check if the book list passed is a Data frame
        if not isinstance(book_list, pd.DataFrame):
            raise TypeError("The book list should be a Dataframe.")

        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list

    def add_book(self, book_name, rating):

        # Check if rating is in the integer from 0 to 5
        if rating not in range(0, 6, 1) or not isinstance(rating, int):
            raise ValueError("Rating should be an integer in the range from 0 to 5. Rating ", rating,
                             "is out of range.")

        # Check if the Book exists in the book list Dataframe
        if len(self.book_list) != 0:
            matches = set(self.book_list['book_name'].str.lower()).intersection(set([book_name.strip().lower()]))
            if len(matches) != 0:
                raise ValueError("Book already exists.")

        # Add the new book to the Dataframe
        added_book = pd.DataFrame({
            'book_name': [book_name],
            'book_rating': [rating]
        })

        self.book_list = pd.concat([self.book_list, added_book], ignore_index=True)

    def has_read(self, book_name):
        # Check book name is a string
        if not isinstance(book_name, str):
            raise TypeError("Book name should be a string.")

        # Check if it is present
        found = book_name.strip().lower() == self.book_list['book_name'].str.lower()
        return found

    def num_books_read(self):
        return len(self.book_list.index)

    def fav_books(self):
        # ret = self.book_list[self.book_list['book_rating'] > 3]
        # xx = ret["book_rating"]
        return self.book_list[self.book_list['book_rating'] > 3]


if __name__ == '__main__':
    book = BookLover("Brook", "rnc3mm@virginia.com", "Romance-drama")
