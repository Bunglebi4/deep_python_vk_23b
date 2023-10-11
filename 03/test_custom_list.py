import unittest
from custom_list import CustomList


class TestCustomList(unittest.TestCase):

    def test_addition(self):
        obj_1 = CustomList([0, 3, 2, 3, 3])
        obj_2 = CustomList([0, 3, 1, 3, 3])
        result = obj_1 + obj_2
        expected = CustomList([0, 6, 3, 6, 6])
        self.assertEqual(list(result), list(expected))

    def test_addition_longer_first_cust_list(self):
        obj_1 = CustomList([0, 3, 2, 3, 3])
        obj_2 = CustomList([0, 3, 1, 3, 3, 0, 1, 2])
        result = obj_1 + obj_2
        expected = CustomList([0, 6, 3, 6, 6, 0, 1, 2])
        self.assertEqual(list(result), list(expected))

    def test_addition_longer_second_cust_list(self):
        obj_1 = CustomList([0, 3, 2, 3, 3, 1, 2])
        obj_2 = CustomList([0, 3, 1, 3, 3])
        result = obj_1 + obj_2
        expected = CustomList([0, 6, 3, 6, 6, 1, 2])
        self.assertEqual(list(result), list(expected))

    def test_addition_with_list(self):
        obj_1 = CustomList([0, 3, 2, 3, 3])
        obj_2 = [0, 3, 1, 3, 3]
        result = obj_1 + obj_2
        expected = CustomList([0, 6, 3, 6, 6])
        self.assertEqual(list(result), list(expected))

    def test_addition_longer_first_list(self):
        obj_1 = CustomList([0, 3, 2, 3, 3, 1, 2, 3])
        obj_2 = [0, 3, 1, 3, 3]
        result = obj_1 + obj_2
        expected = CustomList([0, 6, 3, 6, 6, 1, 2, 3])
        self.assertEqual(list(result), list(expected))

    def test_addition_longer_second_list(self):
        obj_1 = CustomList([0, 3, 2, 3, 3])
        obj_2 = [0, 3, 1, 3, 3, 1, 2, 3]
        result = obj_1 + obj_2
        expected = CustomList([0, 6, 3, 6, 6, 1, 2, 3])
        self.assertEqual(list(result), list(expected))

    def test_addition_list_with_custom_list(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = [0, 3, 1, 3, 3]
        result = obj2 + obj1
        expected = CustomList([0, 6, 3, 6, 6])
        self.assertEqual(list(result), list(expected))

    def test_addition_list_with_custom_with_longer_frst(self):
        obj1 = CustomList([0, 3, 2, 3, 3, 1, 2, 3])
        obj2 = [0, 3, 1, 3, 3]
        result = obj2 + obj1
        expected = CustomList([0, 6, 3, 6, 6, 1, 2, 3])
        self.assertEqual(list(result), list(expected))

    def test_addition_list_with_custom_with_diff_scnd(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = [0, 3, 1, 3, 3, 1, 2, 3]
        result = obj2 + obj1
        expected = CustomList([0, 6, 3, 6, 6, 1, 2, 3])
        print(type(result))
        self.assertEqual(list(result), list(expected))

    def test_subtraction(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = CustomList([0, 3, 1, 3, 3])
        result = obj1 - obj2
        expected = CustomList([0, 0, 1, 0, 0])
        self.assertEqual(list(result), list(expected))

    def test_subtraction_with_second_longer(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = CustomList([0, 3, 1, 3, 3, 0, 1, 2])
        result = obj1 - obj2
        expected = CustomList([0, 0, 1, 0, 0, 0, -1, -2])
        self.assertEqual(list(result), list(expected))

    def test_subtraction_with_first_longer(self):
        obj1 = CustomList([0, 3, 2, 3, 3, 1, 2])
        obj2 = CustomList([0, 3, 1, 3, 3])
        result = obj1 - obj2
        expected = CustomList([0, 0, 1, 0, 0, 1, 2])
        self.assertEqual(list(result), list(expected))

    def test_subtraction_with_list(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = [0, 3, 1, 3, 3]
        result = obj1 - obj2
        expected = CustomList([0, 0, 1, 0, 0])
        self.assertEqual(list(result), list(expected))

    def test_subtraction_with_list_with_first_longer(self):
        obj1 = CustomList([0, 3, 2, 3, 3, 1, 2, 3])
        obj2 = [0, 3, 1, 3, 3]
        result = obj1 - obj2
        expected = CustomList([0, 0, 1, 0, 0, 1, 2, 3])
        self.assertEqual(list(result), list(expected))

    def test_subtraction_with_list_with_second_longer(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = [0, 3, 1, 3, 3, 1, 2, 3]
        result = obj1 - obj2
        expected = CustomList([0, 0, 1, 0, 0, -1, -2, -3])
        self.assertEqual(list(result), list(expected))

    def test_subtraction_from_list(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = [0, 3, 1, 3, 3]
        result = obj2 - obj1
        expected = CustomList([0, 0, -1, 0, 0])
        self.assertEqual(list(result), list(expected))

    def test_subtraction_from_list_with_first_longer(self):
        obj1 = CustomList([0, 3, 2, 3, 3, 1, 2, 3])
        obj2 = [0, 3, 1, 3, 3]
        result = obj2 - obj1
        expected = CustomList([0, 0, -1, 0, 0, -1, -2, -3])
        self.assertEqual(list(result), list(expected))

    def test_subtraction_with_from_with_second_longer(self):
        obj1 = CustomList([0, 3, 2, 3, 3])
        obj2 = [0, 3, 1, 3, 3, 1, 2, 3]
        result = obj2 - obj1
        expected = CustomList([0, 0, -1, 0, 0, 1, 2, 3])
        self.assertEqual(list(result), list(expected))

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
            return obj1 + obj2

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
        obj1 = CustomList([0, 23, -100, 3, 3])
        obj2 = CustomList([0, 3, 2, 3, 3])
        self.assertTrue(obj1 < obj2)

    def test_false_lt(self):
        obj1 = CustomList([0, 7, 3, 9, 3])
        obj2 = CustomList([0, 3, 2, 3, 3])
        self.assertFalse(obj1 < obj2)

    def test_equal_lt(self):
        obj1 = CustomList([0, 9, 0, 0, 3])
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
        var = obj2 + obj1
        var2 = obj2 - obj1
        var3 = obj1 - obj2
        self.assertEqual(list(obj1), list(expected_obj1))
        self.assertEqual(list(obj2), list(expected_obj2))
        return var, var2, var3

    def test_add_type_error(self):
        obj1 = CustomList([0, 1, 2, 3])
        obj2 = "sodjkfgnsodjfgn"
        with self.assertRaises(TypeError):
            var = obj1 + obj2
            return var

    def test_sub_type_error(self):
        obj1 = CustomList([0, 1, 2, 3])
        obj2 = "sodjkfgnsodjfgn"
        with self.assertRaises(TypeError):
            var = obj1 - obj2
            return var

    def test_rsub_type_error(self):
        obj1 = CustomList([0, 1, 2, 3])
        obj2 = "sodjkfgnsodjfgn"
        with self.assertRaises(TypeError):
            var = obj2 - obj1
            return var

    def test_ne_type_error(self):
        obj1 = CustomList([0, 1, 2, 3])
        obj2 = "sodjkfgnsodjfgn"
        with self.assertRaises(TypeError):
            var = obj1 != obj2
            return var

    def test_le_type_error(self):
        obj1 = CustomList([0, 1, 2, 3])
        obj2 = "sodjkfgnsodjfgn"
        with self.assertRaises(TypeError):
            var = obj1 <= obj2
            return var

    def test_lt_type_error(self):
        obj1 = CustomList([0, 1, 2, 3])
        obj2 = "sodjkfgnsodjfgn"
        with self.assertRaises(TypeError):
            var = obj1 < obj2
            return var

    def test_ge_type_error(self):
        obj1 = CustomList([0, 1, 2, 3])
        obj2 = "sodjkfgnsodjfgn"
        with self.assertRaises(TypeError):
            var = obj1 >= obj2
            return var

    def test_gt_type_error(self):
        obj1 = CustomList([0, 1, 2, 3])
        obj2 = "sodjkfgnsodjfgn"
        with self.assertRaises(TypeError):
            var = obj1 > obj2
            return var

    def test_radd(self):
        obj1 = CustomList([0, 1, 2, 3])
        obj2 = "sodjkfgnsodjfgn"
        with self.assertRaises(TypeError):
            var = obj2 + obj1
            return var

        obj1 = CustomList([0, 1, 2, 3])
        obj2 = [0, -2, 3]
        expected = CustomList([0, -1, 5, 3])
        self.assertIsInstance(obj2 + obj1, CustomList)
        self.assertEqual(list(obj2 + obj1), list(expected))

    def test_add_with_negative(self):
        obj1 = CustomList([-1, -2, -3, -5])
        obj2 = [-1, -1, -1]
        expected = CustomList([-2, -3, -4, -5])
        self.assertIsInstance(obj2 + obj1, CustomList)
        self.assertEqual(list(obj2 + obj1), list(expected))
        self.assertEqual(list(obj1 + obj2), list(expected))

    def test_add_empty_list(self):
        self.assertEqual(
            list(CustomList([]) + []),
            []
        )

    def test_sub_empty_list(self):
        self.assertEqual(
            list(CustomList([]) - []),
            []
        )

    def test_empty_list_str(self):
        obj = CustomList([])
        self.assertEqual(str(obj), 'CustomList = [], sum = 0')
