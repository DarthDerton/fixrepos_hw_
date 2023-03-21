"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return [1, 5]
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open("some_file.txt") as fi:
    for line in fi:
        ...
"""
from typing import Tuple

"""the function reads the t.txt file and outputs
 from a sequence of numbers located one number on each line
  a tuple consisting of the minimum and maximum numbers in the sequence"""


def find_maximum_and_minimum(t: str) -> tuple[float, float]:
    maximum = float('-inf')
    """infinity num"""
    minimum = float('inf')
    """ minus infinity num"""
    with open(t.txt, 'r') as fi:
        for line in fi:
            num = float(line)
            minimum = min(minimum, num)
            maximum = max(maximum, num)
    kort = [minimum, maximum]
    return kort