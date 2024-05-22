# https://leetcode.com/problems/palindrome-partitioning/?envType=daily-question&envId=2024-05-22

from typing import List

def partition(s: str) -> List[List[str]]:
    def dfs(i:int, path:List[str]):
        if i >= len(s):
            res.append(path[:])
            return
        
        for j in range(i+1, len(s)+1):
            subStr = s[i:j]
            if subStr == subStr[::-1]:
                path.append(subStr)
                dfs(j, path)
                path.pop()

    res = []
    dfs(0, [])
    return res

print(partition(s = "aab"))