# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/description/

from typing import List

def minDifference(nums: List[int]) -> int:
    nums.sort()
    n = len(nums)
    if n <= 4:
        return 0
    return min(
        nums[n-4] - nums[0],
        nums[n-3] - nums[1],
        nums[n-2] - nums[2],
        nums[n-1] - nums[3],
    )

nums = [3,100,20]
print(minDifference(nums))