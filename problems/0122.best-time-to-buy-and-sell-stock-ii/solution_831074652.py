# 0122 - Best Time to Buy and Sell Stock II
# Date: 2022-10-27
# Runtime: 65 ms, Memory: 15.3 MB
# Submission Id: 831074652


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, prev = 0, prices[0]
        for price in prices:
            ans = max(ans, ans+price-prev)
            prev = price
        return ans