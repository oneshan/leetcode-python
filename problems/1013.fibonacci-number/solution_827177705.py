# 1013 - Fibonacci Number
# Date: 2022-10-21
# Runtime: 36 ms, Memory: 13.9 MB
# Submission Id: 827177705


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        prev_2, prev_1 = 0, 1
        for i in range(2, n+1):
            prev_2, prev_1 = prev_1, prev_1 + prev_2
        return prev_1