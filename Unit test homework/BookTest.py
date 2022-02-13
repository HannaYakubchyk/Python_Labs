import unittest
from unittest import TestCase

import self

import Book


class BookTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set Up Class Method!"""
        print("Setting up class for tests!")
        print("==========================")

    @classmethod
    def tearDownClass(cls):
        """Tear Down Class Method!"""
        print("==========================")
        print("Cleaning mess after testing!")

    def setUp(self):
        """Set Up Method!"""
        print("Setting up for a test")
        print("==========================")

    def tearDown(self):
        """Tear Down Method!"""
        print("==========================")
        print("Cleaning mess after a test")

    def test_how_old_is_the_book(self):
        self.assertEqual(Book.book1.how_old_is_the_book(2020), 2)

    def test_current_year_of_publishment(self):
        self.assertEqual(Book.book1.current_year_of_publishment(), 2022)

    def test_compare(self):
        self.assertTrue(Book.Book.__cmp__(Book.book1, Book.book2))

    def test_show_book_info(self):
        self.assertMultiLineEqual("твердый", Book.book2.coverType)

    def test_str(self):
        self.assertEqual(Book.book1.__str__(), Book.book1.get_id())


if __name__ == '__main__':
    unittest.main()
