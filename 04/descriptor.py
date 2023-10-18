class Price:
    def __init__(self):
        self.name = None

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)) or value <= 0:
            print(value)
            raise ValueError("Цена должна быть больше нуля")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class BookName:
    def __init__(self):
        self.name = None

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, str) or len(value) > 36:
            raise ValueError("Значение должно быть строкой короче 37 символов")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Genres:
    valid_genres = ["Programming", "Non-Fiction", "Science Fiction", "Chess"]
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value not in self.valid_genres:
            raise ValueError("Invalid book genre")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class NewBook:
    price = Price()
    name = BookName()
    genres = Genres()

    def __init__(self, name, price, genres):
        self.price = price
        self.name = name
        self.genres = genres
