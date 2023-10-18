class Mark:
    def __init__(self):
        self.name = None

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int) or value <= 0 or value >= 6:
            print(value)
            raise ValueError("Оценка должна быть целым числом в диапазоне от 1 до 5")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Name:
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


class CurriculumDescriptor:
    def __init__(self, *valid_courses):
        self.name = None
        self.valid_courses = valid_courses

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not all(course in self.valid_courses for course in value):
            invalid_courses = [course for course in value if course not in self.valid_courses]
            raise ValueError(f"Недопустимые курсы: {', '.join(invalid_courses)}")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Student:
    marks = Mark()
    name = Name()
    curriculum = CurriculumDescriptor("Математика", "История", "Физика")

    def __init__(self, name, marks, curriculum):
        self.marks = marks
        self.name = name
        self.curriculum = curriculum
