# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/?envType=daily-question&envId=2024-08-02

from typing import List

def minSwaps(nums: List[int]) -> int:
    total_ones = nums.count(1)
    max_num_of_ones = cur_window_of_ones = 0
    l = 0
    N = len(nums)

    for r in range(2 * N):
        if nums[r % N] == 1:
            cur_window_of_ones += 1

        if r - l + 1 > total_ones:
            cur_window_of_ones -= nums[l % N]
            l += 1

        max_num_of_ones = max(max_num_of_ones, cur_window_of_ones)
    
    return total_ones - max_num_of_ones

nums = [0,1,1,1,0,0,1,1,0]
print(minSwaps(nums))