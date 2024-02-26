# 0123 - Best Time to Buy and Sell Stock III
# Date: 2022-10-29
# Runtime: 3324 ms, Memory: 28.9 MB
# Submission Id: 832657509


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        
        left_profits = [0] * n
        right_profits = [0] * (n+1)
        
        curr_min = prices[0]
        for i in range(1, n):
            left_profits[i] = max(left_profits[i-1], prices[i]-curr_min)
            curr_min = min(curr_min, prices[i])
        
        curr_max = prices[-1]
        for i in range(n-2, -1, -1):
            right_profits[i] = max(right_profits[i+1], curr_max-prices[i])
            curr_max = max(curr_max, prices[i])
            
        ans = 0
        for i in range(n):
            ans = max(ans, left_profits[i] + right_profits[i+1])
        return ans