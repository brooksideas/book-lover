##############################
# File name booklover_test.py#
##############################
import unittest
from booklover import BookLover


class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        # add a book and test if it is in `book_list`.
        book = BookLover("Brook", "rnc3mm@virginia.com", "Romance-drama")
        book.add_book("The Best of me", 5)
        actual = book.book_list["book_name"][0]
        expected = "The Best of me"
        self.assertEqual(actual, expected)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        book = BookLover("Brook", "rnc3mm@virginia.com", "Romance-drama")
        book.add_book("The Best of me", 5)
        # Second duplication error is raised
        with self.assertRaises(ValueError) as exception_context:
            book.add_book("The Best of me", 4)
        self.assertEqual(
            str(exception_context.exception),
            "Book already exists."
        )
        actual = len(book.book_list.index)
        expected = 1
        self.assertTrue(actual == expected)  # Check it is only added once

    def test_3_has_read(self):
        # pass a book in the list and test if the answer is `True`.
        book = BookLover("Brook", "rnc3mm@virginia.com", "Romance-drama")
        book.add_book("The Best of me", 5)
        book.book_list
        # Correctly passed value
        actual = book.has_read("The Best of me")
        self.assertTrue(actual[0])

    def test_4_has_read(self):
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        # pass a book in the list and test if the answer is `True`.
        book = BookLover("Brook", "rnc3mm@virginia.com", "Romance-drama")
        book.add_book("The Best of me", 5)
        book.book_list
        # Correctly passed value
        actual = book.has_read("Introduction to DS")
        self.assertFalse(actual[0])

    def test_5_num_books_read(self):
        # add some books to the list, and test num_books matches expected.
        book = BookLover("Brook", "rnc3mm@virginia.com", "Romance-drama")
        book.add_book("The Best of me", 5)
        book.add_book("Introduction to DS", 4)
        book.add_book("Fundamentals to CS", 2)
        actual = book.num_books_read()
        expected = 3
        self.assertEqual(actual, expected)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3.
        # Your test should check that the returned books have rating  > 3
        book = BookLover("Brook", "rnc3mm@virginia.com", "Romance-drama")
        book.add_book("The Best of me", 5)
        book.add_book("Introduction to DS", 4)
        book.add_book("Fundamentals to CS", 2)
        actual = len(book.fav_books())  # Must have at least one book rated over 3
        expected = 1
        self.assertGreaterEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=3)
