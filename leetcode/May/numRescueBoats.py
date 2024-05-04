# https://leetcode.com/problems/boats-to-save-people/?envType=daily-question&envId=2024-05-04

from typing import List

def numRescueBoats(p: List[int], limit: int) -> int:
    p.sort()
    boats = 0
    l, r = 0, len(p) - 1

    while l <= r:
        boats += 1

        if p[l] + p[r] <= limit:
            l += 1
        r -=1

    return boats

print(numRescueBoats([3,2,2,1], 3))