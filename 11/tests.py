import json
import unittest
from cjson import loads, dumps


class TestCJson(unittest.TestCase):
    def test_loads_dumps(self):
        json_str = open("100mb.json")
        expected_dict = json.load(json_str)

        result_dict = loads(json_str)
        self.assertEqual(result_dict, expected_dict)

        result_str = dumps(expected_dict)
        self.assertEqual(result_str, json_str)


if __name__ == "__main__":
    unittest.main()
