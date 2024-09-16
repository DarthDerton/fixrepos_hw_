import functools
"""
Написать декоратор который позволит сохранять информацию из
исходной функции (__name__ and __doc__), а так же сохранит саму
исходную функцию в атрибуте __original_func

print_result изменять нельзя, за исключением добавления вашего
декоратора на строку отведенную под него - замените комментарий

До применения вашего декоратор будет вызываться AttributeError при custom_sum.__original_func
Это корректное поведение
После применения там должна быть исходная функция

Ожидаемый результат:
print(custom_sum.__doc__)  # 'This function can sum any objects which have __add___'
print(custom_sum.__name__)  # 'custom_sum'
print(custom_sum.__original_func)  # <function custom_sum at <some_id>>
"""


"""
The original_info_ decorator takes a function as an argument and returns another decorator original_info.
The original_info decorator takes a function as an argument and returns a wrapper function
that calls the original function.
The wrapper function also sets the name, doc,
and __original_func attributes of the original function on the wrapper function.

The print_result decorator takes a function as an argument and returns a wrapper function wrapper_print.
The wrapper function calls the original function and prints the result. The wrapper function then returns the result.
The print_result decorator also uses the original_info_
decorator to preserve the original function's information on the wrapper function.

Finally, the custom_sum function with the print_result decorator.
When custom_sum is called, the wrapper_print function is called instead.
The wrapper_print function calls the original custom_sum function and prints the result.
The wrapper_print function then returns the result.


"""


def original_info_(initial_func):
    def original_info(wrap_func):
        def wrapper(*args):
            return wrap_func(*args)
        wrapper.__name__ = initial_func.__name__
        wrapper.__doc__ = initial_func.__doc__
        wrapper.__original_func = initial_func
        return wrapper
    return original_info()


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