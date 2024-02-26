# 0826 - Soup Servings
# Date: 2023-07-29
# Runtime: 55 ms, Memory: 17 MB
# Submission Id: 1006547062


class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1

        m = (n + 24) // 25        
        dp = [[0] * (m+1) for _ in range(m+1)]
        dp[m][m] = 1
        for i in range(m, 0, -1):
            for j in range(m, 0, -1):
                dp[max(0, i-4)][max(0, j)] += dp[i][j] / 4
                dp[max(0, i-3)][max(0, j-1)] += dp[i][j] / 4
                dp[max(0, i-2)][max(0, j-2)] += dp[i][j] / 4
                dp[max(0, i-1)][max(0, j-3)] += dp[i][j] / 4
        
        return sum(dp[0]) - dp[0][0] / 2