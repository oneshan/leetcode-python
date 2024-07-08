# 0826 - Soup Servings
# Date: 2024-06-07
# Runtime: 97 ms, Memory: 17.7 MB
# Submission Id: 1280506070


class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4800:
            return 1
            
        n = (n+24) // 25
        dp = [[0] * (n+1) for _ in range(n+1)]
        dp[-1][-1] = 1

        for i in range(n, 0, -1):
            for j in range(n, 0, -1):
                prob = dp[i][j] / 4
                dp[max(i-4, 0)][max(j, 0)] += prob
                dp[max(i-3, 0)][max(j-1, 0)] += prob
                dp[max(i-2, 0)][max(j-2, 0)] += prob
                dp[max(i-1, 0)][max(j-3, 0)] += prob

        return sum(dp[0]) - dp[0][0] / 2