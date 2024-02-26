# 1013 - Fibonacci Number
# Date: 2022-10-27
# Runtime: 29 ms, Memory: 13.9 MB
# Submission Id: 831402911


class Solution:
    def fib(self, n: int) -> int:
        memo = {}

        def recur(n):
            if n <= 1:
                return n
            if n not in memo:
                memo[n] = recur(n-2) + recur(n-1)
            return memo[n]
        
        return recur(n)