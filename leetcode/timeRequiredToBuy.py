# https://leetcode.com/problems/time-needed-to-buy-tickets/?envType=daily-question&envId=2024-04-09

from typing import List

def timeRequiredToBuy(tickets: List[int], k: int) -> int:
    time = 0

    while True:
        for i in range(len(tickets)):
            if tickets[i] > 0:
                time += 1
                tickets[i] -= 1

            if i == k and tickets[i] == 0:
                return time
            
# one-pass
# time complexity - O(n)
# space complexity - O(1)
def timeRequiredToBuy(tickets: List[int], k: int) -> int:
    res = 0

    for i in range(len(tickets)):
        if i <= k:
            res += min(tickets[i], tickets[k])
        else:
            res += min(tickets[i], tickets[k]-1)
    return res

            
tickets = [5,1,1,1]
k = 0
print(timeRequiredToBuy(tickets, k))