import json


def parse_json(json_str, keyword_callback, required_fields=None, keywords=None):
    json_doc = json.loads(json_str)
    for key in required_fields:
        if json_doc.get(key):
            for el in keywords:
                if el in json_doc.get(key):
                    keyword_callback(el)


def keyword1_callback(el):
    print(f"i did it for {el}")


with open("test_files_for_json_parser/good_input.json", encoding='utf-8') as fl:
    json_str = fl.read()
parse_json(json_str, keyword1_callback, required_fields=["name"], keywords=["Иполлит"])
