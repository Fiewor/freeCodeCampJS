# https://leetcode.com/problems/sequential-digits/submissions/1163867351/?envType=daily-question&envId=2024-02-02

from collections import deque
from typing import List

def sequentialDigits(low: int, high: int) -> List[int]:
    low_dig, high_dig = len(str(low)), len(str(high))
    res = []

    for digits in range(low_dig, high_dig + 1):
        for start in range(1, 9):
            if start + digits > 10:
                break
            num = prev = start

            for i in range(digits-1):
                num *= 10
                prev += 1
                num += prev

            if low <= num <= high:
                res.append(num)

    return res

def sequentialDigits(low: int, high: int) -> List[int]:
    res = []
    queue = deque(range(1, 10))

    while queue:
        n = queue.popleft()

        if n > high:
            continue

        if low <= n <= high:
            res.append(n)

        ones = n % 10
        if ones < 9:
           queue.append((n*10) + (ones+1)) 

    return res

low, high = 100, 300
print(sequentialDigits(low, high))