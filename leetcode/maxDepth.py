# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/?envType=daily-question&envId=2024-04-04

def maxDepth(s: str) -> int:
    res, count = 0, 0

    for char in s:
        if char == '(':
            count += 1
        if char == ')':
            count -= 1
        res = max(res, count)

    return res

s = "(1+(2*3)+((8)/4))+1"
print(maxDepth(s))