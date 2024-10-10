# https://leetcode.com/problems/maximum-width-ramp/?envType=daily-question&envId=2024-10-10

from typing import List

def maxWidthRamp(nums: List[int]) -> int:
    n = len(nums)
    max_right = [0] * n
    prev_max = 0

    for i in range(n-1, -1, -1):
        max_right[i] = max(prev_max, nums[i])
        prev_max = max_right[i]
    
    ans = 0
    l = 0
    for r in range(n):
        if nums[l] > max_right[r]:
            l += 1
        ans = max(ans, r-l)
    return ans


nums = [9,8,1,0,1,9,4,0,4,1]
print(maxWidthRamp(nums))