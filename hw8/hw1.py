"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.

from enum import Enum


class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"


class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"


Should become:

class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""


"""
This code defines two classes, ColorsEnum and SizesEnum, which are enums and contain a set of values.
"""


class SimplifiedEnum(type):
    def __new__(cls, name, bases, attrs):
        values = attrs.pop('_SimplifiedEnum__keys')
        obj = super().__new__(cls, name, bases, attrs)
        for i, value in enumerate(values):
            if isinstance(value, tuple):
                value, alias = value
            else:
                alias = value
            enum_value = obj(value, alias)
            setattr(obj, value, enum_value)
            setattr(obj, alias, enum_value)
        return obj


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")
