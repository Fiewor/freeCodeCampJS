# https://leetcode.com/problems/spiral-matrix-iii/description/?envType=daily-question&envId=2024-08-08

from typing import List

def spiralMatrixIII(rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
    res = []
    step = 1
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    i = 0
    r, c = rStart, cStart
    
    while len(res) < (rows*cols):
        for _ in range(2): # move step times, twice. R - 1, D - 1, L - 2, U - 2
            dr, dc = directions[i]
            for _ in range(step):
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
                r, c = r + dr, c + dc
            i = (i+1) % 4 # in order to stay inbounds
        step += 1

    return res

rows = 5
cols = 6
rStart = 1
cStart = 4
print(spiralMatrixIII(rows, cols, rStart, cStart))