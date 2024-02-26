# 0714 - Best Time to Buy and Sell Stock with Transaction Fee
# Date: 2023-09-24
# Runtime: 575 ms, Memory: 23.5 MB
# Submission Id: 1057856530


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold, free = -prices[0], 0
        for i in range(1, len(prices)):
            free = max(free, hold + prices[i] - fee)
            hold = max(hold, free - prices[i])            
        return free