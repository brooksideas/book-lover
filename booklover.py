class BookLover:
    '''
    PURPOSE:
    A class to identify a Book Lover.

    ATTRIBUTES:
    name: The name of the person (type:string)
    email: The person’s email, serving as a unique identifier (type:string)
    fav_genre: The person’s favorite book genre (e.g., mystery, fantasy, or historical fiction). (type:string)

    METHODS:
    __init__ : Initialize with the three required attributes (name, email, and fav_genre) and two optional ones
    (num_books and book_list).
    add_book: Takes two arguments book_name and rating and add the book to the user list if it does not exist
    has_read:  This function takes book_name (string) as input and determines if the person has read the book.
    num_books_read:  This function takes no parameters and just returns the total number of books the person has read.
    fav_books: This function takes no parameters and returns the filtered dataframe of the person’s most favorite books.
    -------------------------------------------------------------------------
    '''
