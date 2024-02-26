# 0322 - Coin Change
# Date: 2022-11-09
# Runtime: 3414 ms, Memory: 35.2 MB
# Submission Id: 839891797


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @lru_cache(None)
        def dfs(rem):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            
            min_cost = float('inf')
            for coin in coins:
                res = dfs(rem-coin)
                if res != -1:
                    min_cost = min(min_cost, res + 1)
            return min_cost if min_cost != float('inf') else -1
        
        return dfs(amount)