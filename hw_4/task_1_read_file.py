import os
"""
Write a function that gets file path as an argument.
Read the first line of the file.
If first line is a number return true if number in an interval [1, 3)*
and false otherwise.
In case of any error, a ValueError should be thrown.

Write a test for that function using pytest library.

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - all temporary files are removed after test run

You will learn:
 - how to test Exceptional cases
 - how to clean up after tests
 - how to check if file exists**
 - how to handle*** and raise**** exceptions in test. Use sample from the documentation.

* https://en.wikipedia.org/wiki/Interval_(mathematics)#Terminology
** https://docs.python.org/3/library/os.path.html
*** https://docs.python.org/3/tutorial/errors.html#handling-exceptions
**** https://docs.python.org/3/tutorial/errors.html#raising-exceptions
"""

"""
In this solution, we use the os.path module to check for the existence of a file.
If the file does not exist, we throw a ValueError exception.
Then we open the file and read the first line.
If the first string is a number, we check if it is in the interval [1, 3) and return the corresponding value.
If the first string is not a number, we throw a ValueError exception.
"""


def read_magic_number(path: str) -> bool:
    if not os.path.isfile(path):
        raise ValueError("File not found")
    with open(path, 'r') as f:
        try:
            first_line = float(f.readline().strip())
            if 1 <= first_line < 3:
                return True
            else:
                return False
        except ValueError:
            raise ValueError("Invalid file content")