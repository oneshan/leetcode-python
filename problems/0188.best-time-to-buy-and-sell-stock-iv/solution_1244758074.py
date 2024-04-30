# 0188 - Best Time to Buy and Sell Stock IV
# Date: 2024-04-29
# Runtime: 238 ms, Memory: 81.3 MB
# Submission Id: 1244758074


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        
        @cache
        def dp(i, k, is_hold):
            if i == len(prices) or k == 0:
                return 0
            
            # do nothing
            res = dp(i+1, k, is_hold)
            
            if is_hold:  # sell
                res = max(res, prices[i] + dp(i+1, k-1, False))
            else:  # buy
                res = max(res, -prices[i] + dp(i+1, k, True))
                
            return res
        
        return dp(0, k, False)