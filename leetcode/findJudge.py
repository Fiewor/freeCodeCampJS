# https://leetcode.com/problems/find-the-town-judge/?envType=daily-question&envId=2024-02-22

from collections import defaultdict

def findJudge(n: int, trust: list[list[int]]) -> int:
    incoming = defaultdict(int)
    outgoing = defaultdict(int)
    for source_node, destination_node in trust:
        outgoing[source_node] += 1
        incoming[destination_node] += 1
    
    for i in range(1, n+1):
        if incoming[i] == n-1 and outgoing[i] == 0:
            return i
    return -1

def findJudge(self, n: int, trust: list[list[int]]) -> int:
    delta = defaultdict(int)
    for source_node, destination_node in trust:
        delta[source_node] -= 1
        delta[destination_node] += 1

    for i in range(1, n+1):
        if delta[i] == n-1:
            return i
    return -1

n = 2
trust = [[1,2]]
# incoming    outgoing
# 1 -> 0       1 -> 1
# 2 -> 1       2 -> 0
print(findJudge(n, trust))