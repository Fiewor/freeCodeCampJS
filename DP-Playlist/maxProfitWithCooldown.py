def f(ind: int, buy: int, values: list[int], n: int, memo):
    if ind >= n:
        return 0
    
    if (ind, buy) in memo:
        return memo[(ind, buy)]
    
    profit = 0

    if buy == 1:
        buyCurrent = f(ind+1, 0, values, n, memo) - values[ind]
        notBuyCurrent = f(ind+1, 1, values, n, memo)
        profit = max(buyCurrent, notBuyCurrent)
    else:
        sellCurrent = f(ind+2, 1, values, n, memo) + values[ind] # now ind + 2, because you can't buy right after selling
        notSellCurrent = f(ind+1, 0, values, n, memo)
        profit = max(sellCurrent, notSellCurrent)
    
    memo[(ind, buy)] = profit
    return memo[(ind, buy)]

def maxProfit(values: list[int], n: int) -> int:
    memo = {}
    return f(0, 1, values, n, memo)

def maxProfitTab1(values: list[int], n: int) -> int:
    tab = [[0] * 2 for _ in range(n + 1)]

    for ind in range(n - 1, -1, -1):
            for buy in range(2):
                if buy == 1:
                    buyCurrent = tab[ind+1][0] - values[ind]
                    notBuyCurrent = tab[ind+1][1]
                    tab[ind][buy] = max(buyCurrent, notBuyCurrent)
                else:
                    sellCurrent = tab[ind+2][1] + values[ind]
                    notSellCurrent = tab[ind+1][0]
                    tab[ind][buy] = max(sellCurrent, notSellCurrent)
            
    return tab[0][1]

def maxProfitTab2(values: list[int], n: int) -> int:
    tab = [[0] * 2 for _ in range(n + 1)]

    for ind in range(n - 1, -1, -1):
        buyCurrent = tab[ind + 1][0] - values[ind]
        notBuyCurrent = tab[ind + 1][1]
        tab[ind][1] = max(buyCurrent, notBuyCurrent) # buy case
        
        sellCurrent = tab[ind + 2][1] + values[ind]
        notSellCurrent = tab[ind + 1][0]
        tab[ind][0] = max(sellCurrent, notSellCurrent) # sell case
            
    return tab[0][1]

def maxProfitSpaceOp(values: list[int], n: int) -> int:
    front1 = front2 = curr = [0] * 2

    for ind in range(n - 1, -1, -1):
        buyCurrent = front1[0] - values[ind]
        notBuyCurrent = front1[1]
        curr[1] = max(buyCurrent, notBuyCurrent) # buy case
        
        sellCurrent = front2[1] + values[ind]
        notSellCurrent = front1[0]
        curr[0] = max(sellCurrent, notSellCurrent) # sell case
    
    front2 = front1
    front1 = curr
            
    return curr[1]

print(maxProfit([7, 1, 5, 3, 6, 4], 6))
print(maxProfitTab1([7, 1, 5, 3, 6, 4], 6))
print(maxProfitTab2([7, 1, 5, 3, 6, 4], 6))
print(maxProfitSpaceOp([7, 1, 5, 3, 6, 4], 6))