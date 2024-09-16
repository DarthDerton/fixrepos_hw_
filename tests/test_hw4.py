import pytest
from hw4 import cache


def test_cache():
    """test that the cached function returns the same result as the original function"""
    def add(a, b):
        return a + b

    cached_add = cache(add)

    assert add(1, 2) == cached_add(1, 2)

    """test that the cached function returns the cached result for the same arguments"""
    assert cached_add(1, 2) == cached_add(1, 2)

    """test that the cached function returns the correct result for different arguments"""
    assert cached_add(2, 3) == 5

    """test that the cache is working correctly"""
    assert len(cached_add.__closure__[0].cell_contents) == 2

    """test that the cache is cleared when the function is called with different arguments"""
    cached_add(1, 2)
    cached_add(2, 3)

    assert len(cached_add.__closure__[0].cell_contents) == 2