# 0518 - Coin Change II
# Date: 2022-11-09
# Runtime: 302 ms, Memory: 14.1 MB
# Submission Id: 839894802


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]

        return dp[-1]