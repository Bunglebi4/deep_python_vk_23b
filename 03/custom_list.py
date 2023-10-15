class CustomList(list):

    def __add__(self, other):
        if not isinstance(other, (CustomList, list)):
            raise TypeError(f"operation '+'"
                            f" unsupported for {type(other)}")
        result = CustomList()
        if not isinstance(other, CustomList):
            other = CustomList(other)
        max_len = max(len(self), len(other))
        for i in range(max(len(self), len(other))):
            if i <= min(len(self), len(other)) - 1:
                result_elem = self[i] + other[i]
            else:
                if max_len == len(other):
                    result_elem = other[i]
                else:
                    result_elem = self[i]
            result.append(result_elem)
        return CustomList(result)

    def __radd__(self, other):
        if not isinstance(other, (CustomList, list)):
            raise TypeError(f"operation '+'"
                            f" unsupported for {type(other)}")
        result = CustomList()
        if not isinstance(other, CustomList):
            other = CustomList(other)
        max_len = max(len(self), len(other))
        for i in range(max(len(self), len(other))):
            if i <= min(len(self), len(other)) - 1:
                result_elem = self[i] + other[i]
            else:
                if max_len == len(other):
                    result_elem = other[i]
                else:
                    result_elem = self[i]
            result.append(result_elem)
        return CustomList(result)

    def __sub__(self, other):
        if not isinstance(other, (CustomList, list)):
            raise TypeError(f"operation '-'"
                            f" unsupported for {type(other)}")
        result = CustomList()
        if not isinstance(other, CustomList):
            other = CustomList(other)
        max_len = max(len(self), len(other))
        for i in range(max(len(self), len(other))):
            if i <= min(len(self), len(other)) - 1:
                result_elem = self[i] - other[i]
            else:
                if max_len == len(other):
                    result_elem = -other[i]
                else:
                    result_elem = self[i]
            result.append(result_elem)
        return result

    def __rsub__(self, other):
        if not isinstance(other, (CustomList, list)):
            raise TypeError(f"operation '-'"
                            f" unsupported for {type(other)}")
        if not isinstance(other, CustomList):
            other = CustomList(other)
        max_len = max(len(other), len(self))
        result = CustomList()
        for i in range(max(len(other), len(self))):
            if i <= min(len(self), len(other)) - 1:
                result_elem = other[i] - self[i]
            else:
                if max_len == len(self):
                    result_elem = -self[i]
                else:
                    result_elem = other[i]
            result.append(result_elem)
        return result

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        if isinstance(other, CustomList):
            return sum(self) != sum(other)
        raise TypeError(f"operation '!='"
                        f" unsupported for {type(other)}")

    def __le__(self, other):
        if not isinstance(other, CustomList):
            raise TypeError(f"operation '<='"
                            f" unsupported for {type(other)}")
        return sum(self) <= sum(other)

    def __lt__(self, other):
        if not isinstance(other, CustomList):
            raise TypeError(f"operation '<'"
                            f" unsupported for {type(other)}")
        return sum(self) < sum(other)

    def __ge__(self, other):
        if not isinstance(other, CustomList):
            raise TypeError(f"operation '>='"
                            f" unsupported for {type(other)}")
        return sum(self) >= sum(other)

    def __gt__(self, other):
        if not isinstance(other, CustomList):
            raise TypeError(f"operation '>'"
                            f" unsupported for {type(other)}")
        return sum(self) > sum(other)

    def __str__(self):
        return f'CustomList = {list(self)}, sum = {sum(self)}'
