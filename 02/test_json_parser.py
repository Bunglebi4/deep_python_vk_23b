import unittest
from json import JSONDecodeError
from unittest.mock import patch, MagicMock
from json_parser import parse_json


class TestJsonParser(unittest.TestCase):
    def test_parsing(self):
        keyword_callback = MagicMock()
        parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}', keyword_callback, required_fields=["key1"],
                   keywords=["word2"])
        self.assertEqual(keyword_callback.call_count, 1)

    def test_parsing_with_no_callback(self):
        keyword_callback = MagicMock()
        parse_json('{"key1": "Word1", "key2": "word2 word3"}', keyword_callback, required_fields=["key1"],
                   keywords=["word2"])
        self.assertEqual(keyword_callback.call_count, 0)

    def test_parsing_with_no_keys(self):
        keyword_callback = MagicMock()
        parse_json('{"key1": "Word1", "key2": "word2 word3"}', keyword_callback, required_fields=["key8"],
                   keywords=["word2"])
        self.assertEqual(keyword_callback.call_count, 0)

    def test_parsing_with_bad_input(self):
        keyword_callback = MagicMock()
        with self.assertRaises(JSONDecodeError):
            parse_json('{1: "Word1", "key2": "word2 word3"}', keyword_callback, required_fields=["key8"],
                       keywords=["word2"])

    def test_parsing_with_no_fields(self):
        keyword_callback = MagicMock()
        parse_json('{"key1": "Word1", "key2": "word2 word3"}', keyword_callback, required_fields=["key8"],
                   keywords=["word100"])
        self.assertEqual(keyword_callback.call_count, 0)

    def test_parsing_with_empty_args(self):
        keyword_callback = MagicMock()
        parse_json('{"key1": "Word1", "key2": "word2 word3"}', keyword_callback, required_fields=[],
                   keywords=[])
        self.assertEqual(keyword_callback.call_count, 0)

    def test_parsing_with_two_words_in_fields(self):
        keyword_callback = MagicMock()
        parse_json('{"key1": "Word1", "key2": "word2 word3"}', keyword_callback, required_fields=[],
                   keywords=[])
        self.assertEqual(keyword_callback.call_count, 0)

    def test_parse_json_with_empty_required_fields(self):
        json_str = '{"field1": "value1", "field2": "value2", "field3": "keyword1" }'

        def keyword_callback(keyword):
            self.fail("Keyword callback should not be called if required fields are empty")

        parse_json(json_str, keyword_callback, required_fields=[], keywords=["keyword1", "keyword2"])
