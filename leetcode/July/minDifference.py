# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/description/?envType=daily-question&envId=2024-07-03

import heapq
from typing import List

# time complexity -> O(nlogn)
def minDifference(nums: List[int]) -> int:
    n = len(nums)
    if n <= 4: return 0
    nums.sort()
    return min(
        nums[n-4] - nums[0],
        nums[n-3] - nums[1],
        nums[n-2] - nums[2],
        nums[n-1] - nums[3],
    )

# time complexity -> O(nlogn)
def minDifference(nums: List[int]) -> int:
    if len(nums) <= 4: return 0

    nums.sort()

    res = float('inf')

    for l in range(4):
        r = len(nums) - 4 + l
        res = min(
            res,
            nums[r] - nums[l]
        )
    
    return res

# # time complexity -> O(n)
def minDifference(nums: List[int]) -> int:
    if len(nums) <= 4: return 0

    res = float('inf')

    min_four = sorted(heapq.nsmallest(4, nums))
    max_four = sorted(heapq.nlargest(4, nums))

    for i in range(4):
        res = min(
            res,
            max_four[i] - min_four[i]
        )
    
    return res    

nums = [1,5,0,10,14]
print(minDifference(nums))