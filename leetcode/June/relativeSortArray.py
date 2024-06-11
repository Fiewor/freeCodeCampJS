# https://leetcode.com/problems/relative-sort-array/description/?envType=daily-question&envId=2024-06-11

from collections import Counter
from typing import List

# using hashmap
def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        left = list(sorted([num for num in arr1 if num not in arr2]))
        count = Counter(arr1)

        for num in arr2:
            for _ in range(count[num]):
                res.append(num)
        
        return res + left

# using counting sort
def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
    res = []
    count = [0] * 1001

    for el in arr1:
        count[el] += 1

    for el in arr2:
        while count[el]:
            res.append(el)
            count[el] -= 1

    for i, el in enumerate(count):
        while el:
            res.append(i)
            el -= 1
    
    return res

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

print(relativeSortArray(arr1, arr2))