# 0070 - Climbing Stairs
# Date: 2024-02-12
# Runtime: 33 ms, Memory: 16.5 MB
# Submission Id: 1172707108


class Solution:
    def climbStairs(self, n: int) -> int:
        p1 = p2 = 1
        for i in range(1, n):
            p2, p1 = p1, p1 + p2
        return p1