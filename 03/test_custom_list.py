import unittest
from custom_list import CustomList


class TestCustomList(unittest.TestCase):

    def test_addition(self):
        obj_1 = CustomList([0, 3, 2, 3, 3])
        obj_2 = CustomList([0, 3, 1, 3, 3])
        result = obj_1 + obj_2
        expected = CustomList([0, 6, 3, 6, 6])
        self.assertEqual(result, expected)

    def test_addition_with_different_len(self):
        obj_1 = CustomList([0, 3, 2, 3, 3])
        obj_2 = CustomList([0, 3, 1, 3, 3, 0, 1, 2])
        result = obj_1 + obj_2
        expected = CustomList([0, 6, 3, 6, 6, 0, 1, 2])
        self.assertEqual(result, expected)

    def test_addition_with_diff_len_v_2(self):
        obj_1 = CustomList([0, 3, 2, 3, 3, 1, 2])
        obj_2 = CustomList([0, 3, 1, 3, 3])
        result = obj_1 + obj_2
        expected = CustomList([0, 6, 3, 6, 6, 1, 2])
        self.assertEqual(result, expected)

    def test_addition_with_list(self):
        obj_1 = CustomList([0, 3, 2, 3, 3])
        obj_2 = [0, 3, 1, 3, 3]
        result = obj_1 + obj_2
        expected = CustomList([0, 6, 3, 6, 6])
        self.assertEqual(result, expected)

    def test_addition_with_list_with_diff_len(self):
        obj_1 = CustomList([0, 3, 2, 3, 3, 1, 2, 3])
        obj_2 = [0, 3, 1, 3, 3]
        result = obj_1 + obj_2
        expected = CustomList([0, 6, 3, 6, 6, 1, 2, 3])
        self.assertEqual(result, expected)

    def test_addition_with_list_with_diff_len_v2(self):
        obj_1 = CustomList([0, 3, 2, 3, 3])
        obj_2 = [0, 3, 1, 3, 3, 1, 2, 3]
        result = obj_1 + obj_2
        expected = CustomList([0, 6, 3, 6, 6, 1, 2, 3])
        self.assertEqual(result, expected)

    def test_addition_list_with_custom_list(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = [0, 3, 1, 3, 3]
        result = obj2 + obj1
        expected = CustomList([0, 6, 3, 6, 6])
        self.assertEqual(result, expected)

    def test_addition_list_with_custom_with_diff_len(self):
        obj1 = CustomList([0, 3, 2, 3, 3, 1, 2, 3])
        obj2 = [0, 3, 1, 3, 3]
        result = obj2 + obj1
        expected = CustomList([0, 6, 3, 6, 6, 1, 2, 3])
        self.assertEqual(result, expected)

    def test_addition_list_with_custom_with_diff_len2(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = [0, 3, 1, 3, 3, 1, 2, 3]
        result = obj2 + obj1
        expected = CustomList([0, 6, 3, 6, 6, 1, 2, 3])
        print(type(result))
        self.assertEqual(result, expected)

    def test_subtraction(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = CustomList([0, 3, 1, 3, 3])
        result = obj1 - obj2
        expected = CustomList([0, 0, 1, 0, 0])
        self.assertEqual(result, expected)

    def test_subtraction_with_different_len(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = CustomList([0, 3, 1, 3, 3, 0, 1, 2])
        result = obj1 - obj2
        expected = CustomList([0, 0, 1, 0, 0, 0, -1, -2])
        self.assertEqual(result, expected)

    def test_subtraction_with_diff_len_v_2(self):
        obj1 = CustomList([0, 3, 2, 3, 3, 1, 2])
        obj2 = CustomList([0, 3, 1, 3, 3])
        result = obj1 - obj2
        expected = CustomList([0, 0, 1, 0, 0, 0, 1, 2])
        self.assertEqual(result, expected)

    def test_subtraction_with_list(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = [0, 3, 1, 3, 3]
        result = obj1 - obj2
        expected = CustomList([0, 0, 1, 0, 0])
        self.assertEqual(result, expected)

    def test_subtraction_with_list_with_diff_len(self):
        obj1 = CustomList([0, 3, 2, 3, 3, 1, 2, 3])
        obj2 = [0, 3, 1, 3, 3]
        result = obj1 - obj2
        expected = CustomList([0, 0, 1, 0, 0, 1, 2, 3])
        self.assertEqual(result, expected)

    def test_subtraction_with_list_with_diff_len_v2(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = [0, 3, 1, 3, 3, 1, 2, 3]
        result = obj1 - obj2
        expected = CustomList([0, 0, 1, 0, 0, -1, -2, -3])
        self.assertEqual(result, expected)

    def test_subtraction_from_list(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = [0, 3, 1, 3, 3]
        result = obj2 - obj1
        expected = CustomList([0, 0, -1, 0, 0])
        self.assertEqual(result, expected)

    def test_subtraction_from_list_with_diff_len(self):
        obj1 = CustomList([0, 3, 2, 3, 3, 1, 2, 3])
        obj2 = [0, 3, 1, 3, 3]
        result = obj2 - obj1
        expected = CustomList([0, 0, -1, 0, 0, -1, -2, -3])
        self.assertEqual(result, expected)

    def test_subtraction_with_from_with_diff_len_v2(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = [0, 3, 1, 3, 3, 1, 2, 3]
        result = obj2 - obj1
        expected = CustomList([0, 0, -1, 0, 0, 1, 2, 3])
        self.assertEqual(result, expected)

    def test_equality(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = CustomList([0, 3, 2, 3, 3])
        self.assertTrue(obj1 == obj2)

    def test_false_equality(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = CustomList([0, 4, 2, 3, 3])
        self.assertFalse(obj1 == obj2)

    def test_inequality(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = CustomList([0, 3, 1, 3, 3])
        self.assertTrue(obj1 != obj2)

    def test_false_inequality(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = CustomList([0, 3, 2, 3, 3])
        self.assertFalse(obj1 != obj2)

    def test_less_than_or_equal(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = CustomList([0, 3, 1, 3, 3])
        self.assertTrue(obj2 <= obj1)

    def test_equal_case(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = CustomList([0, 3, 2, 3, 3])
        self.assertTrue(obj2 <= obj1)

    def test_false_less_than_or_equal(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = CustomList([0, 3, 4, 3, 3])
        self.assertFalse(obj2 <= obj1)

    def test_greater_than_or_equal(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = CustomList([0, 3, 3, 3, 3])
        self.assertTrue(obj2 >= obj1)

    def test_greater_equal_case(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = CustomList([0, 3, 2, 3, 3])
        self.assertTrue(obj2 >= obj1)

    def test_greater_less_than_or_equal(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = CustomList([0, 3, 1, 3, 3])
        self.assertFalse(obj2 >= obj1)

    def test_string_representation(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        expected = 'CustomList = [0, 3, 2, 3, 3], sum = 11'
        self.assertEqual(str(obj1), expected)

    def test_nulls_string_representation(self):
        obj1 = CustomList([0, 0, 0, 0, 0, 0])
        expected = 'CustomList = [0, 0, 0, 0, 0, 0], sum = 0'
        self.assertEqual(str(obj1), expected)

    def test_none(self):
        obj1 = CustomList([None])
        obj2 = CustomList([None])
        with self.assertRaises(TypeError):
            obj1 + obj2

    def test_type(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = CustomList([0, 3, 1, 3, 3])
        obj3 = [1, 2, 3, 4]
        self.assertIsInstance(obj1 + obj2, CustomList)
        self.assertIsInstance(obj1 - obj2, CustomList)
        self.assertIsInstance(obj1 + obj3, CustomList)
        self.assertIsInstance(obj1 - obj3, CustomList)
        self.assertIsInstance(obj2 + obj1, CustomList)
        self.assertIsInstance(obj2 - obj1, CustomList)

    def test_lt(self):
        obj1 = CustomList([0, 3, 1, 3, 3])
        obj2 = CustomList([0, 3, 2, 3, 3])
        self.assertTrue(obj1 < obj2)

    def test_false_lt(self):
        obj1 = CustomList([0, 3, 3, 3, 3])
        obj2 = CustomList([0, 3, 2, 3, 3])
        self.assertFalse(obj1 < obj2)

    def test_equal_lt(self):
        obj1 = CustomList([0, 3, 3, 3, 3])
        obj2 = CustomList([0, 3, 3, 3, 3])
        self.assertFalse(obj1 < obj2)

    def test_gt(self):
        obj2 = CustomList([0, 3, 1, 3, 3])
        obj1 = CustomList([0, 3, 2, 3, 3])
        self.assertTrue(obj1 > obj2)

    def test_false_gt(self):
        obj2 = CustomList([0, 3, 3, 3, 3])
        obj1 = CustomList([0, 3, 2, 3, 3])
        self.assertFalse(obj1 > obj2)

    def test_equal_gt(self):
        obj2 = CustomList([0, 3, 3, 3, 3])
        obj1 = CustomList([0, 3, 3, 3, 3])
        self.assertFalse(obj1 > obj2)

    def test_original_lists(self):
        obj1 = CustomList([0, 3, 3, 3, 3])
        obj2 = CustomList([0, 3, 2, 3, 3])
        expected_obj1 = CustomList([0, 3, 3, 3, 3])
        expected_obj2 = CustomList([0, 3, 2, 3, 3])
        obj2 + obj1
        obj2 - obj1
        obj1 - obj2
        self.assertEqual(obj1, expected_obj1)
        self.assertEqual(obj2, expected_obj2)

    def test_add_type_error(self):
        obj1 = CustomList([0, 1, 2, 3])
        obj2 = "sodjkfgnsodjfgn"
        with self.assertRaises(TypeError):
            obj1 + obj2

    def test_sub_type_error(self):
        obj1 = CustomList([0, 1, 2, 3])
        obj2 = "sodjkfgnsodjfgn"
        with self.assertRaises(TypeError):
            obj1 - obj2

    def test_rsub_type_error(self):
        obj1 = CustomList([0, 1, 2, 3])
        obj2 = "sodjkfgnsodjfgn"
        with self.assertRaises(TypeError):
            obj2 - obj1

    def test_eq_type_error(self):
        obj1 = CustomList([0, 1, 2, 3])
        obj2 = "sodjkfgnsodjfgn"
        with self.assertRaises(TypeError):
            var = obj1 == obj2

    def test_ne_type_error(self):
        obj1 = CustomList([0, 1, 2, 3])
        obj2 = "sodjkfgnsodjfgn"
        with self.assertRaises(TypeError):
            var = obj1 != obj2

    def test_le_type_error(self):
        obj1 = CustomList([0, 1, 2, 3])
        obj2 = "sodjkfgnsodjfgn"
        with self.assertRaises(TypeError):
            var = obj1 <= obj2

    def test_lt_type_error(self):
        obj1 = CustomList([0, 1, 2, 3])
        obj2 = "sodjkfgnsodjfgn"
        with self.assertRaises(TypeError):
            var = obj1 < obj2

    def test_ge_type_error(self):
        obj1 = CustomList([0, 1, 2, 3])
        obj2 = "sodjkfgnsodjfgn"
        with self.assertRaises(TypeError):
            var = obj1 >= obj2

    def test_gt_type_error(self):
        obj1 = CustomList([0, 1, 2, 3])
        obj2 = "sodjkfgnsodjfgn"
        with self.assertRaises(TypeError):
            var = obj1 > obj2

    def test_radd(self):
        obj1 = CustomList([0, 1, 2, 3])
        obj2 = "sodjkfgnsodjfgn"
        with self.assertRaises(TypeError):
            var = obj2 + obj1
        obj1 = CustomList([0, 1, 2, 3])
        obj2 = [0, -2, 3]
        expected = CustomList([0, -1, 5, 3])
        self.assertIsInstance(obj2 + obj1, CustomList)
        self.assertEqual(obj2 + obj1, expected)

    def test_add_with_negative(self):
        obj1 = CustomList([-1, -2, -3, -5])
        obj2 = [-1, -1, -1]
        expected = CustomList([-2, -3, -4, -5])
        self.assertIsInstance(obj2 + obj1, CustomList)
        self.assertEqual(obj2 + obj1, expected)
        self.assertEqual(obj1 + obj2, expected)
