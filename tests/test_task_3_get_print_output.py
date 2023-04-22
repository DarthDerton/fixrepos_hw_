import sys
import pytest


"""
In this test, we use the pytest.mark.parametrize decorator to define two test cases for the my_precious_logger function.
The first case checks that the function correctly writes text to stdout if the text does not begin with "error".
The second case checks that the function correctly writes text to stderr if the text starts with "error".

Also use the capsys object provided by Pytest to capture the function's output and inspect its content.
"""


def my_precious_logger(text: str):
    if text.startswith("error"):
        sys.stderr.write(text)
    else:
        sys.stdout.write(text)


@pytest.mark.parametrize("text, expected_output", [
    ("hello", "hello"),
    ("error", "error")
])
def test_my_precious_logger(text, expected_output, capsys):
    my_precious_logger(text)
    captured = capsys.readouterr()
    assert captured.out == expected_output if not text.startswith("error") else ""
    assert captured.err == expected_output if text.startswith("error") else ""