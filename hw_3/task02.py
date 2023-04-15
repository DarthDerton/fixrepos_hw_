import multiprocessing
import random
import hashlib
import struct
from functools import partial
from time import time

"""
this implementation, we use the multiprocessing.
Pool class to create a pool of worker processes.
We then use the map method of the pool to apply
the slow_calculate function to each value in the range from 0 to 500.
The map method returns a list of results, which we sum to get the total sum.
Finally, we close the pool and join the worker processes.
"""


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1,3))
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


if __name__ == '__main__':
    calculate_total_sum()