# 0714 - Best Time to Buy and Sell Stock with Transaction Fee
# Date: 2024-05-02
# Runtime: 482 ms, Memory: 23.5 MB
# Submission Id: 1247375131


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        take, notake = float('-inf'), 0
        
        for price in prices:
            take = max(take, notake-price)
            notake = max(notake, take+price-fee)
            
        return max(take, notake)