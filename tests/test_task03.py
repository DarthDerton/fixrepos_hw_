import pytest
from task03 import make_filter, sample_data, Filter


"""
There are a few issues with the code:
1. The __init__ method of the Filter class is misspelled as init.
2. The lambda function in the example usage of the Filter class is misspelled as lamba.
3. The isinstance function in the example usage of the Filter class is used incorrectly.
It should be isinstance(a, int) instead of isinstance(int, a).
4. The keyword_filter_func function in the make_filter function is comparing
the value of the key in the value dictionary to the entire value dictionary,
instead of the value passed in as an argument to the function.
"""


def test_filter_init():
    f = Filter([lambda x: x > 0])
    assert f.functions == [lambda x: x > 0]


def test_filter_apply():
    f = Filter([lambda x: x > 0])
    assert f.apply([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert f.apply([-1, 0, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert f.apply([-1, -2, -3]) == []


def test_make_filter():
    f = make_filter(name='polly', type='bird')
    assert f.functions[0]({'name': 'polly', 'type': 'bird'}) == True
    assert f.functions[0]({'name': 'polly', 'type': 'dog'}) == False
    assert f.functions[0]({'name': 'fido', 'type': 'bird'}) == False
    assert f.functions[0]({'name': 'fido', 'type': 'dog'}) == False
    assert f.functions[1]({'name': 'polly', 'type': 'bird'}) == True
    assert f.functions[1]({'name': 'polly', 'type': 'dog'}) == False
    assert f.functions[1]({'name': 'fido', 'type': 'bird'}) == False
    assert f.functions[1]({'name': 'fido', 'type': 'dog'}) == False
    assert f.apply(sample_data) == [{'is_dead': True, 'kind': 'parrot', 'type': 'bird', 'name': 'polly'}]


@pytest.fixture
def sample_data():
    return [{'name': 'polly', 'type': 'bird', 'kind': 'parrot', 'is_dead': True},
                {'name': 'fido', 'type': 'dog', 'kind': 'bulldog', 'is_dead': False},
                {'name': 'rex', 'type': 'dog', 'kind': 'poodle', 'is_dead': False},
                {'name': 'tweety', 'type': 'bird', 'kind': 'canary', 'is_dead': True}]
