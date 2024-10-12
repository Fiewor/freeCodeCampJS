# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description/

from typing import List

def minGroups(intervals: List[List[int]]) -> int:
    start = [x[0] for x in intervals]
    end = [x[1] for x in intervals]

    start.sort()
    end.sort()

    l = r = 0
    res = 0
    groups = 0

    while l < len(intervals):
        if start[l] <= end[r]:
            groups += 1
            l += 1
        else:
            groups -= 1
            r += 1
        res = max(res, groups)
    
    return res

intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
print(minGroups(intervals))