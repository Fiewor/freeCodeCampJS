# https://leetcode.com/problems/continuous-subarray-sum/?envType=daily-question&envId=2024-06-08

from typing import List

def checkSubarraySum(nums: List[int], k: int) -> bool:
    total = 0
    map = {}

    for i, num in enumerate(nums):
        total += num
        rem = total % k

        if rem in map:
            if i - map[rem] > 1:
                return True
        else:
            map[rem] = i
        
    return False

# nums = [23,2,4,6,7]
# k = 6
nums = [23,2,6,4,7]
k = 13
print(checkSubarraySum(nums, k))