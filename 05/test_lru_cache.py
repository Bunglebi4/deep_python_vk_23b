import unittest
from lru_cache import LRUCache


class TestLruCache(unittest.TestCase):
    def test_key_add(self):
        cache = LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertIs(cache.get("k3"), None)
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")

        cache.set("k3", "val3")

        self.assertEqual(cache.get("k3"), "val3")
        self.assertIs(cache.get("k2"), None)
        self.assertEqual(cache.get("k1"), "val1")

    def test_cache_with_get_operations(self):
        cache = LRUCache(2)
        for key in range(5):
            cache.set(f"{key}", key * 2)
            cache.get(f"{key % 2}")
        self.assertEqual(cache.get("0"), None)
        self.assertEqual(cache.get("1"), None)
        self.assertEqual(cache.get("2"), None)
        self.assertEqual(cache.get("3"), 6)
        self.assertEqual(cache.get("4"), 8)

    def test_cache_for_factorial(self):
        cache = LRUCache(5)

        def factorial_with_cache(num, cache):
            if cache.get(num) is not None:
                return cache.get(num)
            if num in {0, 1}:
                result = 1
            else:
                result = num * factorial_with_cache(num - 1, cache)
            cache.set(num, result)
            return result

        self.assertEqual(factorial_with_cache(5, cache), 120)
        self.assertEqual(factorial_with_cache(5, cache), 120)
        self.assertEqual(factorial_with_cache(2, cache), 2)
        self.assertEqual(factorial_with_cache(4, cache), 24)
        self.assertEqual(factorial_with_cache(5, cache), 120)
        self.assertEqual(factorial_with_cache(5, cache), 120)
