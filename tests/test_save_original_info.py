import pytest
import functools
from save_original_info import original_info_


"""
В данном примере мы написали три теста для функций custom_sum, original_info_ и without_print.
В первом тесте мы использовали декоратор pytest.mark.parametrize,
чтобы проверить несколько тестовых случаев для функции custom_sum.
Во втором тесте мы проверили, что декоратор original_info_ сохраняет информацию о функции.
В третьем тесте мы проверили, что мы можем получить оригинальную функцию без декоратора print_result.
"""


def original_info_(initial_func):
    def original_info(wrap_func):
        def wrapper(*args):
            return wrap_func(*args)
        wrapper.__name__ = initial_func.__name__
        wrapper.__doc__ = initial_func.__doc__
        wrapper.__original_func = initial_func
        return wrapper
    return original_info(initial_func)


def print_result(func):
    @original_info_(func)
    def wrapper_print(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper_print


@print_result
def custom_sum(*args):
    return functools.reduce(lambda x, y: x + y, args)


@pytest.mark.parametrize("input_args, expected_output", [
    ([1, 2, 3, 4], 10),
    ([1, 2, 3], 6),
    ([1, 2, 3, 4, 5], 15),
    ([], TypeError),
    (["a", "b", "c"], TypeError)
])
def test_custom_sum(input_args, expected_output):
    if expected_output == TypeError:
        with pytest.raises(TypeError):
            custom_sum(*input_args)
    else:
        assert custom_sum(*input_args) == expected_output


def test_original_info():
    @original_info_(custom_sum)
    def new_func(*args):
        pass

    assert new_func.__name__ == "custom_sum"
    assert new_func.__doc__ == "This function can sum any objects which have __add__"
    assert new_func.__original_func == custom_sum


def test_without_print():
    without_print = custom_sum.__original_func
    assert without_print(1, 2, 3, 4) == 10