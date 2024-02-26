# 0188 - Best Time to Buy and Sell Stock IV
# Date: 2023-09-24
# Runtime: 245 ms, Memory: 81.1 MB
# Submission Id: 1057853108


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        @cache
        def dp(i, is_hold, remains):
            if i >= n or remains == 0:
                return 0
            
            ans = dp(i+1, is_hold, remains)
            if is_hold:  # sell
                ans = max(ans, prices[i] + dp(i+1, False, remains-1))
            else:  # buy
                ans = max(ans, -prices[i] + dp(i+1, True, remains))
            return ans

        return dp(0, False, k)
            