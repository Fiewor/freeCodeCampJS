# https://leetcode.com/problems/subsets/description/?envType=daily-question&envId=2024-05-21

from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    res = []
    subsets = []

    def dfs(i):
        if i >= len(nums):
            res.append(subsets[:])
            return
        
        subsets.append(nums[i])
        dfs(i+1)

        subsets.pop()
        dfs(i+1)

    dfs(0)
    return res

print(subsets(nums = [1,2,3]))