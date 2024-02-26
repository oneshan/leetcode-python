# 0122 - Best Time to Buy and Sell Stock II
# Date: 2023-07-25
# Runtime: 76 ms, Memory: 17.7 MB
# Submission Id: 1003225439


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                ans += prices[i] - prices[i-1]
        return ans