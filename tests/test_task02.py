import pytest
from collections.abc import Sequence
from task02 import check_fibonacci


@pytest.mark.parametrize("data, expected", [
    ([1, 1, 2, 3, 5, 8], True),
    ([1, 2, 3, 4, 5], False),
    ([0, 1, 1, 2, 3, 5], True),
    ([1, 1, 3, 4, 7, 11], False),
    ([1, 1, 2, 4, 8, 16], False),
    ([1, 1, 2, 3, 5, 7], False),
    ([1, 2, 3], True),
    ([1, 2], False),
    ([1], False),
    ([], False)
])
def test_check_fibonacci(data: Sequence[int], expected: bool):
    assert check_fibonacci(data) == expected