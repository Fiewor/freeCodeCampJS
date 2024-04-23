from collections import deque

def orangesRotting(grid):
    time = 0
    ROWS, COLS = len(grid), len(grid[0])
    vis = [[0] * COLS for _ in range(ROWS)]
    count_fresh = 0
    q = deque()

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 2:
                vis[r][c] = 2
                q.append(((r, c), 0)) #((row, col), time)
            
            if grid[r][c] == 1:
                count_fresh += 1

    max_time = 0
    count = 0

    while q:
        (row, col), time = q.popleft()
        max_time = max(max_time, time)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        for dr, dc in directions:
            nr, nc = row + dr, col + dc

            if 0 <= nr < ROWS and 0 <= nc < COLS and vis[nr][nc] != 2 and grid[nr][nc] == 1:
                q.append(((nr, nc), time + 1))
                vis[nr][nc] = 2
                count += 1

    if count != count_fresh:
        return -1  

    return max_time

grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
print(orangesRotting(grid))