# subsequence
# order must be maintained
# you're allowed to jump characters i.e. it musn't necessarily be contiguous


# ------ recursion ------

def f(s1: str, s2: str, i: int, j: int) -> int:
    if i < 0 or j < 0:
        return 0
    if s1[i] == s2[j]: # match
        return 1 + f(s1, s2, i - 1, j - 1)
    else: # no match
        return max(f(s1, s2, i - 1, j), f(s1, s2, i, j - 1))

def lcs(s: str, t: str) -> int:
    return f(s, t, len(s) - 1, len(t) - 1)


# ------ memoization ------

def fMemo(s1: str, s2: str, i: int, j: int, memo: dict[(int, int): int]) -> int:
    if i < 0 or j < 0:
        return 0
    
    if (i, j) in memo:
        return memo[(i, j)]
    
    if s1[i] == s2[j]: # match
        memo[(i, j)] = 1 + fMemo(s1, s2, i - 1, j - 1, memo)
    else:
        memo[(i, j)] = max(fMemo(s1, s2, i - 1, j, memo), fMemo(s1, s2, i, j - 1, memo))

    return memo[(i, j)]

def lcsMemo(s: str, t: str) -> int:
    memo = {}
    return fMemo(s, t, len(s) -1, len(t) -1, memo)


def lcsTab(s: str, t: str) -> int:
    m, n = len(s), len(t)
    tab = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(m + 1):
        tab[i][0] = 0
    
    for i in range(n + 1):
        tab[0][i] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]: 
                tab[i][j] = 1 + tab[i - 1][j - 1]
            else:
                tab[i][j] = max(tab[i - 1][j], tab[i][j - 1])

    return tab[m - 1][n - 1]


print(f'recursion: {lcs("adebc", "dcadb")}')
print(f'memo: {lcsMemo("adebc", "dcadb")}')
print(f'tabulation: {lcsTab("adebc", "dcadb")}')
# print(f'space-optimization: {lcsSpaceOp("adebc", "dcadb")}')