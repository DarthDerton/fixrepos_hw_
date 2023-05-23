import pytest
from pathlib import Path
from typing import List, Union, Iterator

from hw1 import merge_sorted_files


@pytest.mark.parametrize("file_list, expected", [
    (["tests/test_files/file1.txt", "tests/test_files/file2.txt"], [1, 2, 3, 4, 5, 6]),
    (["tests/test_files/file3.txt", "tests/test_files/file4.txt"], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    (["tests/test_files/file5.txt"], [1, 2, 3, 4, 5]),
    ([], []),
])
def test_merge_sorted_files(file_list: List[Union[Path, str]], expected: List[int]):
    result = list(merge_sorted_files(file_list))
    assert result == expected