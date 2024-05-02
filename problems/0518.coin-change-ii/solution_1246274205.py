# 0518 - Coin Change II
# Date: 2024-05-01
# Runtime: 95 ms, Memory: 16.8 MB
# Submission Id: 1246274205


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[-1]