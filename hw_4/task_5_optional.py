from typing import List, Generator
"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


>>> list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""


"""
This function uses  that in Python, True is equivalent to 1 and False is equivalent to 0.
Therefore, the expression i%3==0 evaluates to True if i is divisible by 3 and False otherwise.
Similarly, the expression i%5==0 evaluates to True if i is divisible by 5 and False otherwise.
The expression "fizz"*(i%3==0) evaluates to the string "fizz" if i is divisible by 3 and the empty string "" otherwise.
Similarly, the expression "buzz"*(i%5==0) evaluates to the string "buzz" if i is divisible by 5 and the empty string "" otherwise.
The expression "fizz"*(i%3==0) + "buzz"*(i%5==0) concatenates these two strings if i is divisible by both 3 and 5, "fizz"
if i is divisible by 3 but not 5, "buzz" if i is divisible by 5 but not 3, and the empty string "" otherwise. Finally,
the expression or str(i) returns the FizzBuzz string if it is non-empty and the string representation of i otherwise.
"""


def fizzbuzz(n: int) -> Generator[str]:
    for i in range(1, n + 1):
        yield "fizz" * (i % 3 == 0) + "buzz" * (i % 5 == 0) or str(i)