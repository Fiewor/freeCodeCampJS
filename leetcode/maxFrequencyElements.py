# https://leetcode.com/problems/count-elements-with-maximum-frequency/?envType=daily-question&envId=2024-03-08

from collections import Counter

def maxFrequencyElements(nums: list[int]) -> int:
    count = Counter(nums)
    maxFreq = max(count.values())
    return sum([val for val in count.values() if val == maxFreq])

nums = [1,2,2,3,1,4]
print(maxFrequencyElements(nums))
