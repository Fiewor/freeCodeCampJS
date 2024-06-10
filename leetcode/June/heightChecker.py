# https://leetcode.com/problems/height-checker/?envType=daily-question&envId=2024-06-10

from typing import List

# using built-in sort
def heightChecker(heights: List[int]) -> int:
    res = 0
    expected = sorted(heights)

    for i in range(len(heights)):
        if heights[i] != expected[i]:
            res += 1

    return res

# using count sort
def heightChecker(heights: List[int]) -> int:
    res = 0
    expected = []
    count = [0] * 101

    for height in heights:
        count[height] += 1
    
    for i in range(1, 101):
        if count[i]:
            for _ in range(count[i]):
                expected.append(i)

    for i in range(len(heights)):
        if heights[i] != expected[i]:
            res += 1

    return res

heights = [1,1,4,2,1,3]
print(heightChecker(heights))
