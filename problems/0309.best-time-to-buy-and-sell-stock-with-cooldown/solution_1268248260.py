# 0309 - Best Time to Buy and Sell Stock with Cooldown
# Date: 2024-05-26
# Runtime: 50 ms, Memory: 17 MB
# Submission Id: 1268248260


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # dp[day][hold]
        dp = [[0] * 2 for _ in range(n+2)]
        dp[0][1] = dp[1][1] = float('-inf')

        for i in range(2, n+2):
            # do-nothing
            dp[i][0] = dp[i-1][0]
            dp[i][1] = dp[i-1][1]
            # buy
            dp[i][1] = max(dp[i][1], dp[i-2][0] - prices[i-2])
            # sell
            dp[i][0] = max(dp[i][0], dp[i-1][1] + prices[i-2])
        
        return dp[-1][0]