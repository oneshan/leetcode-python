# 0322 - Coin Change
# Date: 2024-04-18
# Runtime: 715 ms, Memory: 16.9 MB
# Submission Id: 1235506123


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], 1 + dp[i-coin])
        return dp[-1] if dp[-1] != float('inf') else -1