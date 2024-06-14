# https://leetcode.com/problems/minimum-increment-to-make-array-unique/?envType=daily-question&envId=2024-06-14

from collections import Counter
from typing import List

# using sort
# time complexity -> O(nlogn)
def minIncrementForUnique(nums: List[int]) -> int:
    nums.sort()
    res = 0

    for i in range(1, len(nums)):
        if nums[i - 1] >= nums[i]:
            res += nums[i - 1] - nums[i] + 1
            nums[i] = nums[i - 1] + 1

    return res

# using hashmap counter
# time complexity -> O(n)
def minIncrementForUnique(nums: List[int]) -> int:
    count = Counter(nums)
    res = 0

    for i in range(max(nums) + len(nums)):
        if count[i] - 1 > 0:
            extra = count[i] - 1
            res += extra
            count[i + 1] += extra

    return res

nums = [3,2,1,2,1,7]
print(minIncrementForUnique(nums))