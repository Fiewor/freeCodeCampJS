# https://leetcode.com/problems/maximum-score-from-removing-substrings/?envType=daily-question&envId=2024-07-12

def maximumGain(s: str, x: int, y: int) -> int:
    def remove_pairs(pair, score):
        nonlocal s
        re = 0
        stack = []
        for char in s:
            if char == pair[1] and stack and stack[-1] == pair[0]:
                re += score
                stack.pop()
            else:
                stack.append(char)
            s = "".join(stack)
        return re
        
    re = 0
    pair = "ab" if x > y else "ba"
    re += remove_pairs(pair, max(x, y))
    re += remove_pairs(pair[::-1], min(x, y))
    return re

s = "cdbcbbaaabab"
x = 4
y = 5
print(maximumGain(s, x, y))