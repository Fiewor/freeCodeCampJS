# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/description/?envType=daily-question&envId=2024-08-03

from typing import List
from collections import Counter, defaultdict

def canBeEqual(target: List[int], arr: List[int]) -> bool:
    return Counter(target) == Counter(arr)

def canBeEqual(target: List[int], arr: List[int]) -> bool:
    count_target = Counter(target)
    count_arr = Counter(arr)

    for el in target:
        if count_target[el] != count_arr[el]:
            return False
    
    return True

# single hashmap
def canBeEqual(target: List[int], arr: List[int]) -> bool:
    count = defaultdict(int)

    for n1, n2 in zip(target, arr):
        count[n1] += 1
        count[n2] -= 1

    for n in count:
        if count[n] != 0:
            return False
    
    return True

target = [1,2,3,4]
arr = [2,4,1,3]
print(canBeEqual(target, arr))