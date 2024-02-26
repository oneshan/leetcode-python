# 0518 - Coin Change II
# Date: 2023-08-11
# Runtime: 117 ms, Memory: 16.4 MB
# Submission Id: 1018048712


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount+1)
        dp[0] = 1
        
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[-1]