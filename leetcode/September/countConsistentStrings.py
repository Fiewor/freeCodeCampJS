# https://leetcode.com/problems/count-the-number-of-consistent-strings/?envType=daily-question&envId=2024-09-12

from typing import List

def countConsistentStrings(allowed: str, words: List[str]) -> int:
    res = len(words)
    for word in words:
        for char in word:
            if char not in allowed:
                res -= 1
    return res

allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
print(countConsistentStrings(allowed, words))