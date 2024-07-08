# 0322 - Coin Change
# Date: 2024-05-24
# Runtime: 695 ms, Memory: 16.9 MB
# Submission Id: 1266376707


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (1 + amount)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], 1 + dp[i-coin])

        return dp[-1] if dp[-1] != float('inf') else -1