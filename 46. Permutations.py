"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

from itertools import permutations
from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    perm = permutations(nums)
    perms = []
    for i in perm:
        perms.append(i)
    return perms
