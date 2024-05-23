# https://leetcode.com/problems/the-number-of-beautiful-subsets/?envType=daily-question&envId=2024-05-23

from collections import Counter, defaultdict
from typing import List

# time complexity -> O(N^2)
def beautifulSubsets(nums: List[int], k: int) -> int:
    def helper(i, count):
        if i == len(nums):
            return 1
        
        res = helper(i+1, count)
        if not count[nums[i]-k] and not count[nums[i]+k]:
            count[nums[i]] += 1
            res += helper(i+1, count)
            count[nums[i]] -= 1

        return res
    
    return helper(0, defaultdict(int)) - 1


# time complexity -> O(N)
def beautifulSubsets(nums: List[int], k: int) -> int:
    cache = {}
    vis = set()
    groups = []
    cnt = Counter(nums)

    def helper(n, g):
        if n not in g:
            return 1
        
        if n in cache:
            return cache[n]
        
        take = helper(n+k, g)
        noTake = (2**g[n] - 1) * helper(n+2*k, g)

        cache[n] = take + noTake
        return take + noTake 

    for n in cnt.keys():
        if n in vis:
            continue

        g = {}

        while n-k in cnt:
            n -= k

        while n in cnt:
            g[n] = cnt[n]
            vis.add(n)
            n += k
        
        groups.append(g)
    
    res = 1
    for g in groups:
        n = min(g.keys())
        res *= helper(n, g)
    return res - 1

nums = [2,4,6]
k = 2

print(beautifulSubsets(nums, k))