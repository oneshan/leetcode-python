# 0747 - Min Cost Climbing Stairs
# Date: 2022-10-22
# Runtime: 56 ms, Memory: 14 MB
# Submission Id: 827767893


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        p2, p1 = cost[0], cost[1]
        for i in range(2, n):
            p2, p1 = p1, min(p1, p2) + cost[i]
        return min(p2, p1)