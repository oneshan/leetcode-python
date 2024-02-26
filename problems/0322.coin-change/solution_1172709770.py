# 0322 - Coin Change
# Date: 2024-02-12
# Runtime: 871 ms, Memory: 16.9 MB
# Submission Id: 1172709770


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        coins.sort()
        for i in range(amount):
            for coin in coins:
                if i + coin > amount:
                    break
                dp[i+coin] = min(dp[i]+1, dp[i+coin])
        return dp[-1] if dp[-1] != float('inf') else -1