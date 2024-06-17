#  https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
import heapq
from typing import List

# sorting
def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = {num:nums.count(num) for num in nums}
    res = sorted(count, key=lambda x:count[x], reverse=True)
    return res[:k]

# also sorting. implemented a bit differently
def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    count = {key:val for key,val in sorted(count.items(), key=lambda x:x[1])}
    return list(reversed(count.keys()))[:k] # i didn't remember you could pass in reverse=True to sorted lol


# max heap
# time complexity -> O(n.klogn) heapify takes O(n). each pop takes O(logn) and we would be doing that k times
def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    maxHeap = [(-freq,num) for num,freq in count.items()]
    heapq.heapify(maxHeap)

    res = []
    for _ in range(k):
        _, num = heapq.heappop(maxHeap)
        res.append(num)
    
    return res

# bucket sort
# time complexity -> O(n)
# space complexity -> O(n)
def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    bucket = [[] for _ in range(len(nums)+1)]

    for num,freq in count.items():
        bucket[freq].append(num)
    
    res = []
    for item in reversed(bucket): #cause you need the largest
        for el in item:
            res.append(el)
            if len(res) == k:
                return res

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))