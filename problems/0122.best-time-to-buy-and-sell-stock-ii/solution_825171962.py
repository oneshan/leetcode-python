# 0122 - Best Time to Buy and Sell Stock II
# Date: 2022-10-18
# Runtime: 132 ms, Memory: 15.2 MB
# Submission Id: 825171962


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                ans += prices[i] - prices[i-1]
        return ans