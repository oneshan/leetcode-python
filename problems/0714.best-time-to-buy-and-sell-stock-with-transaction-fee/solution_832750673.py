# 0714 - Best Time to Buy and Sell Stock with Transaction Fee
# Date: 2022-10-29
# Runtime: 1788 ms, Memory: 21.2 MB
# Submission Id: 832750673


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit, cost = 0, -prices[0]
        for i in range(1, len(prices)):
            profit = max(profit, cost + prices[i] - fee)
            cost = max(cost, profit - prices[i])
        return profit