"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""

import string
from typing import List
from collections import Counter

"""
The function finds the 10 longest words,
which at the same time consist of the largest
number of unique characters
"""


def get_longest_diverse_words(data: str) -> List[str]:
    """Split words into a list"""
    words = data.split()
    """Initialize variable that will store sorted words"""
    sorted_words = []
    """Iterate through each word"""
    for word in words:
        """Initialize variable that will count number of unique symbols in word"""
        counter = 0
        """Iterterate through each character in word"""
        for char in word:
            """Check if symbol is already in list of unique symbols"""
            if char not in word[0:counter]:
                """increment counter"""
                counter += 1
                """Append word and counter to sorted words"""
        sorted_words.append((word, counter))
    """Sort words by unique symbols"""
    sorted_words.sort(key=lambda x: x[1], reverse=True)
    """Return top 10 longest words with most unique symbols"""
    return [word[0] for word in sorted_words[:10]]

    return longest_diverse_words


"""
The function looks for the most
 infrequent character in a text document
 """


def get_rarest_char(data: str) -> str:
    with open(data, 'r') as fi:
        text = fi.read()
    counter = Counter(text)
    rarest_char = min(counter, key=counter.get)
    return rarest_char


"""
function counts punctuation marks
"""


def count_punctuation_chars(data: str) -> int:
    with open(data, 'r') as fi:
        text = fi.read()
    count = sum([1 for char in text if char in string.punctuation])
    return count


"""
function finds the number of non-askii chars
"""


def count_non_ascii_chars(data: str) -> int:
    with open(data, 'r') as fi:
        text = fi.read()
    count = sum([1 for char in text if ord(char) >= 128])
    return count


"""
function finds the most frequently
occurring non-ascii char in a text document
"""


def get_most_common_non_ascii_char(data: str) -> str:
    with open(data, 'r') as fi:
        text = fi.read()
    non_ascii_chars = [char for char in text if ord(char) >= 128]
    counter = Counter(non_ascii_chars)
    most_common_non_ascii_char = max(counter, key=counter.get)
    return most_common_non_ascii_char