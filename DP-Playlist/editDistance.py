def f(i: int, j: int, s1: str, s2: str, memo):
    if i == 0: # end of str1, return length of s2 (that gives the number of elements you need to insert)
        return j
    
    if j == 0: # end of s2, return length of s2 (that gives the number of elements you need to delete)
        return i
    
    if s1[i - 1] == s2[j - 1]: # match, so continue
        return f(i - 1, j - 1, s1, s2, memo)
    
    if (i, j) in memo:
        return memo[(i, j)]
    
    ins = f(i, j - 1, s1, s2, memo) #insert (satisfied one character in s2, so reduce j i.e. range of s2)
    dele =  f(i - 1, j, s1, s2, memo) #delete (one less character in s1, but still same character in s2, so only reduce range of s1)
    repl =  f(i - 1, j - 1, s1, s2, memo) #replace (reduce search range of both s1 and s2)

    memo[(i, j)] = 1 + min(ins, dele, repl)
 
    return memo[(i, j)]

def editDistance(s1: str, s2: str) -> int:
    memo = {}
    # return min number of operations to convert s1 to s2
    return f(len(s1), len(s2), s1, s2, memo)

def editDistanceTab(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)

    tab = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        tab[i][0] = i

    for i in range(n + 1):
        tab[0][i] = i

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]: # match, so continue
                tab[i][j] = tab[i - 1][j - 1]
            else:
                ins = tab[i][j - 1] #insert
                dele = tab[i - 1][j] #delete
                repl = tab[i - 1][j - 1] #replace

                tab[i][j] = 1 + min(ins, dele, repl)
        
    return tab[m][n]

def editDistanceSpaceOp(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)

    prev = curr = [0] * (n + 1)

    for i in range(n + 1):
        prev[i] = i

    for i in range(1, m + 1):
        curr[0] = i
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]: # match, so continue
                curr[j] = prev[j - 1]
            else:
                ins = curr[j - 1] #insert
                dele = prev[j] #delete
                repl = prev[j - 1] #replace

                curr[j] = 1 + min(ins, dele, repl)
        prev = curr
        
    return prev[n]


print(editDistance("horse", "ros"))
print(editDistanceTab("horse", "ros"))
print(editDistanceSpaceOp("horse", "ros"))