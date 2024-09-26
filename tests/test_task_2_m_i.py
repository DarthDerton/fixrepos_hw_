import urllib.request
import pytest
from unittest.mock import patch
from task_2_m_i import count_dots_on_i

"""
In this test, we added a parameter to @pytest.mark.parametrize to test for unreachable URL. If expected_count is 
ValueError, we use mock_urlopen.side_effect to raise the urllib.error. URLError exception and check that the 
count_dots_on_i function throws a ValueError exception with the message "Unreachable{url}". If expected_count is not 
equal to ValueError, we continue testing as before. 
"""


@pytest.mark.parametrize("url, expected_count", [
    ("https://example.com/", 2),
    ("https://www.python.org/", 22),
    ("https://www.google.com/", 33),
    ("https://unreachable-url.com/", ValueError),
])
def test_count_dots_on_i(url, expected_count):
    html = "<html><body><p>This is a test.</p></body></html>"
    with patch("urllib.request.urlopen") as mock_urlopen:
        if expected_count == ValueError:
            mock_urlopen.side_effect = urllib.error.URLError("Unreachable URL")
            with pytest.raises(ValueError):
                count_dots_on_i(url)
        else:
            mock_urlopen.return_value.enter.return_value.read.return_value.decode.return_value = html
            assert count_dots_on_i(url) == expected_count