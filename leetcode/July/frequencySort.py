# leetcode.com/problems/sort-array-by-increasing-frequency/?envType=daily-question&envId=2024-07-23

from collections import Counter
from typing import List

def frequencySort(nums: List[int]) -> List[int]:
    count = Counter(nums)
    
    def custom_sort(x):
        return (count[x], -x)

    nums.sort(key=custom_sort)
    return nums

def frequencySort(nums: List[int]) -> List[int]:
    count = Counter(nums)
    nums.sort(key=lambda x:(count[x], -x))
    return nums

nums = [2,3,1,3,2]
print(frequencySort(nums))