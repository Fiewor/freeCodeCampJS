# https://leetcode.com/problems/first-missing-positive/?envType=daily-question&envId=2024-03-26

from typing import List

# time complexity -> O(n)
# space complexity -> O(n)
def firstMissingPositive(nums: List[int]) -> int:
    nums_set = set(nums)

    for i in range(1, len(nums)+2):
        if i not in nums_set:
            return i

# time complexity -> O(n)
# space complexity -> O(1)
def firstMissingPositive(nums: List[int]) -> int:
    n = len(nums)
    for i in range(n):
        if nums[i] < 0:
            nums[i] = 0

    for i in range(n):
        ind = abs(nums[i]) - 1

        if 0 <= ind < n:
            if nums[ind] == 0:
                nums[ind] = -1 * (n+1)
            if nums[ind] > 0:
                nums[ind] *= -1
    
    for i in range(1, n+1):
        if nums[i - 1] >= 0:
            return 1
    
    return n + 1

#? Explanation for second solution
#! first loop
# replace negative numbers with 0
# the next loop is to help us know, in constant time if an element appears in the array
#! second loop 
# mark values as appearing in the array
# calculate i = abs(num) - 1. 
# ignore if i is out-of-bounds
# if nums[i] is 0, set to -len(nums)+1
# if already negative, ignore
# else set to -nums[i]
#! third loop
# loop from 1 - len(nums)-1
# calculate index = i - 1
# check nums[index] to know if i exists in input array nums
# if negative, it exists, if not, we've found our first positive missing number