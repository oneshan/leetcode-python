# 0070 - Climbing Stairs
# Date: 2022-07-19
# Runtime: 52 ms, Memory: 13.8 MB
# Submission Id: 751126930


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        p2, p1 = 1, 2
        for i in range(3, n+1):
            p2, p1 = p1, p1+p2
        return p1