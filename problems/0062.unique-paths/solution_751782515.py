# 0062 - Unique Paths
# Date: 2022-07-20
# Runtime: 62 ms, Memory: 13.9 MB
# Submission Id: 751782515


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * m
        for r in range(1, n):
            for c in range(1, m):
                dp[c] += dp[c-1]
        return dp[-1]