import doctest
from task_4_doctest import fizzbuzz
"""
To run doctest with pytest, follow these steps:

1. Install Python 3.8 (https://www.python.org/downloads/)
2. Install pytest: pip install pytest
3. Create a file test_fizzbuzz.py in the same directory as the file with the fizzbuzz function.
4. In the file test_fizzbuzz.py write the following code:
"""


def test_doctest():
    result = doctest.testmod(fizzbuzz)
    assert result.failed == 0