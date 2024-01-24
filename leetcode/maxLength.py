from collections import Counter
import sys
from typing import List

def maxLength(arr: List[str]) -> int:
    charset = set()

    def is_unique(s1, s2):
        count_map = Counter(s1) + Counter(s2)
        return max(count_map.values()) == 1 
    
    def helper(i):
        if i < 0: 
            return 0
        
        if i == len(arr):
            return len(charset)

        res = 0

        if is_unique(charset, arr[i]):
            for c in arr[i]:
                charset.add(c)

            res = helper(i+1)

            for c in arr[i]:
                charset.remove(c)

        return max(res, helper(i+1))

    n = len(arr)
    return helper(0)

# arr = ["un","iq","ue"]
arr = ["abc","def","bp","dq","eg","fh"]
# arr = ["abcdefghijklmnopqrstuvwxyz"]
print(maxLength(arr))