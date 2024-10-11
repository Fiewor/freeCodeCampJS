# https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/?envType=daily-question&envId=2024-10-11

import heapq
from typing import List

def smallestChair(times: List[List[int]], targetFriend: int) -> int:
    ind = [i for i in range(len(times))]
    ind.sort(key=lambda i:times[i][0]) #sort indices based on arrival time

    used_chairs = []
    available_chairs = [i for i in range(len(times))]

    for i in ind:
        a, l = times[i]

        while used_chairs and used_chairs[0][0] <= a:
            leave, chair = heapq.heappop(used_chairs)
            heapq.heappush(available_chairs, chair)
        
        chair = heapq.heappop(available_chairs)
        heapq.heappush(used_chairs, (l, chair))
        if i == targetFriend:
            return chair


times = [[3,10],[1,5],[2,6]]
targetFriend = 0
print(smallestChair(times, targetFriend))