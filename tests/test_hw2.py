import pytest
from hw2 import supressor, supressor_generator


@pytest.mark.parametrize("suppressor_type", [supressor, supressor_generator])
def test_suppressor(suppressor_type):
    with suppressor_type(IndexError):
        assert [][2] is None