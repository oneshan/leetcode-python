# 0747 - Min Cost Climbing Stairs
# Date: 2023-10-13
# Runtime: 57 ms, Memory: 16.3 MB
# Submission Id: 1074239002


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        p2, p1 = cost[0], cost[1]
        for i in range(2, n):
            p2, p1 = p1, min(p1, p2) + cost[i]
        return min(p2, p1)