import pytest
import multiprocessing
import random
import hashlib
import struct
from time import time


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def calculate_total_sum():
    start_time = time()
    pool = multiprocessing.Pool()
    values = range(501)
    total_sum = sum(pool.map(slow_calculate, values))
    pool.close()
    pool.join()
    end_time = time()
    print(f"Total sum: {total_sum}")
    print(f"Calculation time: {end_time - start_time} seconds")


@pytest.mark.parametrize("value, expected", [(0, 147), (1, 154), (2, 152), (3, 155), (4, 155)])
def test_slow_calculate(value, expected):
    assert slow_calculate(value) == expected