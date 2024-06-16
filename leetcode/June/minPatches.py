# https://leetcode.com/problems/patching-array/description/?envType=daily-question&envId=2024-06-16

from typing import List

def minPatches(nums: List[int], n: int) -> int:
    i = 0
    res = 0
    end = 1

    while end < n:
        if i < len(nums) and nums[i] <= end:
            end += nums[i]
            i += 1
        else:
            res += 1
            end += end

    return res

nums = [1,5,10]
n = 20
print(minPatches(nums, n))