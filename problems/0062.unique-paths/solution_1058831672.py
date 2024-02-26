# 0062 - Unique Paths
# Date: 2023-09-25
# Runtime: 20 ms, Memory: 16.2 MB
# Submission Id: 1058831672


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for r in range(m):
            dp[r][0] = 1
        for c in range(n):
            dp[0][c] = 1
        
        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[-1][-1]
            