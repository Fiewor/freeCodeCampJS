# https://leetcode.com/problems/sum-of-square-numbers/description/?envType=daily-question&envId=2024-06-17

from math import sqrt


def judgeSquareSum(c: int) -> bool:
    sqrr = set()

    for i in range(int(sqrt(c))+1):
        sqrr.add(i*i)
    
    a = 0
    while a * a < c:
        target = c - a * a
        if target in sqrr:
            return True
        a += 1

    return False

# more space optimized
def judgeSquareSum(c: int) -> bool:
    l, r = 0, len(c)

    while l <= r:
        total = l*l + r*r
        if total > c:
            r -= 1
        elif total < c:
            l += 1
        else:
            return True

    return False

c=8
print(judgeSquareSum(c))