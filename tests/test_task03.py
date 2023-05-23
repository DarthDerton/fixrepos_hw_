import pytest
from typing import Tuple
from task03 import find_maximum_and_minimum


@pytest.mark.parametrize("filename, expected", [
    ("test1.txt", (1.0, 10.0)),
    ("test2.txt", (-5.0, 5.0)),
    ("test3.txt", (0.0, 0.0)),
    ("test4.txt", (1.0, 1.0)),
    ("test5.txt", (-10.0, 10.0))
])
def test_find_maximum_and_minimum(filename: str, expected: Tuple[float, float]):
    result = find_maximum_and_minimum(filename)
    assert result == expected