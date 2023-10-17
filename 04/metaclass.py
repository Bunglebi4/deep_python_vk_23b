class CustomMeta(type):
    def __new__(cls, name, bases, dct):
        custom_dct = {}
        for attr_name, attr_value in dct.items():
            if not (attr_name.startswith('__') or attr_name.endswith('__')):
                custom_attr_name = f'custom_{attr_name}'
            else:
                custom_attr_name = attr_name
            custom_dct[custom_attr_name] = attr_value
        custom_dct["__setattr__"] = cls.__setattr__
        return super().__new__(cls, name, bases, custom_dct)

    def __setattr__(self, name, value):
        if name.startswith('custom_'):
            super().__setattr__(name, value)
        else:
            self.__dict__[f"custom_{name}"] = value


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"


inst = CustomClass()
inst.aboba = 50
print(CustomClass.__dict__)
assert CustomClass.custom_x == 50
assert inst.custom_x == 50
assert inst.custom_val == 99
assert inst.custom_line() == 100
assert str(inst) == "Custom_by_metaclass"

try:
    CustomClass.x
except AttributeError:
    pass

try:
    inst.x
except AttributeError:
    pass

try:
    inst.val
except AttributeError:
    pass

try:
    inst.line()
except AttributeError:
    pass

try:
    inst.yyy
except AttributeError:
    pass

inst.dynamic = "added later"
assert inst.custom_dynamic == "added later"

# Попытка обращения к атрибутам и методам без префикса "custom_"
try:
    inst.dynamic
except AttributeError:
    pass
