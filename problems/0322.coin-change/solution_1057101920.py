# 0322 - Coin Change
# Date: 2023-09-23
# Runtime: 986 ms, Memory: 37.1 MB
# Submission Id: 1057101920


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def dp(i):
            if i < 0:
                return -1
            if i == 0:
                return 0
            
            min_cost = float('inf')
            for coin in coins:
                res = dp(i-coin)
                if res != -1:
                    min_cost = min(min_cost, 1 + res)
            return min_cost if min_cost != float('inf') else -1
        
        return dp(amount)