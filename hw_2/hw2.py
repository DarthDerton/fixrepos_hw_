"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.
You may assume that the array is non-empty and the most common element
always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3, 2
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2, 1
"""
from collections import Counter

from typing import List, Tuple

"""
The function first creates a `counts` dictionary
where the keys are the elements of the list and
the values are the number of occurrences in the list.
It then finds the most frequently occurring element 
using the `max` method with the `key=counts.get` parameter,
which returns the key with the maximum value in the `counts` dictionary.
Likewise, it finds the least frequently occurring element using the `min`
method with the `key=counts.get` parameter, which returns the key with
the minimum value in the `counts` dictionary.
"""


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    counter = Counter(inp)
    most_common = counter.most_common(1)[0][0]
    least_common = min(counter, key=counter.get)
    return most_common, least_common
