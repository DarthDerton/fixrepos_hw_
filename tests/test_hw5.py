import pytest
from hw5 import custom_range


"""
test_custom_range function that checks that the custom_range function returns the correct range for different arguments.
We also check that the function returns an empty list if the start and end indexes match, and that it throws a
ValueError exception if the stop argument is not in the iterable and TypeError exception
if the iterable is not a sequence.
"""


def test_custom_range():
    """test that the function returns the correct range"""
    assert custom_range([1, 2, 3, 4, 5], 2, 4) == [3, 4]

    """test that the function returns the correct range with a step"""
    assert custom_range([1, 2, 3, 4, 5], 1, 5, 2) == [1, 3, 5]

    """test that the function returns the correct range with a negative step"""
    assert custom_range([1, 2, 3, 4, 5], 5, 1, -2) == [5, 3, 1]

    """test that the function returns the correct range with a single argument"""
    assert custom_range([1, 2, 3, 4, 5], 3) == [1, 2, 3]

    """test that the function returns an empty list if the start and stop indices are the same"""
    assert custom_range([1, 2, 3, 4, 5], 3, 3) == []

    """test that the function returns an empty list if the start index is greater than the stop index"""
    assert custom_range([1, 2, 3, 4, 5], 4, 2) == []

    """test that the function raises a ValueError if the stop argument is not in the iterable"""
    with pytest.raises(ValueError):
        custom_range([1, 2, 3, 4, 5], 2, 6)

    """test that the function raises a ValueError if the start argument is not in the iterable"""
    with pytest.raises(ValueError):
        custom_range([1, 2, 3, 4, 5], 6, 2)

    """test that the function raises a TypeError if the iterable is not a sequence"""
    with pytest.raises(TypeError):
        custom_range(123, 2, 4)