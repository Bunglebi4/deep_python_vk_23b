import json


def parse_json(json_s, keyword_callback, required_fields=None, keywords=None):
    if not (required_fields and keywords and keyword_callback):
        raise ValueError("can't find none in json, sorry:-(")
    json_doc = json.loads(json_s)
    for key in required_fields:
        if json_doc.get(key):
            for word in keywords:
                if word.lower() in list(map(lambda x: x.lower(),
                                            json_doc.get(key).split())):
                    keyword_callback(key, word)
