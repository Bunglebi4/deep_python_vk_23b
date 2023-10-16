import unittest
from json import JSONDecodeError
from unittest.mock import MagicMock, call
from json_parser import parse_json


class TestJsonParser(unittest.TestCase):
    def test_parsing(self):
        keyword_callback = MagicMock()
        parse_json(
            '{"key1": "Word1 word2",'
            '"key2": "word2 word3"}',
            keyword_callback,
            required_fields=["key1"],
            keywords=["word2"])
        keyword_callback.assert_called_with("key1", "word2")

    def test_parsing_with_no_callback(self):
        keyword_callback = MagicMock()
        parse_json(
            '{"key1": "Word1", '
            '"key2": "word2 word3"}',
            keyword_callback,
            required_fields=["key1"],
            keywords=["word2"])
        keyword_callback.assert_not_called()

    def test_parsing_with_no_keys(self):
        keyword_callback = MagicMock()
        parse_json(
            '{"key1": "Word1", '
            '"key2": "word2 word3"}',
            keyword_callback,
            required_fields=["key8"],
            keywords=["word2"])
        keyword_callback.assert_not_called()

    def test_parsing_with_bad_input(self):
        keyword_callback = MagicMock()
        with self.assertRaises(JSONDecodeError):
            parse_json(
                '{1: "Word1", '
                '"key2": "word2 word3"}',
                keyword_callback,
                required_fields=["key8"],
                keywords=["word2"])

    def test_parsing_with_no_fields(self):
        keyword_callback = MagicMock()
        parse_json(
            '{"key1": "Word1", '
            '"key2": "word2 word3"}',
            keyword_callback,
            required_fields=["key8"],
            keywords=["word100"])
        keyword_callback.assert_not_called()

    def test_parsing_with_empty_intersection(self):
        keyword_callback = MagicMock()
        parse_json(
            '{"key1": "Word1",'
            ' "key2": "word2 word3"}',
            keyword_callback,
            required_fields=['aa'],
            keywords=['aa'])
        keyword_callback.assert_not_called()

    def test_parsing_with_two_words_in_fields(self):
        keyword_callback = MagicMock()
        parse_json(
            '{"key1": "Word1", '
            '"key2": "word2 word3"}',
            keyword_callback,
            required_fields=['aa'],
            keywords=['aa'])
        keyword_callback.assert_not_called()

    def test_parsing_multiple_keywords(self):
        keyword_callback = MagicMock()
        parse_json(
            '{"key1": "Word1 word2 word3",'
            '"key2": "word2 word3"}',
            keyword_callback,
            required_fields=["key1"],
            keywords=["word2", "word3"])
        expected_calls = [call("key1", "word2"), call("key1", "word3")]
        keyword_callback.assert_has_calls(expected_calls, any_order=True)

    def test_parsing_required_fields_missing(self):
        keyword_callback = MagicMock()
        parse_json(
            '{"key2": "Word1 word2",'
            '"key3": "word2 word3"}',
            keyword_callback,
            required_fields=["key1"],
            keywords=["word2"])
        keyword_callback.assert_not_called()

    def test_parsing_required_fields_present_but_empty(self):
        keyword_callback = MagicMock()
        parse_json(
            '{"key1": "",'
            '"key2": "word2 word3"}',
            keyword_callback,
            required_fields=["key1"],
            keywords=["word2"])
        keyword_callback.assert_not_called()

    def test_parsing_multiple_required_fields(self):
        keyword_callback = MagicMock()
        parse_json(
            '{"key1": "Word1 word2",'
            '"key2": "word2 word3",'
            '"key3": "word2 word3"}',
            keyword_callback,
            required_fields=["key1", "key3"],
            keywords=["word2"])
        expected_calls = [call("key1", "word2"), call("key3", "word2")]
        keyword_callback.assert_has_calls(expected_calls, any_order=True)

    def test_parsing_with_duplicate_keywords(self):
        keyword_callback = MagicMock()
        parse_json(
            '{"key1": "word2 word2",'
            '"key2": "word2 word3"}',
            keyword_callback,
            required_fields=["key1"],
            keywords=["word2"])
        keyword_callback.assert_called_with("key1", "word2")

    def test_parsing_with_case_insensitive_keywords(self):
        keyword_callback = MagicMock()
        parse_json(
            '{"key1": "Word1 WORD2",'
            '"key2": "word2 word3"}',
            keyword_callback,
            required_fields=["key1"],
            keywords=["word2"])

        keyword_callback.assert_called_with("key1", "word2")

    def test_parsing_with_whitespace_around_keywords(self):
        keyword_callback = MagicMock()
        parse_json(
            '{"key1": " Word1 word2 ",'
            '"key2": "word2 word3 "}',
            keyword_callback,
            required_fields=["key1"],
            keywords=["word2"])
        expected_calls = [call("key1", "word2")]
        keyword_callback.assert_has_calls(expected_calls, any_order=True)

    def test_not_full_word_intersection(self):
        keyword_callback = MagicMock()
        parse_json(
            '{"key1": " Word1 word2 ",'
            '"key2": "word2 word3 "}',
            keyword_callback,
            required_fields=["key1"],
            keywords=["word"])
        keyword_callback.assert_not_called()

    def test_none_required_fields(self):
        def keyword_callback(required_fields, keywords):
            print(required_fields, keywords)
        with self.assertRaises(ValueError):
            parse_json(
                '{"key1": " Word1 word2 ",'
                '"key2": "word2 word3 "}',
                keyword_callback,
                required_fields=None,
                keywords=["word2"])

    def test_none_keywords(self):
        def keyword_callback(required_fields, keywords):
            print(required_fields, keywords)
        with self.assertRaises(ValueError):
            parse_json(
                '{"key1": " Word1 word2 ",'
                '"key2": "word2 word3 "}',
                keyword_callback,
                required_fields=["key1"],
                keywords=None)

    def test_none_keyword_callback(self):
        with self.assertRaises(ValueError):
            parse_json(
                '{"key1": " Word1 word2 ",'
                '"key2": "word2 word3 "}',
                keyword_callback=None,
                required_fields=["key1"],
                keywords=["word2"])
