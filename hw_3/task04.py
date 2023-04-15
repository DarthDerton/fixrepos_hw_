from functools import reduce
"""
Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
https://en.wikipedia.org/wiki/Narcissistic_number

Examples:

- 9 is an Armstrong number, 9 = 9^1 = 9
- 10 is not: 10 != 1^2 + 0^2 = 1
- 153 is : 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153


Write a function that detects if a number is Armstrong number in functionaly style:
 - use map or other utilities from functools library,
 - use anonymous functions (or use function as argument)
 - do not use loops, preferably using list comprehensions

### Example function signature and call
"""


def is_armstrong(number: int) -> bool:
    digits = list(map(int, str(number)))
    num_digits = len(digits)
    powered_digits = list(map(lambda x: x ** num_digits, digits))
    return reduce(lambda x, y: x + y, powered_digits) == number


assert is_armstrong(153) == True, 'Is Armstrong number'
assert is_armstrong(10) == False, 'Is not Armstrong number'

"""
The map() and reduce() functions from the functools module are used to convert the number to a list of digits,
raise each digit to the power of the number of digits, and add them.
We also use an anonymous lambda function to integrate into the exponent and check if the sum of the digits
in the exponent of the original spread is equal.
"""