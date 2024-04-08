# https://leetcode.com/problems/valid-parenthesis-string/description/?envType=daily-question&envId=2024-04-07

def checkValidString(s: str) -> bool:
    # DP Memoization solution
    n = len(s)
    cache = {}

    def dfs(i: int, left: int) -> bool:
        if i == n:
            return left == 0
        
        elif (i, left) in cache:
            return cache[(i, left)]
        
        elif left < 0:
            return False
        
        elif s[i] == '(':
            cache[(i, left)] = dfs(i+1, left+1)            
        
        elif s[i] == ')':
            cache[(i, left)] = dfs(i+1, left-1)

        else: # s[i] is '*'.
        # three choices for '*'
            one = dfs(i+1, left+1) # treat as '('
            two = dfs(i+1, left) # treat as '_' i.e. empty space
            three = dfs(i+1, left-1) # treat as ')'
        
            cache[(i, left)] = one or two or three
        
        return cache[(i, left)]
    
    return dfs(0, 0)

# linear solution
# time complexity -> O(n)
# space complexity -> O(1)
def checkValidString(s: str) -> bool:
    cmin, cmax = 0, 0

    for c in s:
        if c == '(':
            cmin += 1
            cmax += 1

        if c == '(':
            cmin -= 1
            cmax -= 1
        
        if c == '*':
            cmin -= 1
            cmax += 1
        
        if cmax < 0:
            return False
        
        if cmin < 0:
            cmin = 0
    
    return cmin == 0

# same as previous solution, except for maintaining cmin >= 0 within if statements
def checkValidString(s: str) -> bool:
    cmin, cmax = 0, 0

    for c in s:
        if c == '(':
            cmin += 1
            cmax += 1

        elif c == ')':
            cmin = max(cmin-1, 0)
            cmax += 1

        else: # c == '*'
            cmin = max(cmin-1, 0)
            cmax += 1
        
        if cmax < 0:
            return False
    
    return cmin == 0

s = "(*()))*("
print(checkValidString(s))