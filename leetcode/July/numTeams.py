# https://leetcode.com/problems/count-number-of-teams/?envType=daily-question&envId=2024-07-29

from typing import List

# math
def numTeams(rating: List[int]) -> int:
    re = 0

    for m in range(1, len(rating)-1):
        left_smaller = 0
        for i in range(m):
            if rating[i] < rating[m]: left_smaller += 1
        left_larger = m - left_smaller

        right_smaller = 0
        for i in range(m+1, len(rating)):
            if rating[i] < rating[m]: right_smaller += 1
        right_larger = len(rating) - m  - 1 - right_smaller

        re += left_smaller * right_larger
        re += left_larger * right_smaller
    
    return re
        

# memoization
def numTeams(rating: List[int]) -> int:
    cache = {}

    def backtrack(i, ascend, count):
        if (i, ascend, count) in cache:
            return cache[(i, ascend, count)]
        if count == 3:
            return 1
        if i == len(rating):
            return 0
        
        re = 0
        for j in range(i+1, len(rating)):
            if ascend and rating[j] > rating[i]:
                re += backtrack(j, ascend, count+1)
            if not ascend and rating[j] < rating[i]:
                re += backtrack(j, ascend, count+1)
        cache[(i, ascend, count)] = re
        return re

    re = 0
    for i in range(len(rating)):
        re += backtrack(i, True, 1)
        re += backtrack(i, False, 1)
    return re

rating = [1,2,3,4]
print(numTeams(rating))