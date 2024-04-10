# https://leetcode.com/problems/reveal-cards-in-increasing-order/?envType=daily-question&envId=2024-04-10

from collections import deque
from typing import List

# time complexity - O(nlogn) from sorting
# space complexity - O(n) from queue
def deckRevealedIncreasing(deck: List[int]) -> List[int]:
    deck.sort()
    res = [0] * len(deck)
    q = deque(range(len(deck)))

    for card in deck:
        ind = q.popleft()
        res[ind] = card

        if q:
            q.append(q.popleft())
    
    return res

# test case
deck = [17,13,11,2,3,5,7]
print(deckRevealedIncreasing(deck))
