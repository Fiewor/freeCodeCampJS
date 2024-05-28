# https://leetcode.com/problems/get-equal-substrings-within-budget/description/?envType=daily-question&envId=2024-05-28

def equalSubstring(s: str, t: str, maxCost: int) -> int:
    l = 0
    cost = 0
    currMax = float('-inf')

    for r in range(len(s)):
        cost += abs(ord(s[r]) - ord(t[r]))

        while cost > maxCost:
            cost -= abs(ord(s[l]) - ord(t[l]))
            l += 1
        
        currMax = max(currMax, cost)
    
    return currMax

s = "abcd"
t = "bcdf"
maxCost = 3
print(equalSubstring(s, t, maxCost))