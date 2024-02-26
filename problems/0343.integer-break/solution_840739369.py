# 0343 - Integer Break
# Date: 2022-11-10
# Runtime: 58 ms, Memory: 13.9 MB
# Submission Id: 840739369


class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1
        
        dp = [0] * (n+1)
        dp[2] = 1
        dp[3] = 2
        dp[4] = 4
        
        for i in range(5, n+1):
            dp[i] = 3 * max(i-3, dp[i-3])
        return dp[-1]