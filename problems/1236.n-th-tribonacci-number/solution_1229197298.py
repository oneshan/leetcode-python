# 1236 - N-th Tribonacci Number
# Date: 2024-04-11
# Runtime: 33 ms, Memory: 16.5 MB
# Submission Id: 1229197298


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        
        # T(n) = T(n-1) + T(n-2) + T(n-3)
        p3, p2, p1 = 0, 1, 1
        for i in range(3, n+1):
            p3, p2, p1 = p2, p1, p1+p2+p3
        return p1