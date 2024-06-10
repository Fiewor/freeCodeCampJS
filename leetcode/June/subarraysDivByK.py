# https://leetcode.com/problems/subarray-sums-divisible-by-k/?envType=daily-question&envId=2024-06-09


from collections import defaultdict
from typing import List

def subarraysDivByK(nums: List[int], k: int) -> int:
    res = 0
    rem = defaultdict(int)
    total_sum = 0
    
    for num in nums:
        total_sum += num
        mod = total_sum % k
        res += rem[mod]
        rem[mod] += 1

    return res