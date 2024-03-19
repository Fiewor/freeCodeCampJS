# https://leetcode.com/problems/task-scheduler/?envType=daily-question&envId=2024-03-19

from collections import Counter, deque
import heapq
from typing import List

def leastInterval(tasks: List[str], n: int) -> int:
    time = 0
    count = Counter(tasks)
    maxHeap = [-c for c in count.values()]
    heapq.heapify(maxHeap)
    q = deque() # [-c, idleTime]
    
    while maxHeap or q:
        time += 1

        if maxHeap:
            cnt = 1 + heapq.heappop(maxHeap)
            if cnt:
                q.append([cnt, time + n])
        
        if q and q[0][1] == time:
            heapq.heappush(maxHeap, q.popleft()[0])

    return time

tasks = ["A","A","A","B","B","B"]
n = 2
print(leastInterval(tasks, n))