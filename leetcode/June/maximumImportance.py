# https://leetcode.com/problems/maximum-total-importance-of-roads/?envType=daily-question&envId=2024-06-28

from typing import List

def maximumImportance(n: int, roads: List[List[int]]) -> int:
    count_edges = [0] * n

    for n1, n2 in roads:
        count_edges[n1] += 1
        count_edges[n2] += 1

    label = 1
    res = 0

    for count in sorted(count_edges):
        res += label * count
        label += 1
    
    return res

n = 5
roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
print(maximumImportance(n, roads))