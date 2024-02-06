# https://leetcode.com/problems/minimum-window-substring/?envType=daily-question&envId=2024-02-04

from collections import Counter
import sys

def minWindow(s: str, t: str) -> str:
    if t == "" or len(t) > len(s):
        return ""
    
    t_count = Counter(t)
    need = len(t_count.keys())
    min_len = sys.maxsize
    min_window = ""
    i = 0

    for j, char in enumerate(s):
        if char in t_count:
            t_count[char] -= 1

            if t_count[char] == 0:
                need -= 1

        while need == 0:
            if j - i + 1 < min_len:
                min_len = j - i + 1
                min_window = s[i : j+1]

            if s[i] in t_count:
                t_count[s[i]] += 1

                if t_count[s[i]] > 0:
                    need += 1

            i += 1

    return min_window

s, t = "ADOBECODEBANC", "ABC"
print(minWindow(s, t))