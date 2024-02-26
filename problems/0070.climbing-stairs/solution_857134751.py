# 0070 - Climbing Stairs
# Date: 2022-12-09
# Runtime: 37 ms, Memory: 13.9 MB
# Submission Id: 857134751


class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def dp(i):
            if i < 2:
                return 1
            return dp(i-1) + dp(i-2)
        
        return dp(n)