# https://leetcode.com/problems/island-perimeter/?envType=daily-question&envId=2024-04-18

from typing import List

def islandPerimeter(grid: List[List[int]]) -> int:
    vis = set()
    ROWS, COLS = len(grid), len(grid[0])

    def dfs(i, j):
        if i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j] == 0: # out-of-bounds or gotten to water
            return 1
        
        if (i, j) in vis:
            return 0
        
        vis.add((i, j))

        perim = dfs(i, j+1) + dfs(i+1, j) + dfs(i, j-1) + dfs(i-1, j)
        return perim

    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j]:
                return dfs[i][j]