# 0747 - Min Cost Climbing Stairs
# Date: 2024-04-29
# Runtime: 43 ms, Memory: 16.6 MB
# Submission Id: 1244827847


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        p2, p1 = cost[0], cost[1]
        for i in range(2, n):
            p2, p1 = p1, min(p1, p2) + cost[i]
        return min(p1, p2)