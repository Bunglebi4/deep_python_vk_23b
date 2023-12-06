.PHONY: all clean test

all: venv cjsonmodule.so

venv:
python3 -m venv venv
. venv/bin/activate && pip install -r requirements.txt

cjsonmodule.so: cjson.c
. venv/bin/activate && python setup.py install

test: all
. venv/bin/activate && python tests.py

clean:
rm -rf venv build dist cjson.cpython-*.so
