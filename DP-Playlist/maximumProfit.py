# buy and sell stocks I -> one buy and one sell
def maximumProfit(prices):
    min_price = prices[0]
    max_profit = 0

    for i in range(len(prices)):
        max_profit = max(max_profit, prices[i] - min_price)
        min_price = min(min_price, prices[i])

    return max_profit

print(maximumProfit([7, 1, 5, 3, 6, 4]))