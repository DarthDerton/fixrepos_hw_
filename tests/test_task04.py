
import pytest
from typing import List
from task04 import check_sum_of_four

"""
@pytest.mark.parametrize decorator to define multiple test cases, each representing a set of inputs
and an expected result.
We then define a test_check_sum_of_four function that takes input and an expected result as parameters and uses
check_sum_of_four function to check that the result is as expected. If the result is not as expected, the test will
fail and pytest will issue an error message.
"""


@pytest.mark.parametrize("a, b, c, d, expected", [
    ([1, 2, 3], [-1, -2, -3], [-3, -2, -1], [1, 2, 3], 18),
    ([0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 81),
    ([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], 0),
    ([-1, -2, -3], [-4, -5, -6], [-7, -8, -9], [-10, -11, -12], 0),
    ([1, 2, 3], [0, 0, 0], [-3, -2, -1], [-1, -2, -3], 6)
])
def test_check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int], expected: int):
    assert check_sum_of_four(a, b, c, d) == expected