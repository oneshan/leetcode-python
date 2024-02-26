# 0867 - New 21 Game
# Date: 2023-05-25
# Runtime: 95 ms, Memory: 16.7 MB
# Submission Id: 956889268


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or k + maxPts - 1 <= n:
            return 1
        
        dp = [0] * (n+1)
        dp[0] = 1
        
        curr = 1
        for i in range(1, n+1):
            dp[i] = curr / maxPts
            if i < k:
                curr += dp[i]
            if i >= maxPts:
                curr -= dp[i-maxPts]
        return sum(dp[k:])