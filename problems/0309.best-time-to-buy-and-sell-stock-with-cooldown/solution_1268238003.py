# 0309 - Best Time to Buy and Sell Stock with Cooldown
# Date: 2024-05-26
# Runtime: 65 ms, Memory: 20.5 MB
# Submission Id: 1268238003


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dp(i, hold):
            if i >= n:
                return 0

            # do nothing
            res = dp(i+1, hold)

            if hold:
                # sell
                res = max(res, prices[i] + dp(i+2, False))
            else:
                # buy
                res = max(res, -prices[i] + dp(i+1, True))

            return res

        return dp(0, False)