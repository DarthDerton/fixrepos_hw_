import pytest
from hw2 import MorningDiscount, ElderDiscount, Order

"""
In this example, we define a TestOrder class in which we define a test_final_price method that will test the final_price
method of the Order class. We use the @pytest.mark.parametrize decorator to define multiple test
cases with different argument values.
In each test case, we instantiate the Order class with the given price and discount_strategy values, and check that the
final_price method returns the expected expected value.
"""


class TestOrder:
    @pytest.mark.parametrize("price, discount_strategy, expected", [
        (100, MorningDiscount(), 75),
        (100, ElderDiscount(), 50),
        (200, MorningDiscount(), 150),
        (200, ElderDiscount(), 100),
    ])
    def test_final_price(self, price, discount_strategy, expected):
        order = Order(price, discount_strategy)
        assert order.final_price() == expected