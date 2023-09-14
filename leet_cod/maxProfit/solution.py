def maxProfit(prices: list[int]) -> int:
    max_profit = 0
    min_price = prices[0]

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit
print(maxProfit([7,1,5,3,6,4]))