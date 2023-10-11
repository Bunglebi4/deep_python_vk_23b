import io
from typing import Any


def find_intersection(set_of_words: set, line: str) -> set[Any]:
    return set(map(lambda x: x.lower(), line.split())) & set_of_words


def find_good_strings(file, list_of_words):
    set_of_words = set(map(lambda x: x.lower(), list_of_words))
    if isinstance(file, io.TextIOWrapper):
        line = file.readline()
        while line:
            if find_intersection(set_of_words, line):
                yield line.strip()
            line = file.readline()

    elif isinstance(file, str):

        with open(file, "r", encoding="utf-8") as file_lst:
            line = file_lst.readline()
            while line:
                if find_intersection(set_of_words, line):
                    yield line.strip()
                line = file_lst.readline()

    else:
        raise TypeError(
            f"Bad file input, file must be io.TextIOBase, not {type(file)}"
        )
