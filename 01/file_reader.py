import io
from typing import Union, Any


class LineFinder:
    def __init__(self, file, list_of_words: list):
        self.set_of_words = set(map(lambda x: x.lower(), list_of_words))
        if isinstance(file, io.TextIOWrapper):
            lines = []
            for line in file:
                lines.append(line)
            self.file_string = lines

        elif isinstance(file, str):
            lines = []
            with open(file, "r", encoding="utf-8") as f:
                for line in f:
                    lines.append(line)
                self.file_string = lines

        else:
            raise TypeError(f"Bad file input, file must be io.TextIOBase, not {type(file)}")

    @staticmethod
    def find_intersection(set_of_words: set, line: str) -> set[Any]:
        return set(map(lambda x: x.lower(), line.split())) & set_of_words

    def find_good_strings(self):

        for line in self.file_string:
            if self.find_intersection(self.set_of_words, line):
                yield line.strip()


with open("test_files_for_file_reader/good_file.txt", encoding='utf-8') as f:
    print(type(f))
    print(*list(LineFinder(f, ["Роза"]).find_good_strings()))


# file_name = "test_files_for_file_reader/good_file.txt"
# print(*list(LineFinder(file_name, ["Роза", "Яблоко"]).find_good_strings()))


# print(LineFinder.find_intersection({"роза", "яблоко"},
#             "роза упала на лапу Азора Яблоко груша апельсин"))