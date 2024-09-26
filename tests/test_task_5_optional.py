import pytest
from typing import List
from task_5_optional import fizzbuzz


"""
In this test, we define parameters n and expected for each test case in the list
using the pytest.mark decorator .parametrize.
"""


@pytest.mark.parametrize("n, expected", [
    (1, ["1"]),
    (2, ["1", "2"]),
    (3, ["1", "2", "fizz"]),
    (4, ["1", "2", "fizz", "4"]),
    (5, ["1", "2", "fizz", "4", "buzz"]),
    (6, ["1", "2", "fizz", "4", "buzz", "fizz"]),
    (7, ["1", "2", "fizz", "4", "buzz", "fizz", "7"]),
    (8, ["1", "2", "fizz", "4", "buzz", "fizz", "7", "8"]),
    (9, ["1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz"]),
    (10, ["1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz"]),
])
def test_fizzbuzz(n: int, expected: List[str]):
    assert list(fizzbuzz(n)) == expected