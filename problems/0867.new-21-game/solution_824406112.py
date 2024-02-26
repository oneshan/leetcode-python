# 0867 - New 21 Game
# Date: 2022-10-17
# Runtime: 63 ms, Memory: 14.3 MB
# Submission Id: 824406112


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0] * (n + maxPts + 1)
        for i in range(k, n+1):
            dp[i] = 1
            
        s = min(n+1-k, maxPts)
        for i in range(k-1, -1, -1):
            dp[i] = s / maxPts
            s += dp[i] - dp[i+maxPts]
        return dp[0]