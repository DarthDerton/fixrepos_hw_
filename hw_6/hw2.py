"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""

"""
We define a backspace_compare function that takes two strings first and second and returns
True if they are equal after processing the # characters, and False otherwise.

To process the # characters, we define an internal process_string function that takes the string s and returns
a new string with the # characters replaced by deleting the previous character. To do this,
we use a stack where we push characters other than #
and remove the last character from the stack if we encounter a # character.

We then compare the processed strings first and second and return True if they are equal,
False otherwise.
"""


def backspace_compare(first: str, second: str) -> bool:
    def process_string(s: str) -> str:
        stack = []
        for c in s:
            if c == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)

    return process_string(first) == process_string(second)