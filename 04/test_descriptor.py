import unittest
from descriptor import Name, Mark, CurriculumDescriptor, Student


class TestStudentDescriptor(unittest.TestCase):
    def test_valid_data(self):
        student = Student("Иван", 5, ["Математика", "История", "Физика"])
        self.assertEqual(student.name, "Иван")
        self.assertEqual(student.marks, 5)
        self.assertEqual(student.curriculum, ["Математика", "История", "Физика"])

    def test_invalid_marks(self):
        with self.assertRaises(ValueError):
            student = Student("Иван", 7, ["Математика", "История", "Физика"])

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            student = Student("Длинное имя, которое не должно быть допущено", 5, ["Математика", "История", "Физика"])

    def test_invalid_curriculum(self):
        with self.assertRaises(ValueError):
            student = Student("Иван", 5, ["Математика", "Биология"])
