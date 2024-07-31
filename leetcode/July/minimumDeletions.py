# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/description/?envType=daily-question&envId=2024-07-30

from collections import defaultdict

def minimumDeletions(s: str) -> int:
    a_count_right = [0] * len(s)

    for i in range(len(s)-2, -1, -1):
        a_count_right[i] = a_count_right[i+1]
        if s[i] == 'a':
            a_count_right[i] += 1
    
    re = len(s)
    b_count_left = 0
    for i, char in enumerate(s):
        if char == 'a':
            a_count_right[i] -= 1
        re = min(re, b_count_left + a_count_right[i])
        if char == 'b':
            b_count_left += 1
    
    return re

# slightly optimized
def minimumDeletions(s: str) -> int:
    a_count_right = 0

    for char in s:
        if char == 'a': a_count_right += 1
    
    re = len(s)
    b_count_left = 0
    for char in s:
        if char == 'a':
            a_count_right -= 1
        re = min(re, b_count_left + a_count_right)
        if char == 'b':
            b_count_left += 1
    
    return re

print(minimumDeletions(s="aababbab"))