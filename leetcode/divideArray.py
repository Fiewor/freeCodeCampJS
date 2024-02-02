# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/?envType=daily-question&envId=2024-02-01

from typing import List

def divideArray(nums: List[int], k: int) -> List[List[int]]:
    nums.sort()
    res = []

    for i in range(0, len(nums), 3):
        if nums[i+2] - nums[i] > k:
            return []
        
        res.append(nums[i:i+3])

    return res

nums, k = [1,3,4,8,7,9,3,5,1], 2
print(divideArray(nums, k))