# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/?envType=daily-question&envId=2024-03-18

from typing import List

# decrement num when new overlapping interval is found
def findMinArrowShots(points: List[List[int]]) -> int:
    points.sort()
    num = len(points) # worstcase, you'll need at least n arrows
    prev = points[0]

    for i in range(1, len(points)):
        curr = points[i]

        if curr[0] <= prev[1]: #overlapping intervals!
            num -= 1
            prev = [curr[0], min(curr[1], prev[1])]
        else:
            prev = curr

    return num

# increment num (and interval end) when new non-overlapping interval is encountered
def findMinArrowShots(points: List[List[int]]) -> int:
    points.sort(key=lambda x:x[1]) #note the sort based on end
    num = 1
    _, currEnd = points[0]

    for i in range(1, len(points)):
        start, end = points[i]

        if start > currEnd:
            num += 1
            currEnd = end

    return num

points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
print(findMinArrowShots(points))
print(findMinArrowShots(points))