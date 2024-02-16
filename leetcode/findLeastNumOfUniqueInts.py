# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/?envType=daily-question&envId=2024-02-16

from collections import Counter
import heapq
from typing import List

# sorting
# def findLeastNumOfUniqueInts(arr: List[int], k: int) -> int:
#     c = Counter(arr)
#     counts = sorted(c.items(), key=lambda x:x[1])
#     no_of_unique_elements = len(c.keys())
    
#     for _, freq in counts:
#         if k >= freq:
#             no_of_unique_elements -= 1
#             k -= freq
    
#     return no_of_unique_elements

# min-heap
def findLeastNumOfUniqueInts(arr: List[int], k: int) -> int:
    freq = Counter(arr)
    heap = list(freq.values())
    res = len(heap)
    heapq.heapify(heap)

    while heap:
        freq = heapq.heappop(heap)

        if k >= freq:
            res -= 1
            k -= freq
        
    return res


arr = [24,119,157,446,251,117,22,168,374,373,323,311,441,213,120,412,200,236,328,24,164,104,331,32,19,223,89,114,152,82,456,381,355,343,157,245,443,368,229,49,82,16,373,142,240,125,8]
k = 41
arr = [4,3,1,1,3,3,2]
k = 3
# arr = [2,4,1,8,3,5,1,3]
# k = 5
# arr = [5,5,4]
# k = 1
print(findLeastNumOfUniqueInts(arr, k))