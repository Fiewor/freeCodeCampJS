# https://leetcode.com/problems/number-of-islands/


from collections import deque
from typing import List

def numIslands(self, grid: List[List[str]]) -> int:
    count = 0
    ROWS, COLS = len(grid), len(grid[0])
    vis = set()

    def dfs(r, c):
        q = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q.append((r, c))

        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == '1' and (nr, nc) not in vis:
                    vis.add((nr, nc))
                    q.append((nr, nc))

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == '1' and (r, c) not in vis:
                count += 1
                dfs(r, c)

    return count