# 0309 - Best Time to Buy and Sell Stock with Cooldown
# Date: 2022-10-29
# Runtime: 93 ms, Memory: 14.2 MB
# Submission Id: 832723732


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p2_sell = p1_sell = sell = 0
        p1_buy = buy = float('-inf')
        for price in prices:
            sell = max(p1_sell, p1_buy + price)
            buy = max(p1_buy, p2_sell - price)
            p2_sell, p1_sell, p1_buy = p1_sell, sell, buy
        return p1_sell