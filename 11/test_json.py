import timeit
import json

import ujson as ujson

import test_json
import cjson


with open("100mb.json") as f:
    large_json_data  = f
    json_time = timeit.timeit(lambda: json.dumps(large_json_data), number=1000)
    print(f"Time for json: {json_time}")


    ujson_time = timeit.timeit(lambda: ujson.dumps(large_json_data), number=1000)
    print(f"Time for ujson: {ujson_time}")


    cjson_time = timeit.timeit(lambda: cjson.dumps(cjson.loads(json.dumps(large_json_data))), number=1000)
    print(f"Time for cjson: {cjson_time}")
