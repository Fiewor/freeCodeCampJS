# https://leetcode.com/problems/path-with-maximum-gold/description/?envType=daily-question&envId=2024-05-14

from typing import List

# with hashset
def getMaximumGold(grid: List[List[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    res = 0

    def dfs(r, c, vis):
        if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in vis or grid[r][c] == 0:
            return 0
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        vis.add((r, c))
        res = grid[r][c]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            res = max(res, grid[r][c] + dfs(nr, nc, vis))
        
        vis.remove((r, c))
        return res

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] != 0:
                res = max(res, dfs(r, c, set()))
    
    return res

# without hashset
def getMaximumGold(grid: List[List[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    res = 0

    def dfs(r, c):
        if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
            return 0
        res = 0
        tmp = grid[r][c]
        grid[r][c] = 0

        directions = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
        for nr, nc in directions:
            res = max(res, tmp + dfs(nr, nc))

        grid[r][c] = tmp
        return res

    for r in range(ROWS):
        for c in range(COLS):
            res = max(res, dfs(r, c))

    return res
        