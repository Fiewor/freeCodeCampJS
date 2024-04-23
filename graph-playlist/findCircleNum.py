# https://leetcode.com/problems/number-of-provinces/

from collections import defaultdict
from typing import List


def findCircleNum(self, isConnected: List[List[int]]) -> int:
    count = 0
    ROWS, COLS = len(isConnected), len(isConnected[0])
    adjList = defaultdict(list)
    vis = set()

    # build adjacency list
    for r in range(ROWS):
        for c in range(COLS):
            if isConnected[r][c] == 1 and r != c:
                adjList[r+1] += [c+1]
                adjList[c+1] += [r+1]
    
    def dfs(node):
        vis.add(node)

        for neighbour in adjList[node]:
            if neighbour not in vis:
                dfs(neighbour)
                
        return                

    for i in range(1, ROWS+1):
        if i not in vis:
            count += 1
            dfs(i)
    
    return count