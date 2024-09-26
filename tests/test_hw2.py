import pytest
from hw2 import backspace_compare


"""
in this test, we define a pytest.mark.parametrize decorator with three parameters: first, second, and expected_result.
We then define several test cases, each of which is a tuple with three values: the first row, the second row,
and the expected result of the comparison. In each test case, we call the backspace_compare function with the given
strings and check that the result is equal to the expected result of the comparison.
"""


@pytest.mark.parametrize("first, second, expected_result", [
    ("ab#c", "ad#c", True),
    ("a##c", "#a#c", True),
    ("a#c", "b", False),
    ("", "", True),
    ("a", "a#", True),
    ("a", "b", False),
    ("a#", "b#", True),
    ("a#b", "c#d", False),
])
def test_backspace_compare(first, second, expected_result):
    assert backspace_compare(first, second) == expected_result