# https://leetcode.com/problems/make-the-string-great/?envType=daily-question&envId=2024-04-05

def makeGood(s: str) -> str:
    def lower(char):
        if ord(char) < ord('a'):
            return chr(ord('a') + ord(char) - ord('A'))
        else:
            return char


    stack = []
    i = 0

    while i < len(s):
        if stack and stack[-1] != s[i] and lower(stack[-1]) == lower(s[i]): #or just use .lower()
            stack.pop()
        else:
            stack.append(s[i])

        i += 1

    return "".join(stack)

s = "leEeetcode"
print(makeGood(s))