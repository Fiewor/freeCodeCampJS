# https://leetcode.com/problems/determine-if-string-halves-are-alike/description/?envType=daily-question&envId=2024-01-12

def halvesAreAlike(self, s: str) -> bool:
    i, j, vowels = 0, len(s) - 1, "aeiouAEIOU"
    c1 = c2 = 0

    while i < j:
        if s[i] in vowels:
            c1 += 1

        if s[j] in vowels:
            c2 += 1
        
        i += 1
        j -= 1
        
    return c1 == c2