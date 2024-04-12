# https://leetcode.com/problems/trapping-rain-water/submissions/1230592448/?envType=daily-question&envId=2024-04-12

from typing import List

# time complexity - O(n)
# space complexity - O(n)
def trap(height: List[int]) -> int:
    n = le(height)
    leftMax = [0] * n
    leftMax[0] = height[0]

    rightMax = [0] * n
    rightMax[n-1] = height[n-1]

    res = 0

    for i in range(1, n):
        leftMax[i] = max(height[i], leftMax[i-1])
    
    for i in range(n-2, -1, -1):
        rightMax[i] = max(height[i], rightMax[i+1])

    for i in range(n)    :
        water = min(leftMax[i], rightMax[i])
        res += water - height[i]

    return res


# time complexity - O(n)
# space complexity - O(1)
def trap(height: List[int]) -> int:
    n = len(height)
    l, r = 0, n - 1
    lMax, rMax = height[l], height[r]
    res = 0

    while l < r:
        if lMax < rMax:
            l += 1
            lMax = max(lMax, height[l])
            res += lMax - height[l]
        else:
            r -= 1
            rMax = max(rMax, height[r])
            res += rMax - height[r]
    
    return res
