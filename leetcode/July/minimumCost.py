# https://leetcode.com/problems/minimum-cost-to-convert-string-i/?envType=daily-question&envId=2024-07-27

from collections import defaultdict
import heapq
from typing import List


def minimumCost(source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
    adj = defaultdict(list)

    for src, dest, cost in zip(original, changed, cost):
        adj[src].append((dest, cost))
    
    def dijkstra(src):
        map = {}
        minHeap = [(0, src)]
        heapq.heapify(minHeap)

        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if node in map:
                continue
            map[node] = cost

            for nei, nei_cost in adj[node]:
                heapq.heappush(minHeap, (cost + nei_cost, nei))
        return map
    
    map = {char: dijkstra(char) for char in set(source)}
    re = 0

    for src, dest in zip(source, target):
        if dest not in map[src]:
            return -1
        
        re += map[src][dest]

    return re
    
source = "abcd"
target = "acbe"
original = ["a","b","c","c","e","d"]
changed = ["b","c","b","e","b","e"]
cost = [2,5,5,1,2,20]
print(minimumCost(source, target, original, changed, cost))