# https://leetcode.com/problems/longest-palindrome/description/?envType=daily-question&envId=2024-06-04

from collections import defaultdict


def longestPalindrome(s: str) -> int:
    res = 0
    count = defaultdict(int)

    for char in s:
        count[char] += 1
        if count[char] % 2 == 0:
            res += 2
    
    for char in count.values():
        if char % 2 == 1:
            res += 1
            break

    return res


def longestPalindrome(s: str) -> int:
    res = 0
    seen = set()

    for char in s:
        if char in seen:
            seen.remove(char)
            res += 2
        else:
            seen.add(char)
        

    return res+1 if len(seen) else res

print(longestPalindrome(s = "abccccdd"))