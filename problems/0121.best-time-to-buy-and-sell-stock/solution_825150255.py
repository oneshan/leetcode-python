# 0121 - Best Time to Buy and Sell Stock
# Date: 2022-10-18
# Runtime: 2561 ms, Memory: 25.1 MB
# Submission Id: 825150255


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, curr_min = 0, prices[0]
        for i in range(1, len(prices)):
            ans = max(ans, prices[i] - curr_min)
            curr_min = min(curr_min, prices[i])
        return ans