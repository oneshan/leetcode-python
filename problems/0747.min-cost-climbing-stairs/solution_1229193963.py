# 0747 - Min Cost Climbing Stairs
# Date: 2024-04-11
# Runtime: 59 ms, Memory: 19.6 MB
# Submission Id: 1229193963


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @cache
        def dp(i):
            if i >= len(cost):
                return 0
            return min(dp(i+1), dp(i+2)) + cost[i]
        
        return min(dp(0), dp(1))