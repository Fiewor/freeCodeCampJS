# https://leetcode.com/problems/set-mismatch/

from collections import Counter
from typing import List

def findErrorNums(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [0] * 2
    rangee = list(range(1,n+1))
    count_y = {num:nums.count(num) for num in rangee}
    count_x = Counter(nums)
    
    for key, val in count_x.items():
        if val == 2:
            res[0] = key

    for key, val in count_y.items():
        if val == 0:
            res[1] = key
    return res
 
# # one count, one loop
def findErrorNums(nums: List[int]) -> List[int]:
    res = [0, 0]
    count = Counter(nums)

    for num in range(1, len(nums)+1):
        if count[num] == 0:
            res[1] = num

        if count[num] == 2:
            res[0] = num
    
    return res

# in-place solution
def findErrorNums(nums: List[int]) -> List[int]:
    res = [0, 0]

    for i in nums:
        i = abs(i)
        nums[i-1] = -nums[i-1]

        if nums[i-1] > 0:
            res[0] = i
        
    for i, n in enumerate(nums):
        if n > 0 and i+1 != res[0]:
            res[1] = i+1

    return res

# math approach
def findErrorNums(nums: List[int]) -> List[int]:
    n = len(nums)
    x, y = 0, 0

    for i in range(1, n+1):
        x += nums[i-1] - i
        y += nums[i-1]**2 - i**2

    missing = (y - x**2) // (2 * x)
    duplicate = x + missing

    return [duplicate, missing]
nums=[1, 2, 2, 4]
print(findErrorNums(nums))