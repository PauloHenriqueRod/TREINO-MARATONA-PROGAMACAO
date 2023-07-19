def robber(nums: list[int]) -> int:
    i = 3
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    if n == 3:
        return max(nums[1], nums[0] + nums[2])
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = nums[1]
    dp[2] = dp[0] + nums[2]
    while i < n:
        dp[i] = nums[i] + max(dp[i-2], dp[i-3])
        i+=1
    return max(dp[-1], dp[-2])

print(robber([4,1,2,7,5,3,1]))