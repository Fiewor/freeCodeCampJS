def f(i: int, j: int, s1: str, s2: str) -> int: 
    if j == 0: # end of s2 means all characters have been found
        return 1
    if i == 0: # end of s1, but characters still remain unfound in s2
        return 0
    if s1[i - 1] == s2[j - 1]:
        pick = f(i - 1, j - 1, s1, s2)
        notPick = f(i - 1, j, s1, s2) # don't take current character, reduce s1 search range 
        return pick + notPick
    else:
        return f(i - 1, j, s1, s2)

def numDistinct(s1: str, s2: str) -> int:
    return f(len(s1), len(s2), s1, s2)

def fMemo(i: int, j: int, s1: str, s2: str, memo) -> int: 
    if j == 0:
        return 1
    
    if i == 0:
        return 0
    
    if (i, j) in memo:
        return memo[(i, j)]
    
    if s1[i - 1] == s2[j - 1]:
        pick = fMemo(i - 1, j - 1, s1, s2, memo)
        notPick = fMemo(i - 1, j, s1, s2, memo)
        memo[(i, j)] = pick + notPick
    else:
        memo[(i, j)] = fMemo(i - 1, j, s1, s2, memo)
    
    return memo[(i, j)]

def numDistinctMemo(s1: str, s2: str) -> int:
    memo = {}
    return fMemo(len(s1), len(s2), s1, s2, memo)
    
def numDistinctTab(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)

    tab = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        tab[i][0] = 1
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                pick = tab[i - 1][j - 1]
                notPick = tab[i - 1][j]

                tab[i][j] = pick + notPick
            else:
                tab[i][j] = tab[i - 1][j]
            
    return tab[m][n]

def numDistinctSpaceOp(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)

    prev = curr = [0] * (m + 1)

    prev[0] = 1
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                pick = prev[j - 1]
                notPick = prev[j]

                curr[j] = pick + notPick
            else:
                curr[j] = prev[j]
        prev = curr
            
    return prev[n]

def numDistinctSpaceOp1D(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)

    prev = [0] * (m + 1)

    prev[0] = 1
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                pick = prev[j - 1]
                notPick = prev[j]

                prev[j] = pick + notPick
            
    return prev[n]

s1 = "babgbag"
s2 = "bag"
print(f"recursion: {numDistinct(s1, s2)}")
print(f"memo: {numDistinctMemo(s1, s2)}")
print(f"tab: {numDistinctTab(s1, s2)}")
print(f"space-op: {numDistinctSpaceOp(s1, s2)}")
print(f"space-op 1D: {numDistinctSpaceOp1D(s1, s2)}")