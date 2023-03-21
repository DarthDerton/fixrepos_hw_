"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import List, Any

def combinations(*args: List[Any]) -> List[List]:
    """
    This function takes K lists as arguments and returns all possible lists of K items
    where the first element is from the first list, the second is from the second and so one.
    """
    """return empty list if arguments are empty lists"""
    if not [arg for arg in args if arg]:
        return []

    """length of the combination"""
    lc = len(args)

    """initialize the list to store all combinations"""
    all_possible_combinations = []

    """initialize the list with indices to track the current combinations"""
    indices = [0 for _ in range(len(args))]

    """loop until all combinations exhaust"""
    while True:
        """append new combination to all possible combinations"""
        combination = [arg[i] for arg, i in zip(args, indices)]
        all_possible_combinations.append(combination)

        """increment the last index unless it's exhausted"""
        if indices[-1] < len(args[-1]) - 1:
            indices[-1] += 1

        elif all(i == len(arg) - 1 for i, arg in zip(indices, args)):
            break

        else:
            for j in range(lc - 1, 0, -1):
                if indices[j] < len(args[j]) - 1:
                    indices[j] += 1
                    indices[j + 1:] = [0] * (lc - 1 - j)
                    break

    return all_possible_combinations