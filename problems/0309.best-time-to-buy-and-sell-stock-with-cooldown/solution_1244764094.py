# 0309 - Best Time to Buy and Sell Stock with Cooldown
# Date: 2024-04-29
# Runtime: 31 ms, Memory: 20.6 MB
# Submission Id: 1244764094


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def dp(i, is_hold):
            if i >= len(prices):
                return 0

            # do nothing
            res = dp(i+1, is_hold)
            
            if is_hold: # sell
                res = max(res, prices[i] + dp(i+2, False))
            else: # buy
                res = max(res, -prices[i] + dp(i+1, True))
            return res
        
        return dp(0, False)