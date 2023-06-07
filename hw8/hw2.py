"""
You are given the following code:

class Order:
    morning_discount = 0.25

    def __init__(self, price):
        self.price = price

    def final_price(self):
        return self.price - self.price * self.morning_discount

Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy

Example of the result call:

def morning_discount(order):
    ...

def elder_discount(order):
    ...

order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50

order_2 = Order(100, elder_discount)
assert order_1.final_price() == 10
"""

"""
To make it possible to use different discount programs, we can use the strategy design pattern.
This pattern allows us to define a family of algorithms, encapsulate each one, and make them interchangeable.
In this case, we can define a DiscountStrategy interface with a single method apply_discount,
and then implement different discount strategies as concrete classes that implement this interface.
"""


class DiscountStrategy:
    def apply_discount(self, price):
        pass


class MorningDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.25


class ElderDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.5


class Order:
    def __init__(self, price, discount_strategy):
        self.price = price
        self.discount_strategy = discount_strategy

    def final_price(self):
        return self.price - self.discount_strategy.apply_discount(self.price)