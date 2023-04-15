from functools import wraps
from typing import Callable
"""In previous homework task 4, you wrote a cache function that remembers other function output value.
Modify it to be a parametrized decorator, so that the following code::

    @cache(times=3)
    def some_function():
        pass


Would give out cached value up to `times` number only.
Example::

    @cache(times=2)
    def f():
        return input('? ')   # careful with input() in python2, use raw_input() instead

    >>> f()
    ? 1
    '1'
    >>> f()     # will remember previous value
    '1'
    >>> f()     # but use it up to two times only
    '1'
    >>> f()
    ? 2
    '2'
"""

"""
The cached_func function calls to see if the result
of calling func with the passed arguments is already
in the cache_dict dictionary. If the number of
results is already in the cache and the result has not
yet reached the value of times, then it is increased
by 1 and the result is returned from the cache_dict dictionary.
The number of results that have not yet been computed or reached
has reached the value of times, then the func function with
the passed arguments is raised, the result is in the cache_dict dictionary,
 and the cached_func function returns.
"""


def cache(times: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        cache_dict = {}

        @wraps(func)
        def cached_func(*args):
            if args in cache_dict and cache_dict[args][1] < times:
                cache_dict[args] = (cache_dict[args][0], cache_dict[args][1] + 1)
            else:
                result = func(*args)
                cache_dict[args] = (result, 1)
            return cache_dict[args][0]

        return cached_func

    return decorator