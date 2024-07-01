# https://leetcode.com/problems/three-consecutive-odds/description/?envType=daily-question&envId=2024-07-01

from typing import List

def threeConsecutiveOdds(arr: List[int]) -> bool:
    odd = 0

    for el in arr:
        if el % 2 == 1:
            odd += 1
        else:
            odd = 0

        if odd == 3:
            return True

    return False