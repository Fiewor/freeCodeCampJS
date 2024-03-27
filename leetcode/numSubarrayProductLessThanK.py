# https://leetcode.com/problems/subarray-product-less-than-k/?envType=daily-question&envId=2024-03-27

def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    n = len(nums)
    l = 0
    prod = 1
    res = 0

    for r in range(n):
        prod *= nums[r]
        
        while prod >= k:
            prod /= nums[l]
            l += 1

        res += r - l + 1

    return res
