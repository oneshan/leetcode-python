# 0072 - Edit Distance
# Date: 2023-02-26
# Runtime: 157 ms, Memory: 17.6 MB
# Submission Id: 904990987


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for r in range(m+1):
            dp[r][0] = r
        for c in range(n+1):
            dp[0][c] = c
            
        for r in range(m):
            for c in range(n):
                if word1[r] == word2[c]:
                    dp[r+1][c+1] = dp[r][c]
                else:
                    dp[r+1][c+1] = 1 + min(dp[r+1][c], dp[r][c+1], dp[r][c])
        return dp[-1][-1]