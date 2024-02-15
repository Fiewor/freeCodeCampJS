# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/?envType=daily-question&envId=2024-02-15

from typing import List

# forward iteration
def largestPerimeter(nums: List[int]) -> int:
    nums.sort()
    ans = -1
    running_sum = 0

    for num in nums:
        if num < running_sum:
            ans = running_sum + num
        running_sum += num

    return ans

# backward iteration
def largestPerimeter(nums: List[int]) -> int:
    nums.sort()
    _sum = sum(nums)

    for i in range(len(nums)-1, 1, -1):
        _sum -= nums[i]
        if _sum > nums[i]:
            return _sum + nums[i]

    return -1

# nums = [5,5,50]
nums = [1,12,1,2,5,50,3]
print(largestPerimeter(nums))