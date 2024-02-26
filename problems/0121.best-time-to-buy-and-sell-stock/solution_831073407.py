# 0121 - Best Time to Buy and Sell Stock
# Date: 2022-10-27
# Runtime: 2959 ms, Memory: 25.1 MB
# Submission Id: 831073407


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, curr_min = 0, float('inf')
        for price in prices:
            curr_min = min(curr_min, price)
            ans = max(ans, price-curr_min)
        return ans