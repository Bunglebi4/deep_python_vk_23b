import unittest
from unittest.mock import patch

from file_reader import LineFinder


class TestEstimating(unittest.TestCase):

    def test_intersection_with_good_input(self):
        self.assertEqual(LineFinder.find_intersection(
            {"роза", "яблоко"},
            "роза упала на лапу Азора Яблоко груша апельсин"),
            {"роза", "яблоко"}
        )

    def test_intersection_with_no_input(self):
        self.assertEqual(LineFinder.find_intersection(
            {"роза", "яблоко"},
            ""),
            set()
        )

    def test_intersection_with_bad_input(self):
        model = LineFinder
        with self.assertRaises(AttributeError):
            model.find_intersection({"роза", "яблоко"}, 23)

    def test_find_string_with_no_intersections(self):
        with open('test_files_for_file_reader/good_file.txt', encoding='UTF-8') as f:
            model = LineFinder(f, ["Яблоко"])
        with patch('file_reader.LineFinder.find_intersection') as mock:
            mock.return_value = {}
            self.assertEqual(list(model.find_good_strings()), [])
