# 0309 - Best Time to Buy and Sell Stock with Cooldown
# Date: 2023-09-24
# Runtime: 39 ms, Memory: 16.5 MB
# Submission Id: 1057857169


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p2_sell = p1_sell = sell = 0
        p1_buy = buy = float('-inf')
        for price in prices:
            sell = max(p1_sell, p1_buy + price)
            buy = max(p1_buy, p2_sell - price)
            p2_sell, p1_sell, p1_buy = p1_sell, sell, buy
        return p1_sell