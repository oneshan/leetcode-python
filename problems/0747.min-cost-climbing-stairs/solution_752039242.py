# 0747 - Min Cost Climbing Stairs
# Date: 2022-07-20
# Runtime: 94 ms, Memory: 13.9 MB
# Submission Id: 752039242


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        p2, p1 = 0, 0
        for c in cost:
            p2, p1 = p1, min(p1, p2)+c
        return min(p1, p2)