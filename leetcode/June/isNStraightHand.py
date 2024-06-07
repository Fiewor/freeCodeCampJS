# https://leetcode.com/problems/hand-of-straights/?envType=daily-question&envId=2024-06-06

from collections import Counter
import heapq
from typing import List

def isNStraightHand(hand: List[int], groupSize: int) -> bool:
    if len(hand) % groupSize:
        return False

    count = Counter(hand)
    minHeap = list(count.keys())
    heapq.heapify(minHeap)

    while minHeap:
        first = minHeap[0]
        for i in range(first, first+groupSize):
            if i not in count:
                return False
            count[i] -= 1

            if count[i] == 0:
                if i != minHeap[0]:
                    return False
                heapq.heappop(minHeap)  
    
    return True

hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
print(isNStraightHand(hand, groupSize))