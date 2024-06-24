# https://leetcode.com/problems/sliding-window-maximum/

from collections import deque
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    res = []
    q = deque()
    l = 0
    
    for r in range(len(nums)):
        while q and nums[q[-1]] < nums[r]:
            q.pop()

        q.append(r)

        if l > q[0]:
            q.popleft()

        if (r-l)+1 >= k:
            res.append(nums[q[0]])
            l += 1

    return res

nums = [1]
k = 1
print(maxSlidingWindow(nums, k))