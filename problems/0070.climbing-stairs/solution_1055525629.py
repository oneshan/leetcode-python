# 0070 - Climbing Stairs
# Date: 2023-09-21
# Runtime: 37 ms, Memory: 16.2 MB
# Submission Id: 1055525629


class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]