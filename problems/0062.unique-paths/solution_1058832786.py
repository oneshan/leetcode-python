# 0062 - Unique Paths
# Date: 2023-09-25
# Runtime: 44 ms, Memory: 16.2 MB
# Submission Id: 1058832786


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for r in range(1, m):
            for c in range(1, n):
                dp[c] += dp[c-1]
        return dp[-1]