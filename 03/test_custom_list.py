import unittest
from custom_list import CustomList


class TestCustomList(unittest.TestCase):

    def test_addition(self):
        a = CustomList([0, 3, 2, 3, 3])
        b = CustomList([0, 3, 1, 3, 3])
        result = a + b
        expected = CustomList([0, 6, 3, 6, 6])
        self.assertEqual(result, expected)

    def test_addition_with_different_len(self):
        a = CustomList([0, 3, 2, 3, 3])
        b = CustomList([0, 3, 1, 3, 3, 0, 1, 2])
        result = a + b
        expected = CustomList([0, 6, 3, 6, 6, 0, 1, 2])
        self.assertEqual(result, expected)

    def test_addition_with_diff_len_v_2(self):
        a = CustomList([0, 3, 2, 3, 3, 1, 2])
        b = CustomList([0, 3, 1, 3, 3])
        result = a + b
        expected = CustomList([0, 6, 3, 6, 6, 1, 2])
        self.assertEqual(result, expected)

    def test_addition_with_list(self):
        a = CustomList([0, 3, 2, 3, 3])
        b = [0, 3, 1, 3, 3]
        result = a + b
        expected = CustomList([0, 6, 3, 6, 6])
        self.assertEqual(result, expected)

    def test_addition_with_list_with_diff_len(self):
        a = CustomList([0, 3, 2, 3, 3, 1, 2, 3])
        b = [0, 3, 1, 3, 3]
        result = a + b
        expected = CustomList([0, 6, 3, 6, 6, 1, 2, 3])
        self.assertEqual(result, expected)

    def test_addition_with_list_with_diff_len_v2(self):
        a = CustomList([0, 3, 2, 3, 3])
        b = [0, 3, 1, 3, 3, 1, 2, 3]
        result = a + b
        expected = CustomList([0, 6, 3, 6, 6, 1, 2, 3])
        self.assertEqual(result, expected)

    def test_addition_list_with_custom_list(self):
        a = CustomList([0, 3, 2, 3, 3])
        b = [0, 3, 1, 3, 3]
        result = b + a
        expected = CustomList([0, 6, 3, 6, 6])
        self.assertEqual(result, expected)

    def test_addition_list_with_custom_with_diff_len(self):
        a = CustomList([0, 3, 2, 3, 3, 1, 2, 3])
        b = [0, 3, 1, 3, 3]
        result = b + a
        expected = CustomList([0, 6, 3, 6, 6, 1, 2, 3])
        self.assertEqual(result, expected)

    def test_addition_list_with_custom_with_diff_len2(self):
        a = CustomList([0, 3, 2, 3, 3])
        b = [0, 3, 1, 3, 3, 1, 2, 3]
        result = b + a
        expected = CustomList([0, 6, 3, 6, 6, 1, 2, 3])
        self.assertEqual(result, expected)

    def test_subtraction(self):
        a = CustomList([0, 3, 2, 3, 3])
        b = CustomList([0, 3, 1, 3, 3])
        result = a - b
        expected = CustomList([0, 0, 1, 0, 0])
        self.assertEqual(result, expected)

    def test_subtraction_with_different_len(self):
        a = CustomList([0, 3, 2, 3, 3])
        b = CustomList([0, 3, 1, 3, 3, 0, 1, 2])
        result = a - b
        expected = CustomList([0, 0, 1, 0, 0, 0, -1, -2])
        self.assertEqual(result, expected)

    def test_subtraction_with_diff_len_v_2(self):
        a = CustomList([0, 3, 2, 3, 3, 1, 2])
        b = CustomList([0, 3, 1, 3, 3])
        result = a - b
        expected = CustomList([0, 0, 1, 0, 0, 0, 1, 2])
        self.assertEqual(result, expected)

    def test_subtraction_with_list(self):
        a = CustomList([0, 3, 2, 3, 3])
        b = [0, 3, 1, 3, 3]
        result = a - b
        expected = CustomList([0, 0, 1, 0, 0])
        self.assertEqual(result, expected)

    def test_subtraction_with_list_with_diff_len(self):
        a = CustomList([0, 3, 2, 3, 3, 1, 2, 3])
        b = [0, 3, 1, 3, 3]
        result = a - b
        expected = CustomList([0, 0, 1, 0, 0, 1, 2, 3])
        self.assertEqual(result, expected)

    def test_subtraction_with_list_with_diff_len_v2(self):
        a = CustomList([0, 3, 2, 3, 3])
        b = [0, 3, 1, 3, 3, 1, 2, 3]
        result = a - b
        expected = CustomList([0, 0, 1, 0, 0, -1, -2, -3])
        self.assertEqual(result, expected)

    def test_subtraction_from_list(self):
        a = CustomList([0, 3, 2, 3, 3])
        b = [0, 3, 1, 3, 3]
        result = b - a
        expected = CustomList([0, 0, -1, 0, 0])
        self.assertEqual(result, expected)

    def test_subtraction_from_list_with_diff_len(self):
        a = CustomList([0, 3, 2, 3, 3, 1, 2, 3])
        b = [0, 3, 1, 3, 3]
        result = b - a
        expected = CustomList([0, 0, -1, 0, 0, -1, -2, -3])
        self.assertEqual(result, expected)

    def test_subtraction_with_from_with_diff_len_v2(self):
        a = CustomList([0, 3, 2, 3, 3])
        b = [0, 3, 1, 3, 3, 1, 2, 3]
        result = b - a
        expected = CustomList([0, 0, -1, 0, 0, 1, 2, 3])
        self.assertEqual(result, expected)

    def test_equality(self):
        a = CustomList([0, 3, 2, 3, 3])
        b = CustomList([0, 3, 2, 3, 3])
        self.assertTrue(a == b)

    def test_false_equality(self):
        a = CustomList([0, 3, 2, 3, 3])
        b = CustomList([0, 4, 2, 3, 3])
        self.assertFalse(a == b)

    def test_inequality(self):
        a = CustomList([0, 3, 2, 3, 3])
        b = CustomList([0, 3, 1, 3, 3])
        self.assertTrue(a != b)

    def test_false_inequality(self):
        a = CustomList([0, 3, 2, 3, 3])
        b = CustomList([0, 3, 2, 3, 3])
        self.assertFalse(a != b)

    def test_less_than_or_equal(self):
        a = CustomList([0, 3, 2, 3, 3])
        b = CustomList([0, 3, 1, 3, 3])
        self.assertTrue(b <= a)

    def test_equal_case(self):
        a = CustomList([0, 3, 2, 3, 3])
        b = CustomList([0, 3, 2, 3, 3])
        self.assertTrue(b <= a)

    def test_false_less_than_or_equal(self):
        a = CustomList([0, 3, 2, 3, 3])
        b = CustomList([0, 3, 4, 3, 3])
        self.assertFalse(b <= a)

    def test_greater_than_or_equal(self):
        a = CustomList([0, 3, 2, 3, 3])
        b = CustomList([0, 3, 3, 3, 3])
        self.assertTrue(b >= a)

    def test_greater_equal_case(self):
        a = CustomList([0, 3, 2, 3, 3])
        b = CustomList([0, 3, 2, 3, 3])
        self.assertTrue(b >= a)

    def test_greater_less_than_or_equal(self):
        a = CustomList([0, 3, 2, 3, 3])
        b = CustomList([0, 3, 1, 3, 3])
        self.assertFalse(b >= a)

    def test_string_representation(self):
        a = CustomList([0, 3, 2, 3, 3])
        expected = 'CustomList = [0, 3, 2, 3, 3], sum = 11'
        self.assertEqual(str(a), expected)

    def test_nulls_string_representation(self):
        a = CustomList([0, 0, 0, 0, 0, 0])
        expected = 'CustomList = [0, 0, 0, 0, 0, 0], sum = 0'
        self.assertEqual(str(a), expected)

    def test_none(self):
        a = CustomList([None])
        b = CustomList([None])
        with self.assertRaises(TypeError):
            a+b
