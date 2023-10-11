import json


def parse_json(json_s, keyword_callback, required_fields=None, keywords=None):
    json_doc = json.loads(json_s)
    for key in required_fields:
        if json_doc.get(key):
            for word in keywords:
                if word == json_doc.get(key):
                    keyword_callback(word)
