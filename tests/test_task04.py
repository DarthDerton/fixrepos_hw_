import pytest
from task04 import is_armstrong


def test_is_armstrong_true():
    assert is_armstrong(153) == True


def test_is_armstrong_false():
    assert is_armstrong(10) == False


def test_is_armstrong_zero():
    assert is_armstrong(0) == True


def test_is_armstrong_single_digit():
    assert is_armstrong(5) == True


def test_is_armstrong_large_number():
    assert is_armstrong(9474) == True


def test_is_armstrong_negative_number():
    assert is_armstrong(-153) == False


def test_is_armstrong_float_number():
    assert is_armstrong(153.0) == True


def test_is_armstrong_string():
    with pytest.raises(TypeError):
        is_armstrong('153')


def test_is_armstrong_list():
    with pytest.raises(TypeError):
        is_armstrong([1, 5, 3])


def test_is_armstrong_dict():
    with pytest.raises(TypeError):
        is_armstrong({1: 5, 3: 7})