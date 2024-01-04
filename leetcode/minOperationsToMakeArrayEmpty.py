# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

from collections import Counter

def minOperations(nums: list[int]) -> int:
    # ----- time limited exceeded
    # seen = {num:nums.count(num) for num in nums}

    # if 1 in seen.values():
    #     return -1
    # else:
    #     return sum(math.ceil(value // 3) for value in seen.values())

    cache = {}
    def dfs(n):
        if n < 0:
            return float('inf')
        if n in [2, 3]:
            return 1
        if n in cache:
            return cache[n]
        res = min(dfs(n - 2), dfs(n - 3))
        if res == -1:
            return -1
        cache[n] = res + 1
        return res + 1
    
    ans = 0
    count = Counter(nums)
    for val in count.values():
        res = dfs(val)
        if res == float('inf'):
            return -1
        ans += res
    return ans

# nums = [2,3,3,2,2,4,2,3,4]
nums = [14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]
print(minOperations(nums))