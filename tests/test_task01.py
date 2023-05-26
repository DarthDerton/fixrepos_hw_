import pytest
from functools import wraps
from typing import Callable
from task01 import cache


@pytest.mark.parametrize("args, expected", [
    ((1, 2), 3),
    ((2, 3), 5),
    ((3, 4), 7),
    ((4, 5), 9),
    ((5, 6), 11),
    ((6, 7), 13),
    ((7, 8), 15),
    ((8, 9), 17),
    ((9, 10), 19),
])
def test_cache(args, expected):
    @cache(2)
    def add(x, y):
        return x + y

    assert add(*args) == expected