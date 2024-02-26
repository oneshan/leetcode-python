# 0062 - Unique Paths
# Date: 2023-09-03
# Runtime: 36 ms, Memory: 16.4 MB
# Submission Id: 1039090969


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for r in range(1, m):
            for c in range(1, n):
                dp[c] += dp[c-1]
        return dp[-1]