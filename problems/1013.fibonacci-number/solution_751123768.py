# 1013 - Fibonacci Number
# Date: 2022-07-19
# Runtime: 50 ms, Memory: 13.9 MB
# Submission Id: 751123768


class Solution:
    cache = {0: 0, 1: 1}
    def fib(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = self.fib(n-2) + self.fib(n-1)
        return self.cache[n]