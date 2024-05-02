# 0121 - Best Time to Buy and Sell Stock
# Date: 2024-05-01
# Runtime: 765 ms, Memory: 27.4 MB
# Submission Id: 1246371085


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, curr_min = 0, 10001
        for price in prices:
            curr_min = min(curr_min, price)
            ans = max(ans, price - curr_min)
        
        return ans