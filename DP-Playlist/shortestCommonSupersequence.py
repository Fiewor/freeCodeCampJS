def shortestSupersequence(a: str, b: str) -> str:
    # find lcs
    m, n = len(a), len(b)
    tab = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                tab[i][j] = 1 + tab[i - 1][j - 1]
            else:
                tab[i][j] = max(tab[i - 1][j], tab[i][j - 1])

    leng = tab[m][n]

    ans = ""

    i, j = m, n

    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            ans += a[i - 1]
            i -= 1
            j -= 1
        elif tab[i - 1][j] > tab[i][j - 1]:
            ans+= a[i - 1]
            i -= 1
        else:
            ans += b[j - 1]
            j -= 1
        
    while i > 0:
        ans += a[i - 1]
        i -= 1
     
    while j > 0:
        ans += b[j - 1]
        j -= 1
    
    return ans[::-1]
    

s1 = "brute"
s2 = "groot"

print(shortestSupersequence(s1, s2))