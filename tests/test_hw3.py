import pytest
from typing import List, Any
from hw3 import combinations


"""
@pytest.mark.parametrize decorator to define multiple test cases for the combinations function. Each test case is
a two-tuple: the list of arguments for the function and the expected result. We then define a test_combinations
function that takes these arguments and checks that the result of the function matches the expected result.
If the results do not match, the test has failed.
"""


@pytest.mark.parametrize(
    "args, expected_output",
    [
        ([], []),
        ([[1, 2], [3, 4]], [[1, 3], [1, 4], [2, 3], [2, 4]]),
        ([[1, 2, 3], [4, 5], [6]], [[1, 4, 6], [1, 5, 6], [2, 4, 6], [2, 5, 6], [3, 4, 6], [3, 5, 6]]),
        ([[1, 2], [], [3, 4]], []),
        ([[1, 2], [3, 4], [5, 6]], [[1, 3, 5], [1, 3, 6], [1, 4, 5], [1, 4, 6], [2, 3, 5], [2, 3, 6], [2, 4, 5], [2, 4, 6]])
    ]
)
def test_combinations(args: List[List[Any]], expected_output: List[List[Any]]):
    assert combinations(*args) == expected_output