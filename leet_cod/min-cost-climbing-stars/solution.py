def solve(cost: list[int]) -> int:
    dp = [0 for i in range(len(cost))]
    dp[0] = cost[0]
    if len(cost) >= 2:
        dp[1] = cost[1]
    for i in range(2, len(cost)):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    return min(dp(len(cost)-1), dp(len(cost)-2))