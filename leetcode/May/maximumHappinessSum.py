# https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

from typing import List

def maximumHappinessSum(happiness: List[int], k: int) -> int:
    res = 0
    happiness.sort(reverse=True)
    ded = 0

    for i in range(k):
        res += max(happiness[i] - ded, 0)
        ded += 1
    
    return res


happiness = [1,2,3]
k = 2
print(maximumHappinessSum(happiness, k))