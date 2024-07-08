# 3414 - Find Number of Ways to Reach the K-th Stair
# Date: 2024-05-19
# Runtime: 115 ms, Memory: 18.4 MB
# Submission Id: 1261955128


class Solution:
    def waysToReachStair(self, k: int) -> int:
        
        @cache
        def dp(i, jump, prev_down):
            res = (i == k)
            if i > 0 and not prev_down:
                res += dp(i-1, jump, True)
            if i <= k+1:
                res += dp(i + (1<<jump), jump+1, False)
            return res
        
        return dp(1, 0, False)