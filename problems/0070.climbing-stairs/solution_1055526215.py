# 0070 - Climbing Stairs
# Date: 2023-09-21
# Runtime: 44 ms, Memory: 16.1 MB
# Submission Id: 1055526215


class Solution:
    def climbStairs(self, n: int) -> int:
        p2 = p1 = 1
        for i in range(2, n+1):
            p2, p1 = p1, p1+p2
        return p1