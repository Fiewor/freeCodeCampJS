# https://leetcode.com/problems/product-of-array-except-self/?envType=daily-question&envId=2024-03-15

from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [0] * n

    res[0] = 1
    for i in range(1, n):
        res[i] = res[i-1] * nums[i- 1]

    postfix = 1
    for i in range(n-1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res

nums = [1,2,3,4]
print(productExceptSelf(nums))