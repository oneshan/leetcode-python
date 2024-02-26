# 0070 - Climbing Stairs
# Date: 2022-10-27
# Runtime: 69 ms, Memory: 13.8 MB
# Submission Id: 831410485


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def recur(n):
            if n < 3:
                return n
            if n not in memo:
                memo[n] = recur(n-1) + recur(n-2)
            return memo[n]
        return recur(n)