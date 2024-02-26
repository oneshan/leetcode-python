# 0188 - Best Time to Buy and Sell Stock IV
# Date: 2022-10-29
# Runtime: 304 ms, Memory: 14 MB
# Submission Id: 832664035


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        cost = [float('inf')] * k
        profit = [0] * k
        
        for price in prices:
            cost[0] = min(cost[0], price)
            profit[0] = max(profit[0], price-cost[0])

            for i in range(1, k):
                cost[i] = min(cost[i], price-profit[i-1])
                profit[i] = max(profit[i], price-cost[i])

        return max(profit)