import os
import unittest
from unittest.mock import patch
from file_reader import find_intersection, find_good_strings


class TestEstimating(unittest.TestCase):

    def test_intersection_with_good_input(self):
        self.assertEqual(find_intersection(
            {"роза", "яблоко"},
            "роза упала на лапу Азора Яблоко груша апельсин"),
            {"роза", "яблоко"}
        )

    def test_intersection_with_no_input(self):
        self.assertEqual(find_intersection(
            {"роза", "яблоко"},
            ""),
            set()
        )

    def test_intersection_with_bad_input(self):
        with self.assertRaises(AttributeError):
            find_intersection({"роза", "яблоко"}, 23)

    def test_find_string_with_no_intersections(self):
        with open(
                'test_files_for_file_reader/good_file.txt',
                encoding='UTF-8'
        ) as file_obj:
            with patch('file_reader.find_intersection') as mock:
                mock.return_value = {}
                self.assertEqual(list(
                    find_good_strings(file_obj, ["garbage"])), [])

    def test_file_not_found_error(self):
        with self.assertRaises(FileNotFoundError):
            list(find_good_strings(
                'buba/good_file.txt',
                ["Momma", "Imma", "Criminal"]
            ))

    def test_find_good_strings_with_case_insensitivity(self):
        file_content = "Роза красная\nРОЗА синяя"
        with open("test_file.txt", "w", encoding="utf-8") as file_obj:
            file_obj.write(file_content)
        good_strings = list(find_good_strings("test_file.txt", ["роза"]))
        self.assertEqual(good_strings, ["Роза красная", "РОЗА синяя"])

    def test_find_good_strings_with_no_match(self):
        file_content = "Шарик бежит\nКот спит"
        with open("test_file.txt", "w", encoding="utf-8") as file_obj:
            file_obj.write(file_content)
        good_strings = list(find_good_strings("test_file.txt", ["роза"]))
        self.assertEqual(good_strings, [])

    def test_find_good_strings_with_two_match(self):
        file_content = "Шарик бежит\nКот спит"
        with open("test_file.txt", "w", encoding="utf-8") as file_obj:
            file_obj.write(file_content)
        good_strings = list(find_good_strings(
            "test_file.txt", ["Шарик", "спит"]
        ))
        self.assertEqual(good_strings, ["Шарик бежит", "Кот спит"])

    def test_find_good_strings_with_two_filters(self):
        file_content = "Шарик бежит\nКот спит"
        with open("test_file.txt", "w", encoding="utf-8") as file_obj:
            file_obj.write(file_content)
        good_strings = list(find_good_strings(
            "test_file.txt", ["Кот", "спит"])
        )
        self.assertEqual(good_strings, ["Кот спит"])

    def test_find_good_strings_with_two_cases(self):
        file_content = "Шарик бежит\nКОТ СПИТ"
        with open("test_file.txt", "w", encoding="utf-8") as file_obj:
            file_obj.write(file_content)
        good_strings = list(find_good_strings(
            "test_file.txt", ["КОТ", "спит"]))
        self.assertEqual(good_strings, ["КОТ СПИТ"])

    def test_find_good_strings_with_full_intersection(self):
        file_content = "Шарик"
        with open("test_file.txt", "w", encoding="utf-8") as file_obj:
            file_obj.write(file_content)
        good_strings = list(find_good_strings("test_file.txt", ["Шарик"]))
        self.assertEqual(good_strings, ["Шарик"])

    def tearDown(self):
        try:
            os.remove("test_file.txt")
        except FileNotFoundError:
            pass
