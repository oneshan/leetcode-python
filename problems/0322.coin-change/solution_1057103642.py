# 0322 - Coin Change
# Date: 2023-09-23
# Runtime: 815 ms, Memory: 16.5 MB
# Submission Id: 1057103642


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], 1 + dp[i-coin])
        return dp[-1] if dp[-1] != float('inf') else -1