"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List

"""the function calculates the number of tuples (i, j, k, l) such that A[i] + B[j] + C[k] + D[l] = zero"""


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    count = 0
    for i in range(len(a)):
        for j in range(len(b)):
            for h in range(len(c)):
                for l in range(len(d)):
                    if a[i]+b[j]+c[h]+d[l] == 0:
                        count += 1
    return count