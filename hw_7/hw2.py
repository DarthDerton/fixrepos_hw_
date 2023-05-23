"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with supressor(IndexError):
...    [][2]

"""

"""
Here's an implementation of the context manager that suppresses a passed exception as a class
"""


class supressor:
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if isinstance(exc_value, self.exception):
            return True


"""
Here's an implementation of the same context manager as a generator
"""

from contextlib import contextmanager


@contextmanager
def supressor_generator(exception):
    try:
        yield
    except exception:
        pass
