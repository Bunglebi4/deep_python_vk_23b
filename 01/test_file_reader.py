import io
import os
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
        with open(
                'test_files_for_file_reader/good_file.txt',
                encoding='UTF-8'
        ) as file_obj:
            model = LineFinder(file_obj, ["garbage"])
        with patch('file_reader.LineFinder.find_intersection') as mock:
            mock.return_value = {}
            self.assertEqual(list(model.find_good_strings()), [])

    def test_initialization_with_file_object(self):
        with open(
                'test_files_for_file_reader/good_file.txt',
                encoding='UTF-8'
        ) as file_obj:
            model = LineFinder(file_obj, ["Momma", "Imma", "Criminal"])
        self.assertIsInstance(model.file_list, list)
        self.assertIsInstance(model.set_of_words, set)

    def test_initialization_with_file_string(self):
        model = LineFinder(
            'test_files_for_file_reader/good_file.txt',
            ["Momma", "Imma", "Criminal"]
        )
        self.assertIsInstance(model.file_list, list)
        self.assertIsInstance(model.set_of_words, set)

    def test_file_not_found_error(self):
        with self.assertRaises(FileNotFoundError):
            LineFinder('buba/good_file.txt', ["Momma", "Imma", "Criminal"])

    def test_init_with_empty_file(self):
        file = io.StringIO("")
        with self.assertRaises(TypeError):
            LineFinder(file, ["Роза"])

    def test_find_good_strings_with_case_insensitivity(self):
        file_content = "Роза красная\nРОЗА синяя"
        with open("test_file.txt", "w", encoding="utf-8") as file_obj:
            file_obj.write(file_content)
        finder = LineFinder("test_file.txt", ["роза"])
        good_strings = list(finder.find_good_strings())
        self.assertEqual(good_strings, ["Роза красная", "РОЗА синяя"])

    def test_find_good_strings_with_no_match(self):
        file_content = "Шарик бежит\nКот спит"
        with open("test_file.txt", "w", encoding="utf-8") as file_obj:
            file_obj.write(file_content)
        finder = LineFinder("test_file.txt", ["роза"])
        good_strings = list(finder.find_good_strings())
        self.assertEqual(good_strings, [])

    def test_find_good_strings_with_two_match(self):
        file_content = "Шарик бежит\nКот спит"
        with open("test_file.txt", "w", encoding="utf-8") as file_obj:
            file_obj.write(file_content)
        finder = LineFinder("test_file.txt", ["Шарик", "спит"])
        good_strings = list(finder.find_good_strings())
        self.assertEqual(good_strings, ["Шарик бежит", "Кот спит"])

    def test_find_good_strings_with_two_filters(self):
        file_content = "Шарик бежит\nКот спит"
        with open("test_file.txt", "w", encoding="utf-8") as file_obj:
            file_obj.write(file_content)
        finder = LineFinder("test_file.txt", ["Кот", "спит"])
        good_strings = list(finder.find_good_strings())
        self.assertEqual(good_strings, ["Кот спит"])

    def test_find_good_strings_with_two_cases(self):
        file_content = "Шарик бежит\nКОТ СПИТ"
        with open("test_file.txt", "w", encoding="utf-8") as file_obj:
            file_obj.write(file_content)
        finder = LineFinder("test_file.txt", ["КОТ", "спит"])
        good_strings = list(finder.find_good_strings())
        self.assertEqual(good_strings, ["КОТ СПИТ"])

    def test_find_good_strings_with_full_intersection(self):
        file_content = "Шарик"
        with open("test_file.txt", "w", encoding="utf-8") as file_obj:
            file_obj.write(file_content)
        finder = LineFinder("test_file.txt", ["Шарик"])
        good_strings = list(finder.find_good_strings())
        self.assertEqual(good_strings, ["Шарик"])

    def tearDown(self):
        try:
            os.remove("test_file.txt")
        except FileNotFoundError:
            pass
