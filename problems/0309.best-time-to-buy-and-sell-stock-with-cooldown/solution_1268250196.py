# 0309 - Best Time to Buy and Sell Stock with Cooldown
# Date: 2024-05-26
# Runtime: 43 ms, Memory: 16.7 MB
# Submission Id: 1268250196


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        p1_hold = float('-inf')
        p2_free = p1_free = 0
        for price in prices:
            # buy / do nothing
            hold = max(p1_hold, p2_free - price)
            # sell / do nothing
            free = max(p1_free, p1_hold + price)
            
            p2_free, p1_free, p1_hold = p1_free, free, hold

        return free