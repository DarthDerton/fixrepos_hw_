import pytest
from hw1 import get_most_common_non_ascii_char


@pytest.mark.parametrize("data, expected", [
    ("test_files/test1.txt", "é"),
    ("test_files/test2.txt", "ü"),
    ("test_files/test3.txt", "ñ"),
    ("test_files/test4.txt", "ß"),
    ("test_files/test5.txt", "ÿ")
])
def test_get_most_common_non_ascii_char(data: str, expected: str):
    assert get_most_common_non_ascii_char(data) == expected