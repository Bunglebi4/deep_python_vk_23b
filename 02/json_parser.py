import json


def parse_json(json_str, keyword_callback, required_fields=None, keywords=None):
    json_doc = json.loads(json_str)
    for key in required_fields:
        if json_doc.get(key):
            for el in keywords:
                if el in json_doc.get(key):
                    keyword_callback(el)
