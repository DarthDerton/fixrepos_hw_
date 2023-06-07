import pytest
from hw1 import ColorsEnum, SizesEnum


"""
These tests verify that all values and aliases specified in __keys have been created in the corresponding enum class.
They also check that the value and alias of each enum element matches the expected values.
"""


@pytest.mark.parametrize("enum_class, expected_values", [
    (ColorsEnum, ["RED", "BLUE", "ORANGE", "BLACK"]),
    (SizesEnum, ["XL", "L", "M", "S", "XS"])
])
def test_enum_values(enum_class, expected_values):
    for value in expected_values:
        assert hasattr(enum_class, value)
        assert getattr(enum_class, value).value == value
        assert getattr(enum_class, value).alias == value


@pytest.mark.parametrize("enum_class, expected_aliases", [
    (ColorsEnum, ["RED", "BLUE", "ORANGE", "BLACK"]),
    (SizesEnum, ["XL", "L", "M", "S", "XS"])
])
def test_enum_aliases(enum_class, expected_aliases):
    for alias in expected_aliases:
        assert hasattr(enum_class, alias)
        assert getattr(enum_class, alias).value == alias
        assert getattr(enum_class, alias).alias == alias