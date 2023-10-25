import unittest
from lru_cache import LRUCache


class TestLruCache(unittest.TestCase):
    def test_key_add(self):
        cache = LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertIs(cache.get("k3"),None)
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")

        cache.set("k3", "val3")

        self.assertEqual(cache.get("k3"), "val3")
        self.assertIs(cache.get("k2"),None)
        self.assertEqual(cache.get("k1"), "val1")

