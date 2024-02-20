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
def isPowerOfTwo(n: int) -> bool:
    if n <= 0: return False
    while n != 1:
        if n % 2 != 0:
            return False
        n = n // 2
    return True

# loop
def isPowerOfTwo(n: int) -> bool:
    k = 1
    while k < n:
        k *= 2
    
    return k == n

# bitwise approach
def isPowerOfTwo(n: int) -> bool:
    return n > 0 and (n & (n - 1) == 0) 

# math approach
def isPowerOfTwo(n: int) -> bool:
    return n > 0 and math.ceil(2**30 % n) == 0 # dividing n by a number larger than n that's also a power of 2 (we use the largest power of 2)
    # return n > 0 and math.ceil((1 << 30) % n) == 0 #using bitwise shifting cause 1 = 2⁰, so shifting 1 to the left (bitwise) 30 times results in 2^30

print(isPowerOfTwo(16))