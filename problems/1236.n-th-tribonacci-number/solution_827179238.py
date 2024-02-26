# 1236 - N-th Tribonacci Number
# Date: 2022-10-21
# Runtime: 46 ms, Memory: 13.8 MB
# Submission Id: 827179238


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1
        
        p3, p2, p1 = 0, 1, 1
        for i in range(3, n+1):
            p3, p2, p1 = p2, p1, p3+p2+p1
        return p1
        