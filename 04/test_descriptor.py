import unittest
from descriptor import Student


class TestStudentDescriptor(unittest.TestCase):
    def test_valid_data(self):
        student = Student("Иван", 5, ["Математика", "История", "Физика"])
        self.assertEqual(student.name, "Иван")
        self.assertEqual(student.marks, 5)
        self.assertEqual(student.curriculum, ["Математика", "История", "Физика"])

    def test_invalid_marks(self):
        with self.assertRaises(ValueError):
            student = Student("Иван", 7, ["Математика", "История", "Физика"])
            return student

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            student = Student("Длинное имя, которое не должно быть допущено",
                              5, ["Математика", "История", "Физика"])
            return student

    def test_invalid_curriculum(self):
        with self.assertRaises(ValueError):
            student = Student("Иван", 5, ["Математика", "Биология"])
            return student

    def test_invalid_marks_negative(self):
        with self.assertRaises(ValueError):
            student = Student("Иван", -3, ["Математика", "История", "Физика"])
            return student

    def test_valid_curriculum_empty(self):
        student = Student("Иван", 4, [])
        self.assertEqual(student.curriculum, [])

    def test_valid_curriculum_with_spaces(self):
        student = Student("Иван", 4, ["Математика", "История", "Физика"])
        self.assertEqual(student.curriculum, ["Математика", "История", "Физика"])

    def test_valid_name_maximum_length(self):
        name = "A" * 36
        student = Student(name, 4, ["Математика", "История"])
        self.assertEqual(student.name, name)

    def test_invalid_name_maximum_length_exceeded(self):
        with self.assertRaises(ValueError):
            name = "A" * 37
            student = Student(name, 4, ["Математика", "История"])
            return student
