"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

from itertools import combinations
from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    combo = combinations(range(1, n + 1), k)
    combos = []
    for i in list(combo):
        combos.append(list(i))
    if len(combos) == 0:
        return [[n]]
    return combos
