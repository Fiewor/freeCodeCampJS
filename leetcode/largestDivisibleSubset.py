# https://leetcode.com/problems/largest-divisible-subset/?envType=daily-question&envId=2024-02-09

from typing import List

def largestDivisibleSubset(nums: List[int]) -> List[int]:
    nums.sort()
    cache = {}

    def helper(i, prev):
        if (i, prev) in cache: return cache[(i, prev)]
        
        if i == len(nums): return []
        
        res = helper(i+1, prev)
        if nums[i] % prev == 0:
            temp = [nums[i]] + helper(i+1, nums[i])

            res = temp if len(temp) > len(res) else res
        
        cache[(i, prev)] = res
        return res

    return helper(0, 1)

def largestDivisibleSubset(nums: List[int]) -> List[int]:
    nums.sort()
    cache = {}

    def helper(i):
        if i in cache: return cache[i]
        if i == len(nums): return []
        
        res = [nums[i]]
        for j in range(i+1, len(nums)):
            if nums[j] % nums[i] == 0:
                temp = [nums[i]] + helper(j)

                if len(temp) > len(res):
                    res = temp

        cache[i] = res
        return res
    
    res = []
    for i in range(len(nums)):
        temp = helper(i)

        if len(temp) > len(res):
            res = temp

    return res

def largestDivisibleSubset(nums: List[int]) -> List[int]:
    nums.sort()

    tab = [[n] for n in nums]
    res = []

    for i in reversed(range(len(nums))):
        for j in range(i+1, len(nums)):
            if nums[j] % nums[i] == 0:
                temp = [nums[i]] + tab[j]
                tab[i]  = temp if len(temp) > len(tab[i]) else tab[i]
        res = tab[i] if len(tab[i]) > len(res) else res

    return res


nums = [1,2,3]
print(largestDivisibleSubset(nums))