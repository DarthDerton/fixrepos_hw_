import pytest
from hw1 import find_occurrences

"""
In this test, we define a pytest.mark.parametrize decorator with three parameters: tree, element, and expected_count.
We then define several test cases, each of which is a tuple with three values:
a tree, an element, and the expected number of occurrences of the element in the tree.
In each test case, we call the find_occurrences function with the given tree and element,
and check that the result is equal to the expected number of occurrences of the element in the tree.
"""


@pytest.mark.parametrize("tree, element, expected_count", [
    ({'a': 'RED', 'b': 'GREEN', 'c': 'BLUE'}, 'RED', 1),
    ({'a': 'RED', 'b': ['RED', 'GREEN'], 'c': {'d': 'RED'}}, 'RED', 3),
    ({'a': 'RED', 'b': ['RED', 'GREEN'], 'c': {'d': 'RED'}}, 'GREEN', 1),
    ({'a': 'RED', 'b': ['RED', 'GREEN'], 'c': {'d': 'RED'}}, 'YELLOW', 0),
])
def test_find_occurrences(tree, element, expected_count):
    assert find_occurrences(tree, element) == expected_count