# 0747 - Min Cost Climbing Stairs
# Date: 2024-04-29
# Runtime: 58 ms, Memory: 19.6 MB
# Submission Id: 1244829248


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        @cache
        def dp(i):
            if i <= 1:
                return 0
            return min(
                dp(i-1) + cost[i-1],
                dp(i-2) + cost[i-2],
            )
            
        return dp(n)