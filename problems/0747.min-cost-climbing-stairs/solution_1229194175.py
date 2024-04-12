# 0747 - Min Cost Climbing Stairs
# Date: 2024-04-11
# Runtime: 50 ms, Memory: 16.7 MB
# Submission Id: 1229194175


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        p1 = p2 = 0
        for c in cost:
            p2, p1 = p1, min(p1, p2) + c
        return min(p1, p2)