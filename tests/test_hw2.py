import pytest
from hw2 import major_and_minor_elem


"""
@pytest.mark.parametrize decorator to define multiple inputs and expected results. Each input is represented as a tuple
(inp, expected) , where inp is a list and expected is the expected result of the major_and_minor_elem
function on that list.
"""


@pytest.mark.parametrize("inp, expected", [
    ([1, 2, 3, 4, 5, 5, 5, 5], (5, 1)),
    ([1, 2, 3, 4, 5], (1, 5)),
    ([1, 1, 1, 1, 1], (1, 1)),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], (1, 9)),
    ([], (None, None)),
    ([1], (1, 1)),
    ([1, 1, 2, 2, 3, 3], (1, 3)),
    (["a", "b", "c", "c", "c", "d", "d", "d", "d", "d"], ("d", "a")),
    (["a", "a", "a", "b", "b", "c", "c", "c", "c", "c"], ("c", "b")),
])
def test_major_and_minor_elem(inp, expected):
    assert major_and_minor_elem(inp) == expected