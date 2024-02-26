# 0062 - Unique Paths
# Date: 2022-11-07
# Runtime: 59 ms, Memory: 13.9 MB
# Submission Id: 838686802


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for r in range(1, m):
            for c in range(1, n):
                dp[c] += dp[c-1]
        return dp[-1]