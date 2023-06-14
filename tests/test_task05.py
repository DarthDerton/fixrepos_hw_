import pytest
from typing import List
from task05 import find_maximal_subarray_sum


"""
@pytest.mark.parametrize decorator to define multiple test cases, each representing a set of inputs and
an expected result.
We then define a function test_find_maximal_subarray_sum , which takes an input and an expected result as parameters,
and uses find_maximal_subarray_sum function to check that the result is as expected. If the result is not as expected,
the test will fail and pytest will issue an error message.
"""


@pytest.mark.parametrize("nums, k, expected", [
    ([1, 2, 3, 4, 5], 2, 9),
    ([1, -2, 3, 4, -5], 2, 7),
    ([1, -2, 3, 4, -5], 3, 8),
    ([1, -2, 3, 4, -5], 4, 6),
    ([1, -2, 3, 4, -5], 5, 1)
])
def test_find_maximal_subarray_sum(nums: List[int], k: int, expected: int):
    assert find_maximal_subarray_sum(nums, k) == expected