# https://leetcode.com/problems/out-of-boundary-paths/?envType=daily-question&envId=2024-01-26

def findPaths(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    MOD = 10 ** 9 + 7
    cache = {}

    def helper(row, col, maxMove):
        if (row, col, maxMove) in cache:
            return cache[(row, col, maxMove)]
        
        if row < 0 or row >= m or col < 0 or col >= n:
            return 1
        
        if maxMove <= 0:
            return 0
        
        up = helper(row-1, col, maxMove - 1)
        down = helper(row+1, col, maxMove - 1)
        left = helper(row , col+1, maxMove - 1)
        right = helper(row , col-1, maxMove - 1)

        cache[(row, col, maxMove)] = (up + down + left + right) % MOD
        return cache[(row, col, maxMove)]
    
    return helper(startRow, startColumn, maxMove)

m = 2
n = 2
maxMove = 2
startRow = 0
startColumn = 0
print(findPaths(m, n, maxMove, startRow, startColumn))