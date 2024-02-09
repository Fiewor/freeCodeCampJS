# https://leetcode.com/problems/perfect-squares/?envType=daily-question&envId=2024-02-08

import sys

def numSquares(n: int) -> int:
    tab = [0] * (n+1)

    for i in range(1, n+1):
        min_val = sys.maxsize
        j = 1

        while j*j <= i:
            min_val = min(min_val, 1 + tab[i - j*j])
            j += 1
        
        tab[i] = min_val 

    return tab[n]

n = 13
print(numSquares(n))