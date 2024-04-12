# 1236 - N-th Tribonacci Number
# Date: 2024-04-11
# Runtime: 42 ms, Memory: 16.5 MB
# Submission Id: 1229199226


class Solution:
    def tribonacci(self, n: int) -> int:
        
        @cache
        def dp(i):
            if i == 0:
                return 0
            if i < 3:
                return 1
            return dp(i-3) + dp(i-2) + dp(i-1)

        return dp(n)