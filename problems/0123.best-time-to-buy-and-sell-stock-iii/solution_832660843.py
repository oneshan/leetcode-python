# 0123 - Best Time to Buy and Sell Stock III
# Date: 2022-10-29
# Runtime: 2983 ms, Memory: 27.8 MB
# Submission Id: 832660843


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        
        t1_cost = t2_cost = float('inf')
        t1_profit = t2_profit = 0
        
        for price in prices:
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price-t1_cost)
            
            # the cost of reinvestment
            t2_cost = min(t2_cost, price-t1_profit)
            t2_profit = max(t2_profit, price-t2_cost)
            
        return t2_profit