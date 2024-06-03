# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/?envType=daily-question&envId=2024-06-03

def appendCharacters(s: str, t: str) -> int:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1
        
        return len(t) - j

s = "z"
t = "abcde"
print(appendCharacters(s, t))
