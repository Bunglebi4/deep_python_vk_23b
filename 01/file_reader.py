import io
from typing import Any


class LineFinder:
    def __init__(self, file, list_of_words: list):
        self.set_of_words = set(map(lambda x: x.lower(), list_of_words))
        if isinstance(file, io.TextIOWrapper):
            lines = []
            for line in file:
                lines.append(line)
            self.file_list = lines

        elif isinstance(file, str):
            lines = []
            with open(file, "r", encoding="utf-8") as file_lst:
                for line in file_lst:
                    lines.append(line)
                self.file_list = lines

        else:
            raise TypeError(
                f"Bad file input, file must be io.TextIOBase, not {type(file)}"
            )

    @staticmethod
    def find_intersection(set_of_words: set, line: str) -> set[Any]:
        return set(map(lambda x: x.lower(), line.split())) & set_of_words

    def find_good_strings(self):
        for line in self.file_list:
            if self.find_intersection(self.set_of_words, line):
                yield line.strip()
