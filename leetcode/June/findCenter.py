# https://leetcode.com/problems/find-center-of-star-graph/?envType=daily-question&envId=2024-06-27

from collections import defaultdict
from typing import List

def findCenter(edges: List[List[int]]) -> int:
    count = defaultdict(int)

    for n1, n2 in edges:
        if count[n1]:
            return n1
        if count[n2]:
            return n2
        
        count[n1] += 1
        count[n2] += 1

edges = [[1,2],[2,3],[4,2]]
print(findCenter(edges))