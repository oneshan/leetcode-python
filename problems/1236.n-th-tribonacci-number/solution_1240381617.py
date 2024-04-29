# 1236 - N-th Tribonacci Number
# Date: 2024-04-24
# Runtime: 24 ms, Memory: 16.5 MB
# Submission Id: 1240381617


class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n == 0:
            return 0
        if n < 3:
            return 1

        p3, p2, p1 = 0, 1, 1
        for _ in range(3, n+1):
            p3, p2, p1 = p2, p1, p1+p2+p3
        return p1