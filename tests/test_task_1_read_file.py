import pytest
import os
from task_1_read_file import read_magic_number


"""
This example defines multiple test cases using the pytest.mark.parametrize decorator.
Each test case is a two-tuple: the contents of the file and the expected result.
Use pytest.raises to check if exceptions are thrown.
Inside the test case, a temporary file is created, the contents are written to it, and we check that the read_magic_number function returns the expected result.
After each test case, the temporary file is deleted.
"""


@pytest.mark.parametrize("file_content, expected_output", [
    ('2.5', True),
    ('0.5', False),
    ('not a number', pytest.raises(ValueError, match="Invalid file content")),
    ('', pytest.raises(ValueError, match="Invalid file content")),
    (None, pytest.raises(TypeError, match="Invalid argument type")),
    ('nonexistent_file.txt', pytest.raises(ValueError, match="File not found"))
])
def test_read_magic_number(file_content, expected_output):
    with open('test_file.txt', 'w') as f:
        f.write(file_content if file_content is not None else '')
    with expected_output:
        assert read_magic_number('test_file.txt') == (file_content is not None and float(file_content) >= 1 and float(file_content) < 3)
    os.remove('test_file.txt')