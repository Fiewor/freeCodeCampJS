# https://leetcode.com/problems/insert-interval/?envType=daily-question&envId=2024-03-17

from typing import List

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    res = []

    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
    
    res.append(newInterval)

    return res

intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(insert(intervals, newInterval))