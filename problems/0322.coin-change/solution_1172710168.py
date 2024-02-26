# 0322 - Coin Change
# Date: 2024-02-12
# Runtime: 707 ms, Memory: 16.9 MB
# Submission Id: 1172710168


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i-coin]+1, dp[i])

        return dp[-1] if dp[-1] != float('inf') else -1