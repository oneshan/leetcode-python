# 0309 - Best Time to Buy and Sell Stock with Cooldown
# Date: 2022-10-29
# Runtime: 76 ms, Memory: 14.2 MB
# Submission Id: 832719450


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        
        sell = [0] * n
        buy = [0] * n
        
        buy[0] = -prices[0]
        for i in range(1, n):
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
            buy[i] = max(buy[i-1], (sell[i-2] if i >= 2 else 0) - prices[i])
        return sell[-1]