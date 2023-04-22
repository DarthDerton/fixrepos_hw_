import urllib.request


"""
Write a function that accepts an URL as input
and count how many letters `i` are present in the HTML by this URL.

Write a test that check that your function works.
Test should use Mock instead of real network interactions.

You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests

You will learn:
 - how to test using mocks
 - how to write complex mocks
 - how to raise an exception form mocks
 - do a simple network requests


>>> count_dots_on_i("https://example.com/")
59

* https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
"""

"""
This function uses the urllib.request.urlopen method to open the URL and read the HTML content.
It then decodes the content using the utf-8 encoding and counts the number of letter 'i'
present in the HTML content using the count method.
"""


def count_dots_on_i(url: str) -> int:
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')
        return html.count('i')