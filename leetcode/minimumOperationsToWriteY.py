# https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/?envType=company&envId=capital-one&favoriteSlug=capital-one-thirty-days

from typing import List

def minimumOperationsToWriteY(grid: List[List[int]]) -> int:
    def try_(num_y, num_o):
        res = 0
        row = col = 0
        n = len(grid)

        for row in range(n):
            for col in range(n):
                if (row <= n//2 and (row == col or row+col == n-1)) or (row > n//2 and col == n//2):
                    if grid[row][col] != num_y:
                        res += 1
                else:
                    if grid[row][col] != num_o:
                        res += 1
        return res
    
    ans = min(try_(0, 1), try_(0, 2), try_(1, 0), try_(1, 2), try_(2, 0), try_(2, 1))

    return ans

grid = [[0,1,0,1,0],[2,1,0,1,2],[2,2,2,0,1],[2,2,2,2,2],[2,1,2,2,2]]
print(minimumOperationsToWriteY(grid))