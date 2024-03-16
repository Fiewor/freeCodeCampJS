# https://leetcode.com/problems/contiguous-array/?envType=daily-question&envId=2024-03-16

from typing import List

def findMaxLength(nums: List[int]) -> int:
    sum = 0
    diff_index = {}
    max_len = 0

    for i, num in enumerate(nums):
        sum += 1 if num == 1 else -1

        if sum not in diff_index:
            diff_index[sum] = i
        
        if sum == 0:
            max_len = i + 1
        else:
            idx = diff_index[sum]
            max_len = max(max_len, i - idx)

    return max_len


nums = [0,1,0,1]
print(findMaxLength(nums))
