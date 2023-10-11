class CustomList(list):
    def __add__(self, other):
        result = CustomList()
        if not isinstance(other, CustomList):
            other = CustomList(other)
        max_len = max(len(self), len(other))
        for i in range(max(len(self), len(other))):
            result_elem = self[i] + other[i] if\
                i <= min(len(self), len(other)) - 1 else (
                other[i] if max_len == len(other) else self[i])
            result.append(result_elem)
        return result

    def __sub__(self, other):
        result = CustomList()
        if not isinstance(other, CustomList):
            other = CustomList(other)
        max_len = max(len(self), len(other))
        for i in range(max(len(self), len(other))):
            result_elem = self[i] - other[i] if \
                i <= min(len(self), len(other)) - 1 else (
                -other[i] if max_len == len(other) else self[i])
            result.append(result_elem)
        return result

    def __rsub__(self, other):
        if not isinstance(other, CustomList):
            other = CustomList(other)
        max_len = max(len(other), len(self))
        result = CustomList()
        for i in range(max(len(other), len(self))):
            result_elem = other[i] - self[i] if\
                i <= min(len(other), len(self)) - 1 else (
                -self[i] if max_len == len(self) else other[i])
            result.append(result_elem)
        return result

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __str__(self):
        return f'CustomList = {list(self)}, sum = {sum(self)}'
