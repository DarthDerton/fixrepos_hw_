"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""

from collections.abc import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    i = len(data) - 1
    if i < 2:
        return False
    else:
        while i >= 0:
            if data[i - 2] + data[i - 1] == data[i]:
                return True
            else:
                return False
        i -= 1