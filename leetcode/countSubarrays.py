# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/?envType=daily-question&envId=2024-03-29

from typing import List

def countSubarrays(nums: List[int], k: int) -> int:
    max_n = max(nums)
    res = 0
    max_count = 0
    l = 0

    for r in range(len(nums)):
        if nums[r] == max_n:
            max_count += 1
        
        while max_count == k:
            if nums[l] == max_n:
                max_count -= 1
            l += 1
        res += l

    return res

nums = [1,3,2,3,3]
k = 2
print(countSubarrays(nums, k))