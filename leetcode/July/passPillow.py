# https://leetcode.com/problems/pass-the-pillow/description/?envType=daily-question&envId=2024-07-06

def passThePillow(n: int, time: int) -> int:
    rounds = time // (n-1)

    if rounds % 2:
        return n - time%(n-1)
    else:
        return 1 + time%(n-1)

n = 4
time = 5
print(passThePillow(n, time))