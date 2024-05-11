# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/?envType=daily-question&envId=2024-05-11

import heapq
from typing import List

def mincostToHireWorkers(quality: List[int], wage: List[int], k: int) -> float:
    res = float('inf')
    pairs = []

    for i in range(len(quality)):
        pairs.append((wage[i]/quality[i], quality[i]))

    pairs.sort(key=lambda p:p[0])

    maxHeap = []
    total_quantity = 0

    for rate, q in pairs:
        heapq.heappush(maxHeap, -q)
        total_quantity += q

        if len(maxHeap) > k:
            total_quantity += heapq.heappop(maxHeap) #adding because q was negated when pushing to heap
        
        if len(maxHeap) == k:
            res = min(res, total_quantity * rate)

    return res

quality = [10,20,5]
wage = [70,50,30]
k = 2

print(mincostToHireWorkers(quality, wage, k))