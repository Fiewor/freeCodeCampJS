# https://leetcode.com/problems/open-the-lock/?envType=daily-question&envId=2024-04-22

from collections import deque
from typing import List

def openLock(deadends: List[str], target: str) -> int:
    if '0000' in deadends:
        return -1
    
    def children(lock: str):
        res = []
        n = len(lock)

        for i in range(n):
            digit = str((int(lock[i]) + 1) % 10)
            res.append(lock[:i] + digit + lock[i+1:])

            digit = str((int(lock[i]) - 1 + 10) % 10)
            res.append(lock[:i] + digit + lock[i+1:])

        return res
    
    q = deque()
    q.append(('0000', 0))
    vis = set(deadends)

    while q:
        lock, turns = q.popleft()

        if lock == target:
            return turns
        
        for child in children(lock):
            if child not in vis:
                vis.add(child)
                q.append((child, turns + 1))
    
    return -1

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
print(openLock(deadends, target))