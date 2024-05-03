# 0062 - Unique Paths
# Date: 2024-05-02
# Runtime: 32 ms, Memory: 16.5 MB
# Submission Id: 1247232465


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [1] * n
        for r in range(1, m):
            for c in range(1, n):
                dp[c] = dp[c-1] + dp[c]
            
        return dp[-1]