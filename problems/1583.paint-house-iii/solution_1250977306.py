# 1583 - Paint House III
# Date: 2024-05-06
# Runtime: 950 ms, Memory: 51.8 MB
# Submission Id: 1250977306


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        @cache
        def dp(i, prev_c, curr_t):
            if curr_t > target:
                return float('inf')
            if i == m:
                return 0 if curr_t == target else float('inf')
            
            res = float('inf')
            if houses[i] == 0:
                for c in range(1, n+1):
                    next_t = curr_t if c == prev_c else curr_t + 1
                    res = min(res, cost[i][c-1] + dp(i+1, c, next_t))
            else:
                next_t = curr_t if houses[i] == prev_c else curr_t + 1
                res = dp(i+1, houses[i], next_t)
            return res
        
        res = dp(0, 0, 0)
        return res if res != float('inf') else -1