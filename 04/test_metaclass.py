import unittest
from metaclass import CustomMeta


class TestCustomMeta(unittest.TestCase):
    class CustomClass(metaclass=CustomMeta):
        x = 50

        def __init__(self, val=99):
            self.val = val

        def line(self):
            return 100

        def __str__(self):
            return "Custom_by_metaclass"

    def test_customizing_fields(self):
        inst = self.CustomClass()
        self.assertEqual(inst.custom_x, 50)
        self.assertEqual(inst.custom_val, 99)
        self.assertEqual(inst.custom_line(), 100)
        self.assertEqual(self.CustomClass.custom_x, 50)
        self.assertEqual(str(inst), "Custom_by_metaclass")

    def test_original_fields(self):
        inst = self.CustomClass()
        with self.assertRaises(AttributeError):
            return inst.x
        with self.assertRaises(AttributeError):
            return inst.val
        with self.assertRaises(AttributeError):
            return inst.line()
        with self.assertRaises(AttributeError):
            return inst.yyy
        with self.assertRaises(AttributeError):
            return self.CustomClass.x

    def test_dynamic_attrs(self):
        inst = self.CustomClass()
        inst.dynamic = "added later"
        self.assertEqual(inst.custom_dynamic, "added later")
        self.assertTrue("custom_dynamic" in inst.__dict__ and
                        "dynamic" not in inst.__dict__)

    def test_set_custom_attribute_in_constructor(self):
        obj = self.CustomClass(val=42)
        self.assertEqual(obj.custom_val, 42)

    def test_custom_names(self):
        class CustomClass(metaclass=CustomMeta):
            def custom_method(self):
                return "Custom Method"

        self.assertTrue(hasattr(CustomClass, 'custom_custom_method'))

    def test_changing_attrs(self):
        obj = self.CustomClass(42)
        obj.attribute = 'test'
        original_value = obj.custom_attribute
        obj.custom_attribute = 'new_test'
        self.assertNotEquals(original_value, obj.custom_attribute)
        self.assertEqual('new_test', obj.custom_attribute)

    def test_private_attrs(self):
        class Biba(metaclass=CustomMeta):
            def __init__(self, value):
                self._value = value

        self.assertTrue("custom__value" in Biba(12).__dict__)

    def test_custom_method(self):
        class Buba(metaclass=CustomMeta):
            def real_method(self):
                print("i'll be custom")

            def second_useless_method(self):
                print('dont look at me im useless')

        self.assertTrue(hasattr(Buba(), "custom_real_method"))

    def test_private_custom_method(self):
        class Buba(metaclass=CustomMeta):
            def _real_method(self):
                print("i'll be custom")

            def second_useless_method(self):
                print('dont look at me im useless')

        self.assertTrue(hasattr(Buba(), "custom__real_method"))

    def test_protected_custom_method(self):
        class Buba(metaclass=CustomMeta):
            def __real_method(self):
                print("i'll be custom")

            def second_useless_method(self):
                print('dont look at me im useless')

        self.assertTrue(hasattr(Buba(), "custom__Buba__real_method"))

    def test_protected_attr(self):
        class Buba(metaclass=CustomMeta):
            def __init__(self, x_obj):
                self.__x_obj = x_obj
        self.assertTrue(hasattr(Buba(12), "custom__Buba__x_obj"))
