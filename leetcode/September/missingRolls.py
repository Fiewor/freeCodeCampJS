# https://leetcode.com/problems/find-missing-observations/description/?envType=daily-question&envId=2024-09-05

from typing import List


def missingRolls(rolls: List[int], mean: int, n: int) -> List[int]:
    m = len(rolls)
    max_dice_roll = 6
    total_sum = (m + n) * mean
    missing_sum = total_sum - sum(rolls)

    if missing_sum < n or missing_sum > max_dice_roll * n:
        return []

    res = []

    for x in range(n, 0, -1):
        val = min(max_dice_roll, missing_sum - x + 1)
        res.append(val)
        missing_sum -= val
    
    return res


rolls = [1,5,6]
mean = 3
n = 4
print(missingRolls(rolls, mean, n))