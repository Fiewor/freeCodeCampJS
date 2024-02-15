# https://leetcode.com/problems/rearrange-array-elements-by-sign/?envType=daily-question&envId=2024-02-14

from typing import List

def rearrangeArray(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [0] * n
    pos, neg = 0, 1

    for i in range(n):
        if nums[i] > 0:
            res[pos] = nums[i]
            pos += 2
        else:
            res[neg] = nums[i]
            neg += 2
    return res

nums = [3,1,-2,-5,2,-4]
# nums = [-1, 1]
print(rearrangeArray(nums))