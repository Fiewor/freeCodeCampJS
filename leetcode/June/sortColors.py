# https://leetcode.com/problems/sort-colors/description/?envType=daily-question&envId=2024-06-12

from typing import List

def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    count = [0] * 3
    i = 0

    for num in nums:
        count[num] += 1

    for j in range(3):
        for _ in range(count[j]):
            nums[i] = j
            i += 1

nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)