def maxProfit(prices: list[int]) -> int:
    if not prices:
        return 0
    
    max_profit = 0
    min_price = prices[0]

    for price in prices:
        print(min_price)
        print(max_profit)
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit
print(maxProfit([7,1,5,3,6,4]))