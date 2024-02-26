# 0070 - Climbing Stairs
# Date: 2024-01-18
# Runtime: 35 ms, Memory: 17.4 MB
# Submission Id: 1149550331


class Solution:
    def climbStairs(self, n: int) -> int:
        p2 = p1 = 1
        for i in range(1, n):
            p2, p1 = p1, p1+p2
        return p1