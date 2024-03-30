# https://leetcode.com/problems/subarrays-with-k-different-integers/?envType=daily-question&envId=2024-03-30

from collections import defaultdict
from typing import List

def subarraysWithKDistinct(nums: List[int], k: int) -> int:
    res = 0
    count = defaultdict(int)
    l_near = 0
    l_far = 0

    for r in range(len(nums)):
        count[nums[r]] += 1

        while len(count) > k:
            count[nums[l_near]] -= 1

            if count[nums[l_near]] == 0:
                count.pop(nums[l_near])

            l_near += 1
            l_far = l_near

        while count[nums[l_near]] > 1:
            count[nums[l_near]] -= 1
            l_near += 1
        
        if len(count) == k:
            res += l_near - l_far + 1

    return res

nums = [1,2,1,2,3]
k = 2
print(subarraysWithKDistinct(nums, k))