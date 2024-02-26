# 0714 - Best Time to Buy and Sell Stock with Transaction Fee
# Date: 2022-10-29
# Runtime: 1677 ms, Memory: 21.4 MB
# Submission Id: 832747277


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        prev_buy = buy = float('-inf')
        prev_sell = sell = 0
        
        for price in prices:
            sell = max(prev_sell, prev_buy + price - fee)
            buy = max(prev_buy, prev_sell - price)
            prev_buy, prev_sell = buy, sell
        return prev_sell