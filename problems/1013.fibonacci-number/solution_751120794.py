# 1013 - Fibonacci Number
# Date: 2022-07-19
# Runtime: 35 ms, Memory: 13.8 MB
# Submission Id: 751120794


class Solution:
    def fib(self, n: int) -> int:
        p2, p1 = 0, 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        for i in range(1, n):
            p2, p1 = p1, p1 + p2
        return p1