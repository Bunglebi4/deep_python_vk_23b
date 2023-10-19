import unittest
from descriptor import NewBook


class TestNewBookDescriptor(unittest.TestCase):
    def test_valid_data(self):
        new_book = NewBook("C++", 500, 'Programming')
        self.assertEqual(new_book.name, "C++")
        self.assertEqual(new_book.price, 500)
        self.assertEqual(new_book.genres, 'Programming')

    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            new_book = NewBook("sHILD", -7, "Programming")
            return new_book

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            new_book = NewBook("LOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOng",
                               500, "Programming")
            return new_book

    def test_invalid_genre(self):
        with self.assertRaises(ValueError):
            new_book = NewBook("C", 5, "boba")
            return new_book

    def test_invalid_change_price(self):
        new_book = NewBook("C", 5, "Chess")
        with self.assertRaises(ValueError):
            new_book.price = -5
            return new_book

    def test_invalid_change_name(self):
        new_book = NewBook("C", 5, "Chess")
        with self.assertRaises(ValueError):
            new_book.name = "-5" * 200
            return new_book

    def test_invalid_change_genres(self):
        new_book = NewBook("C", 5, "Chess")
        with self.assertRaises(ValueError):
            new_book.genres = "cringe"
            return new_book

    def test_value_genre_save_after_error(self):
        new_book = NewBook("C", 5, "Chess")
        with self.assertRaises(ValueError):
            new_book.genres = "cringe"
            return new_book
        self.assertEqual(new_book.genres, "Chess")

    def test_value_name_save_after_error(self):
        new_book = NewBook("C", 5, "Chess")
        with self.assertRaises(ValueError):
            new_book.name = "cringe"*100
            return new_book
        self.assertEqual(new_book.name, "C")

    def test_value_price_save_after_error(self):
        new_book = NewBook("C", 5, "Chess")
        with self.assertRaises(ValueError):
            new_book.price = -100
            return new_book
        self.assertEqual(new_book.price, 5)

    def test_invalid_marks_negative(self):
        with self.assertRaises(ValueError):
            new_book = NewBook("Haskell", -3, "Chess")
            return new_book

    def test_valid_genre_empty(self):
        with self.assertRaises(ValueError):
            return NewBook("python", 4000, [])

    def test_valid_name_maximum_length(self):
        name = "l" + "O" * 33 + "ng"
        new_book = NewBook(name, 4, "Non-Fiction")
        self.assertEqual(new_book.name, name)

    def test_invalid_name_maximum_length_exceeded(self):
        with self.assertRaises(ValueError):
            name = "A" * 37
            new_book = NewBook(name, 4, "Non-Fiction")
            return new_book
