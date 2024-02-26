# 0070 - Climbing Stairs
# Date: 2022-10-22
# Runtime: 39 ms, Memory: 13.9 MB
# Submission Id: 827763532


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        p2, p1 = 1, 2
        for i in range(3, n+1):
            p2, p1 = p1, p1+p2
        return p1