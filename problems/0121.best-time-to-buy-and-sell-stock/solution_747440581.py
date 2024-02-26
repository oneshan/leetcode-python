# 0121 - Best Time to Buy and Sell Stock
# Date: 2022-07-15
# Runtime: 1501 ms, Memory: 25 MB
# Submission Id: 747440581


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        ans = 0
        curr_min = prices[0]
        for price in prices:
            ans = max(ans, price-curr_min)
            curr_min = min(curr_min, price)
        return ans