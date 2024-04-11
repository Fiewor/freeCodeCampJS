# https://leetcode.com/problems/remove-k-digits/?envType=daily-question&envId=2024-04-11

def removeKdigits(num: str, k: int) -> str:
    stack = []

    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        
        stack.append(digit)
    
    stack = stack[:-k] if k > 0 else stack

    res = "".join(stack).lstrip('0')

    return res if res else '0'

num = "1432219"
k = 3
print(removeKdigits(num, k))
