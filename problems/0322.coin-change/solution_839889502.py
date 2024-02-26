# 0322 - Coin Change
# Date: 2022-11-09
# Runtime: 1745 ms, Memory: 14.3 MB
# Submission Id: 839889502


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount] != float('inf') else -1