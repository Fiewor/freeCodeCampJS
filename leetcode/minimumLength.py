# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/?envType=daily-question&envId=2024-03-05

from collections import deque

# two-pointer approach
def minimumLength(s: str) -> int:
    l, r = 0, len(s) - 1

    while l < r and s[l] == s[r]:
        curr = s[l]

        while l <= r and s[l] == curr:
            l += 1

        while r >= l and s[r] == curr:
            r -= 1

    return r - l + 1
    
# double-ended queue approach
def minimumLength(s: str) -> int:
    q = deque(s)

    while len(q) > 1 and q[0] == q[-1]:
        curr = q[0]
        
        while len(q) > 0 and q[0] == curr:
            q.popleft()
    
        while len(q) > 0 and q[-1] == curr:
            q.pop()
   
    return len(q)


s = "aabccabba"
print(minimumLength(s))
