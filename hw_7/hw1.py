"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""


from pathlib import Path
from typing import List, Union, Iterator


"""
The function first opens all the files in the input list and reads the integers from each
file using a list comprehension. It then merges the integers into a single sorted list using a while loop that
repeatedly finds the minimum value among the first elements of the remaining lists and appends it to the merged list.
Finally, the function closes all the files and returns an iterator over the merged
list using the iter built-in function.
"""


def merge_sorted_files(file_list: List[Union[Path, str]] = ["file1.txt", "file2.txt"]) -> Iterator[int]:
    # Open all files and read the integers
    files = [open(file, 'r') for file in file_list]
    integers = [[int(num) for num in file.read().split()] for file in files]

    merged = []
    while integers:
        min_val = float('inf')
        min_idx = None
        for i, nums in enumerate(integers):
            if nums and nums[0] < min_val:
                min_val = nums[0]
                min_idx = i
        if min_idx is not None:
            merged.append(min_val)
            integers[min_idx].pop(0)
        else:
            break

    for file in files:
        file.close()

    return iter(merged)