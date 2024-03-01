# https://leetcode.com/problems/maximum-odd-binary-number/?envType=daily-question&envId=2024-03-01

def maximumOddBinaryNumber(s: str) -> str:
    count = 0

    for char in s:
        if char == "1":
            count += 1
    
    return (count - 1)*"1" + (len(s) - count)*"0" + "1"

def maximumOddBinaryNumber(s: str) -> str:
    s = [c for c in s]

    left = 0

    for i in range(len(s)):
        if s[i] == "1":
            s[left], s[i] = s[i], s[left]
            left += 1
    
    s[left - 1], s[len(s) - 1] = s[len(s) - 1], s[left - 1]

    return "".join(s)

s = "010"
print(maximumOddBinaryNumber(s))