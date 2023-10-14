import io
from typing import Any


def find_intersection(set_of_words: set, line: str) -> set[Any]:
    return set(map(lambda x: x.lower(), line.split())) & set_of_words


def find_good_strings(file, list_of_words):
    set_of_words = set(map(lambda x: x.lower(), list_of_words))
    if not isinstance(file, (io.TextIOWrapper, str)):
        raise TypeError(
            f"Bad file input, file must be io.TextIOBase, not {type(file)}"
        )
    if isinstance(file, io.TextIOWrapper):
        line_iterator = file
    else:
        line_iterator = open(file, "r", encoding="utf-8")

    with line_iterator:
        line = line_iterator.readline()
        while line:
            if find_intersection(set_of_words, line):
                yield line.strip()
            line = line_iterator.readline()
