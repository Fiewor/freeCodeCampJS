# buy and sell stocks III -> max 2 transactions
def f(ind: int, buy: int, cap: int, values: list[int], n: int, memo): # cap is max number of transactions
    # 1 -> buy
    # 0 -> sell
    if n == 0 or cap == 0:
        return 0
    # ind - 0 to n - 1
    # buy - 2 i.e. 0 or 1
    # cap - 3 i.e. 0, 1, 2
    # memo[N][2][3]
    if (ind, buy, cap) in memo:
        return memo[(ind, buy, cap)]

    profit = 0
    if buy == 1:
        buyCurrent = f(ind + 1, 0, cap, values, n, memo) - values[ind]
        notBuyCurrent = f(ind + 1, 1, cap, values, n, memo)
        profit = max(buyCurrent, notBuyCurrent)        
    else:
        sellCurrent = f(ind + 1, 1, cap - 1, values, n, memo) # cap reduces because you've now performed one complete buy/sell transaction
        notSellCurrent = f(ind + 1, 0, cap, values, n, memo)
        profit = max(sellCurrent, notSellCurrent)
    
    memo[(ind, buy, cap)] = profit
    return memo[(ind, buy, cap)]

# memoization
# Time Complexity -> O(N x 2 x 3) -> O(N)
# Space Complexity -> O(N)
def maxProfit(values: list[int], n: int)-> int:
    memo = {}
    return f(0, 1, 2, values, n, memo)

def maxProfitTab(values: list[int], n: int)-> int:
    # initialize 3D array for 3 changing parameters - index, buy and cap
    # vector<vector<vector<int>>> dp(n, vector<vector<int>> (2, vector<int> (3, 0)))
    tab = [[[0] * (3) for _ in range(2)] for _ in range(n + 1)]
    
    #! handle base cases <- not needed because array is already initialized with 0
    # # if cap === 0, n and buy can have all other ranges of values
    # # n: 0 -> n - 1
    # # buy: 0 -> 2 i.e. 0 or 1
    # for ind in range(n + 1):
    #     for buy in range(2):
    #         tab[ind][buy][0] = 0
    
    # # if n == 0, cap and buy can have their range of values
    # # cap: 0 -> 3 i.e. 0, 1, 2
    # # buy: 0 -> 2 i.e. 0, 1

    # for cap in range(3):
    #     for buy in range(2):
    #         tab[0][buy][cap] = 0
    
    # populate tab i.e. explore all possibilities
    for ind in range(n - 1, -1, -1):
        for buy in range(2):
            for cap in range(1, 3):
                profit = 0
                if buy == 1:
                    buyCurrent = tab[ind + 1][buy][cap] - values[ind]
                    notBuyCurrent = tab[ind + 1][buy][cap]
                    tab[ind][buy][cap] = max(buyCurrent, notBuyCurrent)        
                else:
                    sellCurrent = tab[ind + 1][buy][cap - 1]
                    notSellCurrent = tab[ind + 1][buy][cap]
                    tab[ind][buy][cap] = max(sellCurrent, notSellCurrent)
    
    return tab[0][1][2]

# Time Complexity - O(N x 2 x 3)
# Space Complexity - O(6) ~ O(1) #basically constant space
def maxProfitSpaceOp(values: list[int], n: int)-> int:
    # use 2D instead
    after = curr = [[0] * (3) for _ in range(2)]
    
    for ind in range(n - 1, -1, -1):
        for buy in range(2):
            for cap in range(1, 3):
                if buy == 1:
                    buyCurrent = after[0][cap] - values[ind]
                    notBuyCurrent = after[1][cap]
                    curr[buy][cap] = max(buyCurrent, notBuyCurrent)        
                else:
                    sellCurrent = after[1][cap - 1]
                    notSellCurrent = after[0][cap]
                    curr[buy][cap] = max(sellCurrent, notSellCurrent)
        
        after = curr  
    
    return after[1][2]


values = [3, 3, 5, 0, 0, 3, 1, 4]
print(maxProfit(values, len(values)))
print(maxProfitTab(values, len(values)))
print(maxProfitSpaceOp(values, len(values)))