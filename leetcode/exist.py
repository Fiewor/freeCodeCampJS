# https://leetcode.com/problems/word-search/?envType=daily-question&envId=2024-04-03

from typing import List

def exist(board: List[List[str]], word: str) -> bool:
    ROWS, COLUMNS = len(board), len(board[0])
    path = set()

    def dfs(r, c, k):
        if k == len(word):
            return True
        
        if r < 0 or c < 0 or r >= ROWS or c >= COLUMNS or word[k] != board[r][c] or (r, c) in path:
            return False
        

        path.add((r, c))

        res = dfs(r+1, c, k+1) or dfs(r-1, c, k+1) or dfs(r, c+1, k+1) or dfs(r, c-1, k+1)
        
        path.remove((r, c))

        return res

    for r in range(ROWS):
        for c in range(COLUMNS):
            if dfs(r, c, 0):
                return True
    
    return False
