# https://leetcode.com/problems/power-of-two/?envType=daily-question&envId=2024-02-19

import math

# logarithmic approach
# 2⁰ = 1
# log₂1 = 0
def isPowerOfTwo(n: int) -> bool:
    print(math.log2(n))
    if n <= 0: return False
    return math.ceil(math.log2(n)) == math.floor(math.log2(n)) # checking if the log is an integer

# iterative approach
def isPowerOfTwo(self, n: int) -> bool:
    if n <= 0: return False
    while n != 1:
        if n % 2 != 0:
            return False
        n = n // 2
    return True

print(isPowerOfTwo(16))