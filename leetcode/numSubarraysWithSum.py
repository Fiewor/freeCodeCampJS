# https://leetcode.com/problems/binary-subarrays-with-sum/?envType=daily-question&envId=2024-03-14

from typing import List

def numSubarraysWithSum(nums: List[int], goal: int) -> int:
    def helper(x):
        if x < 0: return 0

        l = res = curr = 0

        for r in range(len(nums)):
            curr += nums[r]

            while curr > x:
                curr -= nums[l]
                l += 1
            
            res += (r - l + 1)

        return res

    return helper(goal) - helper(goal - 1)

# nums = [0,0,0,0,0]
# goal = 0
nums = [1,0,1,0,1]
goal = 2
print(numSubarraysWithSum(nums, goal))
