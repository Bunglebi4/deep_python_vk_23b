class CustomMeta(type):
    def __new__(cls, name, bases, dct):
        custom_dct = {}
        for attr_name, attr_value in dct.items():
            if not (attr_name.startswith('__') and attr_name.endswith('__')):
                custom_attr_name = f'custom_{attr_name}'
            else:
                custom_attr_name = attr_name
            custom_dct[custom_attr_name] = attr_value
        custom_dct["__setattr__"] = cls.__setattr__
        return super().__new__(cls, name, bases, custom_dct)

    def __setattr__(self, name, value):
        self.__dict__[f"custom_{name}"] = value
